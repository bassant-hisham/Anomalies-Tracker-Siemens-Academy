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


# class JenkinsConfig:
#     JENKINS_URL = "http://localhost:8080/"
#     JENKINS_USERNAME = "admin"
#     JENKINS_PASSWORD = "11f6ffd591aa58166016b94c900f0c361d"