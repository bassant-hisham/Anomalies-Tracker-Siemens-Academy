from src.jenkins_wrapper_package.JenkinsWrapper import JenkinsWrapper
import threading
import json
import logging
import os





# **************************
# one instance of the server shared between threads   Vs   one instance for each thread.
# Exception occurred for job 'job_172': ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# connection pool is full, discarding connection: localhost. connection pool size: 10 jenkins
# **************************



class JenkinsJobExecutor:



    def __init__(self):
        self.finished_jobs = []
        self.All_Jobs_Info = {}



    def run_job(self,jenkins_wrapper, job_name):
        try:
            # jenkins_wrapper.create_job_from_xml(job_name, xml_config)

            # jenkins_wrapper.wait_for_job_creation(job_name)

            queue_item = jenkins_wrapper.build_job(job_name)

            build_number = jenkins_wrapper.wait_for_job_to_start_building(job_name)

            self.All_Jobs_Info[job_name] = build_number
            
            thread_fetch_output = threading.Thread(target=jenkins_wrapper.fetch_and_update_console_output,
                                                    args=(job_name, build_number))
            thread_fetch_output.start()

            thread_fetch_output.join()

            # jenkins_wrapper.wait_for_job_to_finish_building(job_name, build_number)

            job_status = jenkins_wrapper.get_build_status(job_name, build_number)
            job_execution_time = jenkins_wrapper.get_execution_time(job_name, build_number)
            self.finished_jobs.append((job_name, job_status, job_execution_time))

            message = f"Job '{job_name}' finished with status: {job_status}  , execution time: {job_execution_time}"
            logging.info(message) 
            print(message)

            #jenkins_wrapper.delete_job(job_name) # add flag

            return job_name, job_status, job_execution_time
        
        except Exception as e:
            message =f"Exception occurred for job '{job_name}': {e}"
            logging.error(message) 
            print(message)
            jenkins_wrapper.delete_job(job_name)

    
    def run_all_jobs(self,server, jobs_to_execute):
        threads = []
        #  add All_Jobs_Info
        # sol-task-job
        for job_name in jobs_to_execute:
            t = threading.Thread(target=self.run_job, args=(server,job_name))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return self.finished_jobs
    

    def run_jobs_in_batches(self,server , jobs_to_execute, batch_size):

        batches = [jobs_to_execute[i:i + batch_size] for i in range(0, len(jobs_to_execute), batch_size)]

        for batch in batches:
            print(batch)
            self.run_all_jobs(server, batch)

        return self.finished_jobs


    # def read_xml_configs_from_file(self , file_path):
    #     xml_configs = []
    #     try:
    #         with open(file_path, 'r') as file:
    #             xml_config = ""
    #             for line in file:
    #                 line = line.strip()
    #                 if line.startswith("<project>") and line.endswith("</project>"):
    #                     xml_config = line
    #                     xml_configs.append(xml_config)
    #                     xml_config = ""
    #     except FileNotFoundError:
    #         print(f"File '{file_path}' not found.")
    #     return xml_configs


    # def get_all_job_status_to_JSON(self):
    #     job_info_dict = {}
    #     for job_data in self.All_Jobs_Info:
    #         job_name, job_status, job_time = job_data
    #         job_info_dict[job_name] = {"job_status": job_status, "job_time": job_time}
    #     with open("job_info.json", 'w') as json_file:
    #         json.dump(job_info_dict, json_file, indent=4)


    # def custom_sort_by_status_and_version(self , entry):
    #     status_order = {
    #         'Build Failure': 1,
    #         'Build Success': 2
    #     }
    #     status = entry[1]
    #     version = int(entry[0].replace('-', ''))
    #     return (status_order.get(status, float('inf')), version)


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
        return self.All_Jobs_Info.get(job_name)
