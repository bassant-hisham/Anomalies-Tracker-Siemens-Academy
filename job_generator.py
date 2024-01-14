from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from xml.dom import minidom
from getpass import getpass
from enum import Enum
import jenkins
import logging
import json


class ConcurrentBuilds(Enum):
    enable = 0
    disable = 1
    disable_and_abort_previous = 2


class PipelineSpeed(Enum):
    NONE = 'None'
    PERFORMANCE_OPTIMIZED = 'PERFORMANCE_OPTIMIZED'
    SURVIVABLE_NONATOMIC = 'SURVIVABLE_NONATOMIC'
    MAX_SURVIVABILITY = 'MAX_SURVIVABILITY'


class TimePeriod(Enum):
    Second = 'second'
    Minute = 'minute'
    Hour = 'hour'
    Day = 'day'
    Week = 'week'
    Month = 'month'
    Year = 'year'


class BuildAfter(Enum):
    NONE = 'None'
    stable = ["SUCCESS", "0", "BLUE", "true"]
    unstable = ["UNSTABLE", "1", "YELLOW", "true"]
    fails = ["FAILURE", "2", "RED", "true"]
    always = ["ABORTED", "3", "ABORTED", "false"]


def prettify(elem: ET.Element) -> str:
    """
    Return a pretty-printed XML string for the Element
    :param elem:     root element of xml
    """
    try:
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    except Exception as e:
        logging.error(f"Error while prettifying XML: {e}")


def get_type(json_file: str) -> str:
    """
    Get type of solution from json file
    :param json_file:       full/relevant path of json file
    """
    try:
        with open(json_file) as jf:
            json_object = json.load(jf)
            for key in json_object.keys():
                return key
    except FileNotFoundError:
        logging.error(f"JSON file '{json_file}' not found.")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file '{json_file}'. Check JSON syntax.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


