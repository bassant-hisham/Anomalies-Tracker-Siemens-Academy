# Import libraries
from abc import ABC, abstractmethod
import jenkins
import logging


# Import modules
import xml_handler
import json_handler
import script_handler


# Functions
def get_type_of_solution(json_object: dict) -> str:
    """
    Get type of solution
    :param json_object:       jobs dictionary with all jobs
    """
    try:
        for key in json_object.keys():
            return key
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return ""


def create_jobs(json_object: dict, server: jenkins.Jenkins) -> None:
    solution_type = get_type_of_solution(json_object)
    solution = SolutionHandlerFactory.create_solution_handler(solution_type)
    if solution is not None:
        job_ids = solution.generate_all_pipeline_job_xml(json_object)
        for job_id in job_ids:
            with open(f"job{job_id}.xml") as xmlFile:
                config = xmlFile.read()
                server.upsert_job(f"job{job_id}", config)


def initialize_jenkins_server(url: str, username: str, password: str) -> jenkins.Jenkins:
    """
    Initialize Jenkins server with the provided URL, username, and password.
    
    :param url: Jenkins server URL
    :param username: Jenkins username
    :param password: Jenkins password
    :return: Jenkins server instance
    """
    try:
        server = jenkins.Jenkins(url, username=username, password=password)
        # Check if the server is accessible by making a small request
        print(server.get_whoami())
        return server
    except Exception as e:
        logging.error(f"Failed to initialize Jenkins server. Error: {e}")


#####################################################################################################################################################
# Classes

class SolutionHandler(ABC):

    @staticmethod
    def get_prerequisites(job: dict) -> tuple:
        """
        Get prerequisites of the job
        :param job:      dictionary job
        """
        previous_task_id = job["prerequisites"]["previous_task_id"]
        previous_job_id = job["prerequisites"]["previous_job_id"]
        return previous_task_id, previous_job_id

    @abstractmethod
    def generate_script(self, job: dict) -> str:
        """
        Generate pipeline script for given job
        :param job:      dictionary job
        """

    @abstractmethod
    def generate_all_pipeline_job_xml(self, json_object: dict) -> list:
        """
        Generate xml config files for all jobs in given json file
        :param json_object:       jobs dictionary with all jobs
        """


class SolutionHandlerFactory:
    @staticmethod
    def create_solution_handler(solution_type: str) -> SolutionHandler:
        if solution_type == "Ethernet":
            return EthernetHandler()
        elif solution_type == "5G":
            # Add 5G solution handler implementation
            return None
        else:
            raise ValueError(f"Unsupported solution type: {solution_type}")


