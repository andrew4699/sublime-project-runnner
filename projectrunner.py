import sublime
import sublime_plugin

from .starthandler import StartHandler

class ProjectRunner(sublime_plugin.EventListener):
	terminal = None
	project_file = None
	project_data = None
	window = None
	view = None
	run_thread = None
	start_handler = None

	def on_activated(self, view):
		win = view.window()
		
		if win is not None:
			project_file = win.project_file_name()
			
			if project_file is not None:
				project_data = win.project_data()

				if "projectrunner" in project_data and project_file != self.project_file:
					self.project_file = project_file
					self.project_data = project_data['projectrunner']
					self.window = win
					self.view = view
					self.process_project_data()

	def process_project_data(self):
		if "start" in self.project_data and self.project_data['start'] != False:
			self.start_handler = StartHandler(self)