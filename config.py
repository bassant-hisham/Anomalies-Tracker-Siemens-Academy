from enum import Enum
import logging
import os


DEBUG_MODE = True

DELETE_JOB_AFTER_FINISH = False



if DEBUG_MODE:
    ENABLE_LOGGER = True   
    DUMP_CONSOLE_OUTPUT = True
    WAIT_TIMEOUT = 50
else:
    ENABLE_LOGGER = False
    DUMP_CONSOLE_OUTPUT = False
    WAIT_TIMEOUT = 30

class BuildState(Enum):
    SUCCESS = ('green', 'SUCCESS')
    FAILURE = ('red', 'FAILURE')
    JOB_CREATED = ('rgb(33, 188, 180)', 'Job Created')
    JOB_IN_BATCH = ('lightgreen', 'Job In Batch')
    JOB_STARTED = ('orange', 'Job Started')
    JOB_CRASHED = ('lightyellow', 'Job Crashed in Jenkins')
    BINARY_SEARCH    = ('rgb(33, 188, 180)', 'BINARY SEARCH MODE')
    CHILD_JOB_FAILED = ('red', 'Dependency Failed')
    FIRST_FAILURE   = ('red', 'FIRST FAILURE')
    def __init__(self, color, description):
        self.color = color
        self.description = description
    
    @classmethod
    def get_color_by_description(cls, description):
        for status in cls:
            if status.description == description:
                return status.color
        return None
    


class JenkinsConfig:
    JENKINS_URL = "http://localhost:9090/"
    JENKINS_USERNAME = "AhmedSh"
    JENKINS_PASSWORD = "#myjenkinsacc#"



if ENABLE_LOGGER:
    log_folder = os.path.join(os.path.dirname(__file__),'generated', 'logs')
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, 'info.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )

    logger = logging.getLogger(__name__)