class Solution(ABC):

    @abstractmethod
    def generate_script(self, job: dict) -> str:
        """
        Generate pipeline script for given job
        :param job:      dictionary job extracted from json file
        """

    def generate_pipeline_job_xml(self, job: dict, job_num: str, description: str = "", display_name: str = "",
                                  keep_dependencies: bool = False, days_to_keep_builds: int = -1, max_builds_to_keep: int = -1,
                                  days_to_keep_artifacts: int = -1, max_builds_to_keep_with_artifacts: int = -1,
                                  disable_concurrent_builds: ConcurrentBuilds = ConcurrentBuilds.enable, disable_resume: bool = False,
                                  github_project_url: str = "", github_project_display_name: str = "",
                                  pipeline_speed: PipelineSpeed = PipelineSpeed.NONE, preserve_stashes: int = -1,
                                  throttle_builds: int = -1, time_period: TimePeriod = TimePeriod.Hour, user_boost: bool = False,
                                  build_after_type: BuildAfter = BuildAfter.NONE, projects_to_watch: list = (),
                                  github_hook_trigger: bool = False, sandbox_enabled: bool = True, quiet_period: int = -1,
                                  build_remotely_auth_token: str = "", disable: bool = False) -> None:
        """
        Generate xml config files for given job with specific actions
        :param job:                                 job details which is usually retrieved from a json file.
        :param job_num:                             job name which is usually indicated by a number.
        :param description:                         description about the job.
        :param display_name:                        optional display name shown for the project throughout the Jenkins web GUI.
        :param keep_dependencies:                   unclear; preferably keep as default.
        :param days_to_keep_builds:                 build records are only kept up to this number of days.
        :param max_builds_to_keep:                  only up to this number of build records are kept.
        :param days_to_keep_artifacts:              artifacts from builds older than this number of days will be deleted, but the logs, history, reports, etc for the build will be kept.
        :param max_builds_to_keep_with_artifacts:   only up to this number of builds have their artifacts retained.
        :param disable_concurrent_builds:           do not allow concurrent builds.
        :param disable_resume:                      do not allow the pipeline to resume if the controller restarts.
        :param github_project_url:                  url for the GitHub hosted project (without the tree/master or tree/branch part).
        :param github_project_display_name:         value will be used as context name for commit status if status builder or status publisher is defined for this project.
        :param pipeline_speed:                      this setting allows users to change the default durability mode for running Pipelines. In most cases this is a trade-off between performance and the ability for running pipelines to resume after unplanned Jenkins outages.
        :param preserve_stashes:                    keep this many of the most recent builds' stashes.
        :param throttle_builds:                     the maximum number of builds allowed within the specified time period.
        :param time_period:                         The time period within which the maximum number of builds will be enforced.
        :param user_boost:                          enable this option to permit user triggered builds to skip the rate limit.
        :param build_after_type:                    specify the condition on which the project being watched is done with to trigger a build for this job.
        :param projects_to_watch:                   when some other projects finish building, a new build is scheduled for this project.
        :param github_hook_trigger:                 GitHub Plugin triggers a one-time polling on GITScm if hook came from a GitHub repository which matches the Git repository defined in SCM/Git section of this job.
        :param sandbox_enabled:                     run Groovy script in a sandbox with limited abilities.
        :param quiet_period:                        jenkins will wait for the specified period of time (in seconds) before actually starting the build.
        :param build_remotely_auth_token:           an authentication token used if you would like to trigger new builds by accessing a special predefined URL (convenient for scripts).
        :param disable:                             disable the job.
        """
        try:
            root = ET.Element('flow-definition', attrib={'plugin': 'workflow-job@1385.vb_58b_86ea_fff1'})

            actions = ET.SubElement(root, 'actions')

            if description != "":
                describe = ET.SubElement(root, 'description')
                describe.text = description

            if display_name != "":
                displayName = ET.SubElement(root, 'displayName')
                displayName.text = display_name

            declarative_job_action = ET.SubElement(actions, 'org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobAction',
                                                   attrib={'plugin': 'pipeline-model-definition@2.2151.ve32c9d209a_3f'})
            declarative_job_property_tracker_action = ET.SubElement(actions,
                                                                    'org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction',
                                                                    attrib={'plugin': 'pipeline-model-definition@2.2151.ve32c9d209a_3f'})
            job_properties = ET.SubElement(declarative_job_property_tracker_action, 'jobProperties')
            triggers = ET.SubElement(declarative_job_property_tracker_action, 'triggers')
            parameters = ET.SubElement(declarative_job_property_tracker_action, 'parameters')
            options = ET.SubElement(declarative_job_property_tracker_action, 'options')
            declarative_job_property_tracker = ET.SubElement(declarative_job_property_tracker_action,
                                                             'org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction')
            description = ET.SubElement(root, 'description')

            keepDependencies = ET.SubElement(root, 'keepDependencies')
            if keep_dependencies:
                keepDependencies.text = 'true'
            else:
                keepDependencies.text = 'false'

            properties = ET.SubElement(root, 'properties')

            if days_to_keep_builds > 0 or max_builds_to_keep > 0 or days_to_keep_artifacts > 0 or max_builds_to_keep_with_artifacts > 0:
                discard_build = ET.SubElement(properties, 'jenkins.model.BuildDiscarderProperty')
                strategy = ET.SubElement(discard_build, 'strategy class="hudson.tasks.LogRotator', attrib={'class': 'hudson.tasks.LogRotator'})
                daysToKeep = ET.SubElement(strategy, 'daysToKeep')
                daysToKeep.text = str(days_to_keep_builds)
                numToKeep = ET.SubElement(strategy, 'numToKeep')
                numToKeep.text = str(max_builds_to_keep)
                artifactDaysToKeep = ET.SubElement(strategy, 'artifactDaysToKeep')
                artifactDaysToKeep.text = str(days_to_keep_artifacts)
                artifactNumToKeep = ET.SubElement(strategy, 'artifactNumToKeep')
                artifactNumToKeep.text = str(max_builds_to_keep_with_artifacts)

            if 1 <= disable_concurrent_builds.value <= 2:
                DisableConcurrentBuilds = ET.SubElement(properties, 'org.jenkinsci.plugins.workflow.job.properties.DisableConcurrentBuildsJobProperty')
                abortPrevious = ET.SubElement(DisableConcurrentBuilds, 'abortPrevious')
                if disable_concurrent_builds == ConcurrentBuilds.disable:
                    abortPrevious.text = 'false'
                else:
                    abortPrevious.text = 'true'

            if disable_resume:
                DisableResume = ET.SubElement(properties, 'org.jenkinsci.plugins.workflow.job.properties.DisableResumeJobProperty')

            if github_project_url != "":
                GithubProject = ET.SubElement(properties, 'com.coravy.hudson.plugins.github.GithubProjectProperty', attrib={'plugin': 'github@1.37.3.1'})
                projectUrl = ET.SubElement(GithubProject, 'projectUrl')
                projectUrl.text = github_project_url
                displayName = ET.SubElement(GithubProject, 'displayName')
                if github_project_display_name != "":
                    displayName.text = github_project_display_name

            if pipeline_speed != PipelineSpeed.NONE:
                DurabilityHint = ET.SubElement(properties, 'org.jenkinsci.plugins.workflow.job.properties.DurabilityHintJobProperty')
                hint = ET.SubElement(DurabilityHint, 'hint')
                hint.text = pipeline_speed.value

            if preserve_stashes >= 0:
                PreserveStashes = ET.SubElement(properties, 'org.jenkinsci.plugins.pipeline.modeldefinition.properties.PreserveStashesJobProperty',
                                                attrib={'plugin': 'pipeline-model-definition@2.2151.ve32c9d209a_3f'})
                buildCount = ET.SubElement(PreserveStashes, 'buildCount')
                buildCount.text = str(preserve_stashes)

            if throttle_builds > 0:
                RateLimit = ET.SubElement(properties, 'jenkins.branch.RateLimitBranchProperty_-JobPropertyImpl',
                                          attrib={'plugin': 'branch-api@2.1135.v8de8e7899051'})
                durationName = ET.SubElement(RateLimit, "durationName")
                durationName.text = time_period.value
                count = ET.SubElement(properties, 'count')
                count.text = throttle_builds
                userBoost = ET.SubElement(properties, 'userBoost')
                if user_boost:
                    userBoost.text = 'true'
                else:
                    userBoost.text = 'false'

            PipelineTriggers = ET.SubElement(properties, 'org.jenkinsci.plugins.workflow.job.properties.PipelineTriggersJobProperty')
            triggers = ET.SubElement(PipelineTriggers, 'triggers')

            if build_after_type != BuildAfter.NONE:
                BuildTrigger = ET.SubElement(triggers, 'jenkins.triggers.ReverseBuildTrigger')
                spec = ET.SubElement(BuildTrigger, 'spec')
                upstreamProjects = ET.SubElement(BuildTrigger, 'upstreamProjects')
                projects = ""
                if len(projects_to_watch):
                    for project in projects_to_watch:
                        projects += f"{project},"
                else:
                    pass
                upstreamProjects.text = projects
                threshold = ET.SubElement(BuildTrigger, 'threshold')
                name = ET.SubElement(threshold, 'name')
                name.text = build_after_type.value[0]
                ordinal = ET.SubElement(threshold, 'ordinal')
                ordinal.text = build_after_type.value[1]
                color = ET.SubElement(threshold, 'color')
                color.text = build_after_type.value[2]
                completeBuild = ET.SubElement(threshold, 'completeBuild')
                completeBuild.text = build_after_type.value[3]

            if github_hook_trigger:
                GitHubPushTrigger = ET.SubElement(triggers, 'com.cloudbees.jenkins.GitHubPushTrigger', attrib={'plugin': 'github@1.37.3.1'})
                spec = ET.SubElement(GitHubPushTrigger, 'spec')

            definition = ET.SubElement(root, 'definition', attrib={'class': 'org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition',
                                                                   'plugin': 'workflow-cps@3826.v3b_5707fe44da_'})

            script = ET.SubElement(definition, 'script')
            script.text = self.generate_script(job)

            sandbox = ET.SubElement(definition, 'sandbox')
            if sandbox_enabled:
                sandbox.text = 'true'
            else:
                sandbox.text = 'false'

            triggers = ET.SubElement(root, 'triggers')

            if quiet_period >= 0:
                quietPeriod = ET.SubElement(root, 'quietPeriod')
                quietPeriod.text = quiet_period

            if build_remotely_auth_token != "":
                authToken = ET.SubElement(root, 'authToken')
                authToken.text = build_remotely_auth_token

            disabled = ET.SubElement(root, 'disabled')
            if disable:
                disabled.text = 'true'
            else:
                disabled.text = 'false'

            xml_tree = ET.ElementTree(root)
            xml_string = prettify(root)
            with open(f"job{job_num}.xml", "w") as new_job:
                new_job.write(xml_string)
        except Exception as e:
            logging.error(f"Error while generating XML configuration: {e}")

    @abstractmethod
    def generate_all_pipeline_job_xml(self, json_file: str) -> None:
        """Generate xml config files for all jobs in given json file"""


