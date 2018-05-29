import threading
import os
import subprocess
import sublime

from . import constants

class StartHandler():
	start_cmd = None
	run_thread = None
	terminal = None

	def __init__(self, start_cmd, start_path, project_file):
		self.start_cmd = self.calculate_start_cmd(start_cmd)
		self.start_path = self.calculate_start_path(start_path, project_file)

		response = sublime.ok_cancel_dialog("ProjectRunner auto startup:\n\n" + self.start_cmd)
		self.on_start_response(response)

	def calculate_start_path(self, start_path, project_file):
		project_file_dir = os.path.dirname(project_file)

		if start_path is not None and start_path != ".":
			return os.path.join(project_file_dir, start_path)
		else:
			return project_file_dir

	# "start" can be set to a non-string, in which case we'll assume they want "npm start"
	def calculate_start_cmd(self, cmd):
		if isinstance(cmd, str):
			return cmd
		else:
			return constants.DEFAULT_STARTUP

	def on_start_response(self, yes):
		if yes:
			self.run_thread = threading.Thread(target=self.start)
			self.run_thread.daemon = True # Don't auto-terminate on close
			self.run_thread.start()

	def start(self):
		print("Start, path = " + self.start_path)
		#os.chdir(self.start_path);
		#self.terminal = os.system(self.start_cmd);
		#self.terminal = subprocess.Popen("cmd.exe /K " + self.start_cmd, shell=True, cwd=self.start_path)
		self.terminal = subprocess.call(self.start_cmd)

	def stop(self):
		if self.terminal is not None:
			print("stop")
			#subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid = self.terminal.pid))
			self.terminal = None