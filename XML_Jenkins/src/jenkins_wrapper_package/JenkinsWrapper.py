import jenkins
import time
import logging
import os


class JenkinsWrapper:
    def __init__(self, url: str, username: str, password: str):
        try:
            self.server = jenkins.Jenkins(url, username=username, password=password)
        except jenkins.JenkinsException as e:
            message = f"Failed to initialize Jenkins server: {str(e)}"
            logging.fatal(message)
            print(message)
            self.server = None

    
    def create_job_from_xml(self, job_name: str, xml_config: str) -> bool:
        try:
            self.server.upsert_job(job_name, xml_config)
            message = f"Job '{job_name}' created successfully"
            logging.info(message)
            print(message)
            return True
        except jenkins.JenkinsException as e:
            message = f"Failed to create job '{job_name}': {str(e)}"
            logging.error(message)
            print(message)
            return False


    def build_job(self, job_name: str) -> dict:
        try:
            return self.server.build_job(job_name)
        except jenkins.JenkinsException as e:
            message = f"Failed to build job '{job_name}': {str(e)}"
            logging.error(message) and print(message)
            return {}


    def delete_job(self, job_name: str) -> bool:
        try:
            self.server.delete_job(job_name)
            message = f"Successfully deleted job '{job_name}'."
            logging.info(message)
            print(message)
            return True
        except jenkins.JenkinsException as e:
            message = f"Failed to delete job '{job_name}': {str(e)}"
            logging.error(message) 
            print(message)
            return False


    def get_build_info(self, job_name: str, build_number: int) -> dict:
        try:
            return self.server.get_build_info(job_name, build_number)
        except jenkins.JenkinsException as e:
            print(f"Failed to get build info for job '{job_name}' and build number '{build_number}': {str(e)}")
            return {}


    def get_build_output(self, job_name: str, build_number: int) -> str:
        try:
            return self.server.get_build_console_output(job_name, build_number)
        except jenkins.JenkinsException as e:
            print(f"Failed to get build output for job '{job_name}' and build number '{build_number}': {str(e)}")
            return ""


    def fetch_and_update_console_output(self, job_name: str, build_number: int) -> None:
        try:
            while True:
                console_output = self.server.get_build_console_output(job_name, build_number)
                output_folder = os.path.join(os.path.dirname(__file__),'..', '..', 'generated','console')
                os.makedirs(output_folder, exist_ok=True)

                output_file = os.path.join(output_folder, f"console_output_job_{job_name}_build_{build_number}.txt")


                with open(output_file, 'w') as file:
                    file.write(console_output)

                build_info = self.server.get_build_info(job_name, build_number)
                if not build_info['building']:
                    break

                time.sleep(5)
        except jenkins.JenkinsException as e:
            message =  f"Failed to fetch and update console output for job '{job_name}' and build number '{build_number}': {str(e)}"
            logging.error(message) 
            print(message)


    def abort_build(self, job_name: str, build_number: int) -> bool:
        try:
            self.server.stop_build(job_name, build_number)
            message =  f"Build {build_number} of job '{job_name}' aborted successfully"
            logging.info(message) 
            print(message)
            return True
        except jenkins.JenkinsException as e:
            print(f"Failed to abort build {build_number} of job '{job_name}': {str(e)}")
            return False
        
        
    def get_build_status(self, job_name: str, build_number: int) -> str:
        try:
            build_info = self.server.get_build_info(job_name, build_number)
            if build_info['building']:
                return "Build in progress"
            else:
                result = build_info['result']
                if result:
                    return f"Build {result.capitalize()}"
                else:
                    return "Build status unavailable"
        except jenkins.JenkinsException as e:
            print(f"Failed to get build status for job '{job_name}' and build number '{build_number}': {str(e)}")
            return "Error"


    def get_build_time(self, job_name: str, build_number: int) -> str:
        try:
            build_info = self.server.get_build_info(job_name, build_number)
            timestamp = build_info['timestamp']
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp / 1000))
        except jenkins.JenkinsException as e:
            print(f"Failed to get build time for job '{job_name}' and build number '{build_number}': {str(e)}")
            return ""
        
    
    def get_execution_time(self, job_name: str, build_number: int) -> str:
        """
        retrieves the execution time of a specific build in a Jenkins job and returns it in seconds.
        
        :param job_name: The name of the Jenkins job.
        :type job_name: str
        :param build_number: integer represents the specific build number of a job in Jenkins.
        :type build_number: int
        :return: a string that represents the execution time of a job in seconds.
        """
        try:
            build_info = self.server.get_build_info(job_name, build_number)
            duration = build_info['duration']
            execution_time_seconds = duration / 1000
            return f"{execution_time_seconds} seconds"
        except jenkins.JenkinsException as e:
            print(f"Failed to get execution time for job '{job_name}' and build number '{build_number}': {str(e)}")
            return ""


    def get_last_build_number(self, job_name: str) -> int:
        """
        retrieves the last build number for a given job name using the Jenkins API.
        
        :param job_name: The name of the Jenkins job.
        :type job_name: str
        :return: an integer value representing the last build number of a job. If the last build number is
        found in the job information, it is returned. If the last build number is not found or if there is
        an exception while retrieving the job information, the function returns 0 or -1 respectively.
        """
        try:
            job_info = self.server.get_job_info(job_name)
            if 'lastBuild' in job_info and job_info['lastBuild'] is not None:
                return job_info['lastBuild']['number']
            else:
                return 0
        except jenkins.JenkinsException as e:
            print(f"Failed to get last build number for job '{job_name}': {str(e)}")
            return -1
        

    def wait_for_job_creation(self, job_name: str) -> None:
        """
        Wait until the Jenkins job is created.
        
        :param job_name: The name of the Jenkins job.
        :type job_name: str
        """
        while not self.server.job_exists(job_name):
            message = f"Waiting for job '{job_name}' to be created..."
            logging.info(message) 
            print(message)
            time.sleep(5)

        message = f"Job '{job_name}' created successfully on the server"
        logging.info(message) 
        print(message)


    def wait_for_job_to_start_building(self, job_name: str) -> int:
        """
        waits for a job to start building and returns the build number.
        
        :param job_name: The name of the Jenkins job.
        :type job_name: str
        :return: an integer, which is the build number of the job that started building.
        """
        build_number = 0
        while build_number == 0:
            build_number = self.get_last_build_number(job_name)
            message =  f"Waiting for job '{job_name}' to start building"
            logging.info(message) 
            print(message)
            time.sleep(10)

        message = f"Job '{job_name}' started building. Build number: {build_number}"
        logging.info(message) 
        print(message)
        return build_number

    
    def wait_for_job_to_finish_building(self, job_name: str, build_number: int) -> None:
        """
        waits for a job in Jenkins to finish building by continuously checking its
        status every 5 seconds.
        
        :param job_name: The name of the Jenkins job.
        :type job_name: str
        :param build_number: integer represents the specific build number of a job in Jenkins.
        :type build_number: int
        """
        while self.server.get_build_info(job_name, build_number)['building']:
            time.sleep(5)