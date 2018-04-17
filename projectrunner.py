import sublime
import sublime_plugin
import subprocess
import os
import threading

RESPONSE_YES = 0
RESPONSE_NO = 1

DEFAULT_STARTUP = "npm start"

class ProjectRunner(sublime_plugin.EventListener):
	terminal = None
	project_file = None
	project_data = None
	window = None
	view = None
	run_thread = None

	def on_activated(self, view):
		win = view.window()

		if win is not None:
			project_file = win.project_file_name()
			
			if project_file is not None:
				self.project_data = win.project_data()

				if "projectrunner" in self.project_data and project_file != self.project_file:
					self.project_file = project_file
					self.window = win
					self.view = view
					self.process_project_data()

	def process_project_data(self):
		if "start" in self.project_data['projectrunner'] and self.project_data['projectrunner']['start'] != False:
			self.window.show_quick_panel(["Perform project startup", "Cancel"], self.on_start_response)

	def get_run_path(self):
		return os.path.dirname(self.project_file)

	def on_start_response(self, response):
		if response == RESPONSE_YES:
			self.run_thread = threading.Thread(target=self.start)
			self.run_thread.daemon = True # Don't auto-terminate on close
			self.run_thread.start()

	def start(self):
		cmd = ""

		# "start" can be set to a non-string, in which case we'll assume they want "npm start"
		if self.project_data['projectrunner']['start'] is str:
			cmd = self.project_data['projectrunner']['start']
		else:
			cmd = DEFAULT_STARTUP

		os.chdir(self.get_run_path());
		self.terminal = os.system("npm start");