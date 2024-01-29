import jenkins
import time
from typing import Union, Tuple



class JenkinsBuildInfoRetriever:        

    @staticmethod
    def get_build_info(server:jenkins.Jenkins, job_name: str, build_number: int) -> Tuple[bool, Union[dict ,str]]:
        """
        Get build information dictionary.

        :return: tuple containing two elements. The first boolean value indicating whether the build information
        was successfully retrieved or not. The second element is either a dictionary containing the build
        information or a string indicating the failure reason if the build information retrieval failed.
        """
        try:
            return True, server.get_build_info(job_name, build_number)
        except jenkins.JenkinsException as e:
            return False, f"Failed to get build info for job '{job_name}' and build number '{build_number}': {str(e)}"
     

    @staticmethod     
    def get_build_result(build_info: dict) -> str:
        """
        Get the result of a build based on the provided build information.

        :param build_info: A dictionary containing build information.
        :return: A string indicating the result of the build.
        """
        return build_info['result']
                

    @staticmethod
    def is_build_in_progress(build_info: dict) -> bool:
        """
        Check if the build is in progress based on the provided build information.

        :param build_info: A dictionary containing build information.
        :return: True if the build is in progress, False otherwise.
        """
        return build_info['building']
    

    @staticmethod
    def get_build_status(build_info:dict) -> str:
        """
        the status of a build based on the provided build information.

        :return: a string indicating the status of a build.
        """
        if JenkinsBuildInfoRetriever.is_build_in_progress(build_info):
            return "Build in progress"
        else:
            result = build_info['result']
            if result:
                return f"Build {result}"
            else:
                return "Build status unavailable"


    @staticmethod
    def get_build_timestamp(build_info:dict) -> str:
        """
        :return: a string representation of the build timestamp in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        timestamp = build_info['timestamp']
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp / 1000))
    

    @staticmethod
    def get_execution_time(build_info:dict) -> str:
        """
        the execution time in seconds as a string.    
        Important: Make sure to call this function after the build has finished.

        :return: a string that represents the execution time in seconds.
        """
        duration = build_info['duration']
        execution_time_seconds = duration / 1000
        return f"{execution_time_seconds} seconds"