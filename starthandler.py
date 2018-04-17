import threading
import os

from . import constants

class StartHandler():
	project_runner = None

	def __init__(self, project_runner):
		self.project_runner = project_runner
		self.project_runner.window.show_quick_panel(["Perform Project Startup", "Cancel"], self.on_start_response)

	def get_run_path(self):
		project_file_dir = os.path.dirname(self.project_runner.project_file)

		if "path" in self.project_runner.project_data and self.project_runner.project_data['path'] != ".":
			return os.path.join(project_file_dir, self.project_runner.project_data['path'])
		else:
			return project_file_dir

	def on_start_response(self, response):
		if response == constants.RESPONSE_YES:
			self.project_runner.run_thread = threading.Thread(target=self.start)
			self.project_runner.run_thread.daemon = True # Don't auto-terminate on close
			self.project_runner.run_thread.start()

	def start(self):
		cmd = ""

		# "start" can be set to a non-string, in which case we'll assume they want "npm start"
		if self.project_runner.project_data['start'] is str:
			cmd = self.project_runner.project_data['start']
		else:
			cmd = constants.DEFAULT_STARTUP

		os.chdir(self.get_run_path());
		self.project_runner.terminal = os.system("npm start");