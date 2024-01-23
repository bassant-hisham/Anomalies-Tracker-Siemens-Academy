import threading
import logging
import os



from src.Jenkins_APIs import Jenkins

log_folder = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_folder, exist_ok=True)

log_file = os.path.join(log_folder, 'info.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

logger = logging.getLogger(__name__)



from tkinter import Tk, Label, Button, Entry, filedialog, simpledialog

class JenkinsTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jenkins Automation")
        
        self.label = Label(root, text="Enter JSON File Path:")
        self.label.pack(pady=10)

        self.path_entry = Entry(root, width=50)
        self.path_entry.pack(pady=10)

        self.browse_button = Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.start_button = Button(root, text="Start Jenkins Jobs", command=self.start_jenkins_jobs)
        self.start_button.pack(pady=10)

        self.stop_button = Button(root, text="Stop Jenkins Job", command=self.stop_jenkins_job)
        self.stop_button.pack(pady=10)

        self.delete_button = Button(root, text="Delete Jenkins Job", command=self.delete_jenkins_job)
        self.delete_button.pack(pady=10)

        self.output_button = Button(root, text="Get Job Output", command=self.get_job_output)
        self.output_button.pack(pady=10)

        self.info_button = Button(root, text="Get Job Info", command=self.get_job_info)
        self.info_button.pack(pady=10)

        self.status_button = Button(root, text="Get Build Status", command=self.get_build_status)
        self.status_button.pack(pady=10)

        self.commit_button = Button(root, text="Get Commit Hash", command=self.get_job_commit_hash)
        self.commit_button.pack(pady=10)

        self.time_button = Button(root, text="Get Build Time", command=self.get_job_build_time)
        self.time_button.pack(pady=10)

        self.jenkins_instance = Jenkins()

    def browse_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select JSON File", filetypes=[("JSON files", "*.json")])
        self.path_entry.delete(0, 'end')
        self.path_entry.insert(0, file_path)

    def start_jenkins_jobs(self):
        json_path = self.path_entry.get()
        if json_path:
            thread = threading.Thread(target=self.jenkins_instance.start_jobs_in_batches, args=(json_path,))
            thread.start()
        else:
            print("Please select a JSON file.")

    def stop_jenkins_job(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.stop_job(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def delete_jenkins_job(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.delete_job(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def get_job_output(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.get_job_output(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def get_job_info(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.get_job_info(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def get_build_status(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.get_build_status(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def get_job_commit_hash(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.get_job_commit_hash(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def get_job_build_time(self):
        job_name = self.get_user_input("Enter Jenkins Job Name:")
        if job_name:
            self.jenkins_instance.get_job_build_time(job_name)
        else:
            print("Please enter a Jenkins job name.")

    def get_user_input(self, prompt):
        user_input = simpledialog.askstring("User Input", prompt)
        return user_input

def main():
    root = Tk()
    app = JenkinsTkinterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
