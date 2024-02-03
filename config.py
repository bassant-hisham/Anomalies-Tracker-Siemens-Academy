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
    JOB_CREATED = ('rgb(33, 188, 180)', 'Job Created')
    JOB_IN_BATCH = ('lightgreen', 'Job In Batch')
    JOB_STARTED = ('orange', 'Job Started')
    JOB_CRASHED = ('lightyellow', 'Job Crashed in Jenkins')
    CHILD_JOB_FAILED = ('red', 'Dependency Failed')
    def __init__(self, color, description):
        self.color = color
        self.description = description


class JenkinsConfig:
    JENKINS_URL = "http://localhost:8080/"
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