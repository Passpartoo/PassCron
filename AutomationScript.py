import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import schedule
import time
import subprocess
from multiprocessing import Process
import shutil

class AutomationScript(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.running = False
        self.process = None

    def create_widgets(self):
        self.files_var = {}
        self.files = os.listdir("./src")
        for file in self.files:
            self.files_var[file] = tk.BooleanVar()
            ttk.Checkbutton(self, text=file, variable=self.files_var[file]).pack()

        self.upload_button = ttk.Button(self)
        self.upload_button["text"] = "Télécharger des scripts"
        self.upload_button["command"] = self.upload_scripts
        self.upload_button.pack(side=tk.BOTTOM)

        self.next_button = ttk.Button(self)
        self.next_button["text"] = "Suivant"
        self.next_button["command"] = self.print_selected_files
        self.next_button.pack(side=tk.BOTTOM)

    def print_selected_files(self):
        self.listeScript = [file for file in self.files if self.files_var[file].get()]
        messagebox.showinfo("Information", "Développement en cours")

    def upload_scripts(self):
        filepaths = filedialog.askopenfilenames(filetypes=[("Scripts", "*.sh *.bash *.ps1")])
        for filepath in filepaths:
            filename = os.path.basename(filepath)
            shutil.copy(filepath, "./src/" + filename)  # Copie le fichier
            self.files.append(filename)
            self.files_var[filename] = tk.BooleanVar()
            ttk.Checkbutton(self, text=filename, variable=self.files_var[filename]).pack()

    def cron(self, interval, unit):
        self.running = True
        schedule.every(interval).__dict__[unit].do(self.execute_scripts)
        self.process = Process(target=self.run_pending_tasks)
        self.process.start()

    def execute_scripts(self):
        for script in self.listeScript:
            extension = os.path.splitext(script)[1]
            if extension == ".sh":
                subprocess.run(["bash", "./src/" + script], check=True)
            elif extension == ".bash":
                subprocess.run(["bash", "./src/" + script], check=True)
            elif extension == ".ps1":
                subprocess.run(["powershell", "-File", "./src/" + script], check=True)
            else:
                print(f"Extension de script non prise en charge : {extension}")

    def run_pending_tasks(self):
        while self.running:
            schedule.run_pending()
            time.sleep(1)

    def stop_task(self):
        self.running = False

    def restart_task(self):
        self.running = True

    def kill_task(self):
        if self.process is not None:
            try:
                self.process.terminate()
            except Exception as e:
                print(f"Erreur lors de l'arrêt du processus : {str(e)}")
            finally:
                self.process = None

    def list_task(self):
        return [(task, self.running) for task in schedule.jobs]

    def clear(self):
        self.kill_task()
        schedule.clear()