class EthernetHandler(SolutionHandler):

    def __int__(self):
        pass

    @staticmethod
    def get_compilation_configurations(job: dict, script: str) -> str:
        """"
        Get compilation configurations of the job
        :param job:       details about the job in dictionary format
        :param script:    groovy script to be filled
        """
        try:
            compilation_configurations = job["compilation_configurations"]
            compile_design = compilation_configurations["compile_design"]
            source_design_path = compilation_configurations["source_design_path"]
            output_directory = compilation_configurations["output_directory"]
            machine = compilation_configurations["machine"]
            force = compilation_configurations["force"]
            timeout = compilation_configurations["timeout"]
            compiling_command = "sh 'g++ -g  /home/vmarwan/Documents/JB/script.c++ -o /home/vmarwan/Documents/JB/script.out'"
            if compile_design:
                script += script_handler.start_stage("Compiling")
                script += script_handler.write_step(f"echo 'compile_design: {compile_design}'")
                script += script_handler.write_step(f"echo 'source_design_path: {source_design_path}'")
                script += script_handler.write_step(f"echo 'output_directory: {output_directory}'")
                script += script_handler.write_step(f"echo 'machine: {machine}'")
                script += script_handler.write_step(f"echo 'force: {force}'")
                script += script_handler.write_step(f"echo 'timeout: {timeout}'")
                script += script_handler.write_step(compiling_command)
                script += script_handler.end_stage()
            return script
        except Exception as e:
            logging.error(f"Error while getting compilation configurations: {e}")
            return ""

    @staticmethod
    def get_basic_launch_configuration(launching_configurations: dict, script: str) -> str:
        """"
       Get basic launch configurations of the job
       :param launching_configurations:       details about the job launching configuration in dictionary format
       :param script:                         groovy script to be filled
       """
        try:
            schema = launching_configurations["$schema"]
            platform = launching_configurations["platform"]
            solution = launching_configurations["solution"]
            src_file = launching_configurations["src_file"]
            script += script_handler.start_stage("Launching")
            script += script_handler.write_step(f"echo 'schema: {schema}'")
            script += script_handler.write_step(f"echo 'platform: {platform}'")
            script += script_handler.write_step(f"echo 'solution: {solution}'")
            script += script_handler.write_step(f"echo 'src_file: {src_file}'")
            return script
        except Exception as e:
            logging.error(f"Error while getting basic launch configuration: {e}")
            return ""

    @staticmethod
    def get_dut_configurations(dut_configuration: dict, script: str) -> str:
        """
        Get dut configurations of the launching stage
        :param dut_configuration:             design under test configuration details in dictionary format
        :param script:                        groovy script to be filled
        """
        try:
            launch_dpi = dut_configuration["launch_dpi"]
            # terminate_dpi = dut_configuration["terminate_dpi"]
            # terminate_dpi_onerror = dut_configuration["terminate_dpi_onerror"]
            avb_list = dut_configuration["avb_list"]
            design_path = dut_configuration["design_path"]
            # dpi_launch_mode = dut_configuration["dpi_launch_mode"]
            dpi_launch_type = dut_configuration["dpi_launch_type"]
            # dpi_additional_args = dut_configuration["dpi_additional_args"]
            # ENABLE_BACKUP_LOG = dut_configuration["dpi_additional_env_variables"]["ENABLE_BACKUP_LOG"]
            # use_custom_comodels_config = dut_configuration["use_custom_comodels_config"]
            host_name = dut_configuration["custom_comodels_config"][0]["host_name"]
            domain_id = dut_configuration["custom_comodels_config"][0]["domain_id"]
            script += script_handler.write_step(f"echo '#####################DUT CONFIG#####################'")
            script += script_handler.write_step(f"echo 'launch_dpi: {launch_dpi}'")
            script += script_handler.write_step(f"echo 'avb_list: {avb_list}'")
            script += script_handler.write_step(f"echo 'design_path: {design_path}'")
            script += script_handler.write_step(f"echo 'dpi_launch_type: {dpi_launch_type}'")
            script += script_handler.write_step(f"echo 'host_name: {host_name}'")
            script += script_handler.write_step(f"echo 'domain_id: {domain_id}'")
            return script
        except Exception as e:
            logging.error(f"Error while getting dut configurations: {e}")
            return ""

    @staticmethod
    def get_record_configurations(record_replay_configurations: dict, script: str) -> str:
        """
        Get record configurations of launch stage
        :param record_replay_configurations:             configuration details of record and replay
        :param script:                                   groovy script to be filled
        """
        try:
            record_configurations = record_replay_configurations["record_configurations"]
            record_dir = record_configurations["record_dir"]
            config_type = record_configurations["snapshots_number"]["config_type"]
            config_value = record_configurations["snapshots_number"]["config_value"]
            script += script_handler.write_step(f"echo '#####################Record Config#####################'")
            script += script_handler.write_step(f"echo 'record_dir: {record_dir}'")
            script += script_handler.write_step(f"echo 'config_type: {config_type}'")
            script += script_handler.write_step(f"echo 'config_value: {config_value}'")
            return script
        except Exception as e:
            logging.error(f"Error while getting record configurations: {e}")
            return ""

    @staticmethod
    def get_replay_configurations(record_replay_configurations: dict, script: str) -> str:
        """
        Get replay configurations of launch stage
        :param record_replay_configurations:             configuration details of record and replay
        :param script:                                   groovy script to be filled
        """
        try:
            record_configurations = record_replay_configurations["replay_configurations"]
            replay_dir = record_configurations["replay_dir"]
            replay_snapshot_name = record_configurations["replay_snapshot_name"]
            script += script_handler.write_step("echo '#####################Replay Config#####################'")
            script += script_handler.write_step(f"echo 'replay_dir: {replay_dir}'")
            script += script_handler.write_step(f"echo 'replay_snapshot_name: {replay_snapshot_name}'")
            return script
        except Exception as e:
            logging.error(f"Error while getting replay configurations: {e}")
            return ""

    @staticmethod
    def get_master_tool_configuration(tools_configuration: dict, script: str) -> str:
        """
        Get master tool configurations
        :param tools_configuration:             configuration details of the tools
        :param script:                          groovy script to be filled
        """
        try:
            master_tool_configuration = tools_configuration["master_tool_configuration"]
            tool_name = master_tool_configuration["tool_name"]
            master_tool_launch_mode = master_tool_configuration["tool_launch_mode"]
            master_additional_args = master_tool_configuration["additional_args"]
            master_terminate_tool = master_tool_configuration["terminate_tool"]
            master_terminate_tool_onerror = master_tool_configuration["terminate_tool_onerror"]
            master_tool_additional_env_variables = master_tool_configuration["tool_additional_env_variables"]
            VE_ENABLE_BUFFERS_STATISTICS = master_tool_additional_env_variables["VE_ENABLE_BUFFERS_STATISTICS"]
            ENABLE_BACKUP_LOG = master_tool_additional_env_variables["VE_ENABLE_BUFFERS_STATISTICS"]
            script += script_handler.write_step(f"echo '#####################Master Tool#####################'")
            script += script_handler.write_step(f"echo 'tool_name: {tool_name}'")
            script += script_handler.write_step(f"echo 'master_tool_launch_mode: {master_tool_launch_mode}'")
            script += script_handler.write_step(f"echo 'master_additional_args: {master_additional_args}'")
            script += script_handler.write_step(f"echo 'master_terminate_tool: {master_terminate_tool}'")
            script += script_handler.write_step(f"echo 'master_terminate_tool_onerror: {master_terminate_tool_onerror}'")
            script += script_handler.write_step(f"echo 'VE_ENABLE_BUFFERS_STATISTICS: {VE_ENABLE_BUFFERS_STATISTICS}'")
            script += script_handler.write_step(f"echo 'ENABLE_BACKUP_LOG: {ENABLE_BACKUP_LOG}'")
            return script
        except Exception as e:
            logging.error(f"Error while getting master tool configuration: {e}")
            return ""

    @staticmethod
    def get_slave_tool_configuration(tools_configuration: dict, script: str) -> str:
        """
        Get slave tool configurations
        :param tools_configuration:             configuration details of the tools
        :param script:                          groovy script to be filled
        """
        try:
            slave_tool_configuration = tools_configuration["slave_tool_configuration"]
            launch_behavior = slave_tool_configuration["launch_behavior"]
            slave_tool_launch_mode = slave_tool_configuration["tool_launch_mode"]
            slave_additional_args = slave_tool_configuration["additional_args"]
            slave_terminate_tool = slave_tool_configuration["terminate_tool"]
            slave_terminate_tool_onerror = slave_tool_configuration["terminate_tool_onerror"]
            slave_tool_additional_env_variables = slave_tool_configuration["tool_additional_env_variables"]
            script += script_handler.write_step(f"echo '#####################Slave Tool#####################'")
            script += script_handler.write_step(f"echo 'launch_behavior: {launch_behavior}'")
            script += script_handler.write_step(f"echo 'slave_tool_launch_mode: {slave_tool_launch_mode}'")
            script += script_handler.write_step(f"echo 'slave_additional_args: {slave_additional_args}'")
            script += script_handler.write_step(f"echo 'slave_terminate_tool: {slave_terminate_tool}'")
            script += script_handler.write_step(f"echo 'slave_terminate_tool_onerror: {slave_terminate_tool_onerror}'")
            script += script_handler.write_step(f"echo 'slave_tool_additional_env_variables: {slave_tool_additional_env_variables}'")
            return script
        except Exception as e:
            logging.error(f"Error while getting slave tool configuration: {e}")
            return ""

    def get_launching_configurations(self, job: dict, script: str) -> str:
        """
         Get launching configurations of the job
        :param job:                             dictionary job
        :param script:                          groovy script to be filled
        """
        try:
            launching_configurations = job["launching_configurations"]
            dut_configuration = launching_configurations["dut_configuration"][0]
            launch_dpi = dut_configuration["launch_dpi"]
            if launch_dpi:
                script = self.get_basic_launch_configuration(launching_configurations, script)
                script = self.get_dut_configurations(dut_configuration, script)
                record_replay_configurations = dut_configuration["record_replay_configurations"]
                script = self.get_record_configurations(record_replay_configurations, script)
                script = self.get_replay_configurations(record_replay_configurations, script)
                tools_configuration = launching_configurations["tools_configuration"]
                launch_tool = tools_configuration["launch_tool"]
                if launch_tool:
                    script = self.get_master_tool_configuration(tools_configuration, script)
                    script = self.get_slave_tool_configuration(tools_configuration, script)
                script += script_handler.end_stage()
            return script
        except Exception as e:
            logging.error(f"Error while getting launching configurations: {e}")
            return ""

    @staticmethod
    def get_running_configurations(job: dict, script: str) -> str:
        """
        Get running configurations of the job
        :param job:                             dictionary job
        :param script:                          groovy script to be filled
        """
        try:
            run_script = job["running_configurations"]["run_script"]
            error_type = job["running_configurations"]["error_type"]
            crashed_process = job["running_configurations"]["crash_configurations"]["crashed_process"]
            attach_gdb = job["running_configurations"]["crash_configurations"]["attach_gdb"]
            script_path = job["running_configurations"]["script_path"]
            running_command = "sh '/home/vmarwan/Documents/JB/script.out'"
            running_command_with_gdb = "sh 'sudo gdb -ex=r --args /home/vmarwan/Documents/JB/script.out'"
            if run_script:
                script += script_handler.start_stage("Running")
                script += script_handler.write_step(f"echo 'run_script: {run_script}'")
                script += script_handler.write_step(f"echo 'error_type: {error_type}'")
                script += script_handler.write_step(f"echo 'crashed_process: {crashed_process}'")
                script += script_handler.write_step(f"echo 'attach_gdb: {attach_gdb}'")
                script += script_handler.write_step(f"echo 'script_path: {script_path}'")
                if attach_gdb:
                    script += script_handler.write_step("echo '#####################Run With GDB#####################'")
                    script += script_handler.write_step(running_command_with_gdb)
                else:
                    script += script_handler.write_step("echo '#####################Run Without GDB#####################'")
                    script += script_handler.write_step(running_command)
                script += script_handler.end_stage()
            return script
        except Exception as e:
            logging.error(f"Error while getting running configurations: {e}")
            return ""

    def generate_script(self, job: dict) -> str:
        try:
            script = script_handler.start_script()
            script = self.get_compilation_configurations(job, script)
            script = self.get_launching_configurations(job, script)
            script = self.get_running_configurations(job, script)
            script += script_handler.end_script()
            return script
        except Exception as e:
            logging.error(f"Error while generating script: {e}")
            return ""

    def generate_all_pipeline_job_xml(self, json_object: dict) -> list:
        try:
            job_ids = []
            task = list(json_object["Ethernet"].keys())[0]
            jobs = json_object["Ethernet"][task]["jobs"]
            for job_num, job in jobs.items():
                job_ids.append(job_num)
                previous_task_id, previous_job_id = self.get_prerequisites(job)
                script_text = self.generate_script(job)
                xml_handler.generate_pipeline_job_xml(script_text, job_num, projects_to_watch=[f"job{previous_job_id}"])
            logging.info("XML configuration files generated successfully.")
            return job_ids
        except Exception as e:
            logging.error(f"Error while generating pipeline jobs: {e}")
            return []


#####################################################################################################################################################
# Main
def main():
    server = initialize_jenkins_server('http://localhost:8080', username="marwansallam88", password="1738")
    from_front_end = "front_end.json"
    json_object = json_handler.handle_data_from_front_end(from_front_end)
    create_jobs(json_object, server)


if __name__ == "__main__":
    main()