class Ethernet(Solution):

    def __int__(self):
        pass

    def generate_script(self, job: dict) -> str:
        try:
            prerequisites = job["prerequisites"]["previous_job_id"]
            compiling = job["compilation_configurations"]["compile_design"]
            compile_path = job["compilation_configurations"]["source_design_path"]
            compiling_command = f"sh 'sudo g++ -g  /home/vmarwan/Documents/JB/script.c++ -o /home/vmarwan/Documents/JB/script.out'"
            launching_dut = job["launching_configurations"]["dut_configuration"][0]["launch_dpi"]
            terminating_dut = job["launching_configurations"]["dut_configuration"][0]["terminate_dpi"]
            launching_dut = []
            terminating_dut = []
            for dut_config in job["launching_configurations"]["dut_configuration"]:
                launching_dut.append(dut_config["launch_dpi"])
                terminating_dut.append(dut_config["terminate_dpi"])
            launching_tools = job["launching_configurations"]["tools_configuration"]["launch_tool"]
            terminating_master_tool = job["launching_configurations"]["tools_configuration"]["master_tool_configuration"]["terminate_tool"]
            terminating_slave_tool = job["launching_configurations"]["tools_configuration"]["slave_tool_configuration"]["terminate_tool"]
            launching_dut_command = "echo 'launching dut'"
            terminating_dut_command = "echo 'terminating dut'"
            launching_tools_command = "echo 'launching tools'"
            terminating_master_command = "echo 'terminating master'"
            terminating_slave_command = "echo 'terminating slave'"
            running = job["running_configurations"]["run_script"]
            attach_gdb = job["running_configurations"]["crash_configurations"]["attach_gdb"]
            script_path = job["running_configurations"]["script_path"]
            running_command = f"sh 'sudo /home/vmarwan/Documents/JB/script.out'"
            running_command_with_gdb = f"sh 'sudo gdb -ex=r --args /home/vmarwan/Documents/JB/script.out'"
            script = "pipeline{\n\tagent any\n\tstages{"
            if compiling:
                script += "\n\t\tstage('Compiling'){\n\t\t\tsteps{"
                script += "\n\t\t\t\techo 'compiling'"
                script += "\n\t\t\t\t" + compiling_command
                script += "\n\t\t\t}\n\t\t}"
            else:
                pass
            if True in launching_dut or launching_tools:
                script += "\n\t\tstage('Launching'){\n\t\t\tsteps{"
                for launchable in launching_dut:
                    if launchable:
                        script += "\n\t\t\t\t" + launching_dut_command
                        if terminating_dut:
                            script += "\n\t\t\t\t" + terminating_dut_command
                        else:
                            pass
                    else:
                        pass
                if launching_tools:
                    script += "\n\t\t\t\t" + launching_tools_command
                    if terminating_master_tool:
                        script += "\n\t\t\t\t" + terminating_master_command
                    else:
                        pass
                    if terminating_slave_tool:
                        script += "\n\t\t\t\t" + terminating_slave_command
                    else:
                        pass
                else:
                    pass
                script += "\n\t\t\t}\n\t\t}"
            else:
                pass
            if running:
                script += "\n\t\tstage('Running'){\n\t\t\tsteps{"
                script += "\n\t\t\t\techo 'running'"
                script += "\n\t\t\t\tscript{"
                if attach_gdb:
                    script += "\n\t\t\t\t\techo 'attaching'"
                    script += "\n\t\t\t\t\t" + running_command_with_gdb
                else:
                    script += "\n\t\t\t\t\techo 'no attaching'"
                    script += "\n\t\t\t\t\t" + running_command 
                script += "\n\t\t\t\t}\n\t\t\t}\n\t\t}"
            else:
                pass
            script += "\n\t}\n}"
            return script
        except Exception as e:
            logging.error(f"Error while generating script: {e}")

    def generate_all_pipeline_job_xml(self, json_file: str) -> None:
        try:
            with open(json_file) as jf:
                json_object = json.load(jf)
                jobs = json_object["Ethernet"]["task1"]["jobs"]
            for job_num, job in jobs.items():
                pre = job["prerequisites"]["previous_job_id"]
                self.generate_pipeline_job_xml(job, job_num, build_after_type=BuildAfter.stable, projects_to_watch=[f"job{pre}"])
            logging.info("XML configuration files generated successfully.")
        except FileNotFoundError:
            logging.error(f"JSON file '{json_file}' not found.")
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file '{json_file}'. Check JSON syntax.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")


def main():
    json_file = "front_end.json"
    solution_type = get_type(json_file)
    solution_types = {"Ethernet": Ethernet(), "5G": ""}
    solution = solution_types[solution_type]
    solution.generate_all_pipeline_job_xml(json_file)
    username = input("Input Username:  ")
    password = getpass("Input Password: ")
    server = jenkins.Jenkins('http://localhost:8080', username=username, password=password)
    for i in range(1, 4):
        with open(f"job{i}.xml") as xmlFile:
            config = xmlFile.read()
            server.upsert_job(f"job{i}", config)


if __name__ == "__main__":
    main()
