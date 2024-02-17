from src.backend.jenkins_wrapper_package.JenkinsJobExecutor import JenkinsJobExecutor
from src.backend.jenkins_wrapper_package.JenkinsWrapper import JenkinsWrapper
from src.backend.job_generator.job_generator import create_jobs

import config


#to note jenkins jobs is letter case insensitive --> git = Git = giT = GIT
JENKINS_SERVER = JenkinsWrapper(config.JenkinsConfig.JENKINS_URL,
                            config.JenkinsConfig.JENKINS_USERNAME,
                            config.JenkinsConfig.JENKINS_PASSWORD)



class Jenkins:

#0
    def __init__(self):
        self.job_executor = JenkinsJobExecutor()


#1
    # def start_all_jobs(self , json_object):
    #     job_names = create_jobs(json_object, JENKINS_API.server)
    #     self.job_executor.run_all_jobs(JENKINS_API, job_names)

    def start_jobs_in_batches(self, json_object ,isbinarysearch, batch_size = 10):
        job_names = create_jobs(json_object,JENKINS_SERVER.server)
        self.job_executor.run_jobs_in_batches(JENKINS_SERVER, job_names, batch_size)

#2
    def stop_job(self, job_name):
        build_number = self.job_executor.get_build_number(job_name)
        return JENKINS_SERVER.abort_build(job_name , build_number)

#3
    def delete_job(self, job_name):
        JENKINS_SERVER.delete_job(job_name)

#4
    def get_job_console_output(self, job_name):
        build_number = self.job_executor.get_build_number(job_name)
        return JENKINS_SERVER.get_build_console_output(job_name,build_number)

#5
    def get_job_info(self, job_name):
        build_number = self.job_executor.get_build_number(job_name)
        print(JENKINS_SERVER.get_build_info(job_name , build_number))
        return JENKINS_SERVER.get_build_info(job_name , build_number)

#6
    def get_build_status(self, job_name):
        build_number = self.job_executor.get_build_number(job_name)
        return JENKINS_SERVER.get_build_status(job_name , build_number)

#7
    def get_job_commit_hash(self, job_name):   # needs to be tested
        return JENKINS_SERVER.get_git_commit(job_name)

#8
    def get_job_build_time(self, job_name):  #needs to be tested
        build_number = self.job_executor.get_build_number(job_name)
        return JENKINS_SERVER.get_execution_time(job_name , build_number)

#9
    # def binary_search_failure_finder(self):

    def get_job_status(self , jobname):
        return self.job_executor.get_job_status(jobname)
        

    def get_all_status(self):
        return self.job_executor.get_all_jobs_status()