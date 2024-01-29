from collections import deque

from src.backend.jenkins_wrapper_package.JenkinsWrapper import JenkinsWrapper
from src.backend.jenkins_wrapper_package.JenkinsBuildInfoRetriever import JenkinsBuildInfoRetriever

from src.backend.jenkins_wrapper_package.dependency_processor import topological_sort_in_batches
import threading
import logging
from enum import Enum

import config


class BuildState(Enum):
    JOB_CREATED = 'Job Created'
    JOB_IN_BATCH = 'Job In Batch'
    JOB_STARTED = 'Job Started'
    JOB_CRASHED = 'Job Crashed in Jenkins'





class JenkinsJobExecutor:

    def __init__(self):
        self.finished_jobs = []  #to be removed
        self.All_Jobs_Build_Numbers = {}        
        self.All_Jobs_Status = {}
        self.prerequisites = {}


    def run_job(self,jenkins_wrapper:JenkinsWrapper, job_name):
        try:
            queue_item = jenkins_wrapper.build_job(job_name)

            jenkins_wrapper.wait_for_job_to_start_building(job_name)

            build_number = jenkins_wrapper.get_last_build_number(job_name)

            self.All_Jobs_Status[job_name] = BuildState.JOB_STARTED.value
            self.All_Jobs_Build_Numbers[job_name] = build_number
            
            if config.DUMP_CONSOLE_OUTPUT:
                thread_fetch_output = threading.Thread(target=jenkins_wrapper.fetch_and_update_console_output,
                                                        args=(job_name, build_number))
                thread_fetch_output.start()
                thread_fetch_output.join()
            else:
                jenkins_wrapper.wait_for_job_to_finish_building(job_name, build_number)

            req_status, build_info = JenkinsBuildInfoRetriever.get_build_info(jenkins_wrapper.server,job_name,build_number)
            job_status = JenkinsBuildInfoRetriever.get_build_result(build_info)
            job_execution_time = JenkinsBuildInfoRetriever.get_execution_time(build_info)

            self.All_Jobs_Status[job_name] = job_status
            self.finished_jobs.append((job_name, job_status, job_execution_time))

            message = f"Job '{job_name}' finished with status: {job_status}  , execution time: {job_execution_time}"
            logging.info(message) 
            print(message)

            if config.DELETE_JOB_AFTER_FINISH:
                jenkins_wrapper.delete_job(job_name)

            return job_name, job_status, job_execution_time
        
        except Exception as e:
            message =f"Exception occurred for job '{job_name}': {e}"
            logging.error(message) 
            print(message)
            self.All_Jobs_Status[job_name] = BuildState.JOB_CRASHED.value

            if config.DELETE_JOB_AFTER_FINISH:
                jenkins_wrapper.delete_job(job_name)

    
    def run_all_jobs(self,server, jobs_to_execute):
        self.All_Jobs_Status.update({i: BuildState.JOB_IN_BATCH.value for i in jobs_to_execute})

        threads = []
        #  add All_Jobs_Info

        for job_name in jobs_to_execute:
            t = threading.Thread(target=self.run_job, args=(server,job_name))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return self.finished_jobs#no need 
    

    def run_jobs_in_batches(self,server , jobs_to_execute, batch_size):
        print(jobs_to_execute)
        self.All_Jobs_Status.update({i: BuildState.JOB_CREATED.value for i in jobs_to_execute})


        # jobs_to_execute = list(jobs_to_execute.keys())
        jobs_to_execute = topological_sort_in_batches(jobs_to_execute, batch_size)
        # batches = [jobs_to_execute[i:i + batch_size] for i in range(0, len(jobs_to_execute), batch_size)]

        for batch in jobs_to_execute:
            print(batch)
            self.run_all_jobs(server, batch)

        return self.finished_jobs #no need


    def topological_sort(self , dependencies):

        in_degree = {u: 0 for u in dependencies}
        for u in dependencies:
            for v in dependencies[u]:
                if v not in in_degree:
                    in_degree[v] = 0
                in_degree[v] += 1
        queue = deque([u for u in in_degree if in_degree[u] == 0])
        sorted_order = []

        while queue:
            u = queue.popleft()
            sorted_order.append(u)
            for v in dependencies.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(sorted_order) == len(in_degree):
            return sorted_order[::-1]
        else:
            raise Exception("A cycle was detected in the dependencies , please check")


    def binary_search_for_failure(self , jobs_to_execute , xml_configs):

        left = 0
        right = len(jobs_to_execute) - 1
        first_failure = None

        while left <= right:
            mid = left + (right - left) // 2
            build_status , job_name = self.job_thread(jobs_to_execute[mid] , xml_configs[mid])

            if build_status == 'Build Failure': #var
                first_failure = job_name
                right = mid - 1
            else:
                left = mid + 1

        return first_failure
    

    def get_build_number(self, job_name):
        return self.All_Jobs_Build_Numbers.get(job_name)
    

    def get_job_status(self, jobname):
        return self.All_Jobs_Status[jobname]
    

    def get_all_jobs_status(self):
        return self.All_Jobs_Status