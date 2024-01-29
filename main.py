
import sys
from PyQt5 import QtWidgets
from src.frontend.CustomWidgets.mainwindow import MyMainWindow



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MyMainWindow()
    mainwindow.show()
    sys.exit(app.exec_())



# import sys
# from PyQt5 import QtWidgets
# from src.frontend.CustomWidgets.mainwindow import MyMainWindow
# import config
# import logging
# import os
# import threading

# if config.ENABLE_LOGGER:
#     log_folder = os.path.join(os.path.dirname(__file__), 'logs')
#     os.makedirs(log_folder, exist_ok=True)

#     log_file = os.path.join(log_folder, 'info.log')

#     logging.basicConfig(
#         filename=log_file,
#         level=logging.INFO,
#         format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
#     )

#     logger = logging.getLogger(__name__)




# if __name__ == "__main__":
#     thread_output = threading.Thread(target=config.Jenkins_APIs.start_jobs_in_batches,
#                                                         args=("C:/Users/moham/Desktop/Anomalies-Tracker-Siemens-Academy-main_app/Extras/resources/json/3_jobs_front_end.json",))
#     thread_output.start()