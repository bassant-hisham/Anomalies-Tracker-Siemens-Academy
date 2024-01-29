import jenkins
import time
import logging
import os
import config

from typing import Union


class JenkinsWrapper:
    def __init__(self, url: str, username: str, password: str):
        """
        initializes a Jenkins server object.
        
        :param url: The `url` represents the URL of the Jenkins server. in the format `http://<jenkins-server-url>`
        :param username: The `username` used to authenticate with the Jenkins server.
        :param password: The `password` for the Jenkins server.
        """
        try:
            self.server = jenkins.Jenkins(url, username=username, password=password)
        except jenkins.JenkinsException as e:
            message = f"Failed to initialize Jenkins server: {str(e)}"
            logging.fatal(message)
            self.server = None

    
    def create_job_from_xml(self, job_name: str, xml_config: str) -> bool:
        """
        creates a job in Jenkins using the provided XML configuration
        
        :param job_name: name of the job to create in Jenkins
        :param xml_config: XML configuration for the job to create.
        :return: It returns True if the job was created successfully and False if there was an error creating the job.
        """
        try:
            self.server.upsert_job(job_name, xml_config)
            message = f"Job '{job_name}' created successfully"
            logging.info(message)
            return True
        except jenkins.JenkinsException as e:
            message = f"Failed to create job '{job_name}': {str(e)}"
            logging.error(message)
            return False


    def build_job(self, job_name: str) -> int:
        """
        build a job with the given name on a Jenkins server
        
        :param job_name: the name of the job that you want to build
        :return: `int` queue item
        """
        try:
            return self.server.build_job(job_name)
        except jenkins.JenkinsException as e:
            message = f"Failed to build job '{job_name}': {str(e)}"
            logging.error(message)
            return -1


    def delete_job(self, job_name: str) -> bool:
        """
        deletes a job from Jenkins server.
        
        :param job_name: the name of the job that you want to delete
        :return: If the job is successfully deleted, it returns True. If there is an
        exception (jenkins.JenkinsException) while deleting the job, it returns False.
        """
        try:
            self.server.delete_job(job_name)
            message = f"Successfully deleted job '{job_name}'."
            logging.info(message)
            return True
        except jenkins.JenkinsException as e:
            message = f"Failed to delete job '{job_name}': {str(e)}"
            logging.error(message) 
            return False
        

    def abort_build(self, job_name: str, build_number: int) -> bool:
        """
        aborts a specific build of a job in Jenkins.
        
        :param job_name: the name of the job in Jenkins
        :param build_number: the number of a specific build of a job in Jenkins
        :return: If the build is successfully aborted, it returns True. If there is an
        exception while trying to abort the build, it returns False.
        """
        try:
            self.server.stop_build(job_name, build_number)
            message =  f"Build {build_number} of job '{job_name}' aborted successfully"
            logging.info(message) 
            return True
        except jenkins.JenkinsException as e:
            message = f"Failed to abort build {build_number} of job '{job_name}': {str(e)}"
            logging.error(message)
            return False


    def get_build_info(self, job_name: str, build_number: int) -> dict:
        """
        retrieves build information for a specific job and build number from Jenkins server.
        
        :param job_name: the name of the job in Jenkins
        :param build_number: integer that represents the specific build number of a job in Jenkins
        :return: dictionary of build information.
        """
        try:
            return self.server.get_build_info(job_name, build_number)
        except jenkins.JenkinsException as e:
            message = f"Failed to get build info for job '{job_name}' and build number '{build_number}': {str(e)}"
            logging.error(message) 
            return {}


    def get_build_console_output(self, job_name: str, build_number: int) -> Union[bool, str]:
        """
        Get build console text.
        
        :param job_name:the name of the Jenkins job for which you want to retrieve the build console output.
        :param build_number: represents the number of a specific build for a job in Jenkins.
        It is used to identify a particular build of a job
        :returns: Build console output.
        """
        try:
            return True, self.server.get_build_console_output(job_name, build_number)
        except jenkins.JenkinsException as e:
            message = f"Failed to get build output for job '{job_name}' and build number '{build_number}': {str(e)}"
            logging.error(message)
            return False, message


    def fetch_and_update_console_output(self, job_name: str, build_number: int) -> None:
        """
        The function fetches the console output of a Jenkins job and updates it in a text file.
        
        :param job_name: the name of the job in Jenkins for which you want to fetch and update the console output
        :param build_number: represents the specific build number of a job in Jenkins.
        """
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
    

    def get_last_build_number(self, job_name: str) -> int:
        """
        retrieves the last build number for a given job name using the Jenkins API.
        
        :param job_name: The name of the Jenkins job.
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
            message = f"Failed to get last build number for job '{job_name}': {str(e)}"
            logging.error(message)
            return -1

        
    def wait_for_job_creation(self, job_name: str) -> None:
        """
        Wait until the Jenkins job is created.
        
        :param job_name: The name of the Jenkins job.
        """
        start_time = time.time()

        while not self.server.job_exists(job_name):
            elapsed_time = time.time() - start_time
            if elapsed_time > config.WAIT_TIMEOUT:
                message = f"Timeout exceeded. Job '{job_name}' not created within {config.WAIT_TIMEOUT} seconds."
                logging.error(message)
                raise TimeoutError(message)


            message = f"Waiting for job '{job_name}' to be created..."
            logging.info(message) 
            time.sleep(5)

        message = f"Job '{job_name}' created successfully on the server"
        logging.info(message) 


    def is_job_in_queue(self, job_name: str) -> bool:
        """
        Checks if a job is in the build queue.

        :param job_name: The name of the Jenkins job.
        :return: True if the job is in the build queue, False otherwise.
        """
        queue_info = self.server.get_queue_info()
        for item in queue_info:
            task = item.get('task', {})
            if task.get('name') == job_name:
                return True
        return False


    def wait_for_job_to_start_building(self, job_name: str) -> None:
        """
        Waits for a job to start building.

        :param job_name: The name of the Jenkins job.
        """
        in_queue = True

        while in_queue:
            in_queue = self.is_job_in_queue(job_name)

            if in_queue:
                message = f"Job '{job_name}' in the queue."

            logging.info(message)
            time.sleep(5)

    
    def wait_for_job_to_finish_building(self, job_name: str, build_number: int) -> dict:
        """
        waits for a job in Jenkins to finish building by continuously checking its
        status every 5 seconds.
        
        :param job_name: The name of the Jenkins job.
        :param build_number: integer represents the specific build number of a job in Jenkins.
        """
        is_building = True

        while is_building:
            build_info = self.server.get_build_info(job_name, build_number)
            is_building = build_info['building']

            time.sleep(5)

        return build_info