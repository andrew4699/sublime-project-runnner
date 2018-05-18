from .starthandler import StartHandler

class WindowManager():
	window = None

	project_file = None
	project_data = None

	start_handler = None

	def __init__(self, window):
		self.window = window
		pass

	def on_load(self):
		project_file = self.window.project_file_name()
			
		if project_file is not None:
			#print("on_load: " + project_file)
			#print("old: " + (self.project_file or ""))

			if project_file != self.project_file:
				self.project_file = project_file
				project_data = self.window.project_data()
				#print("switched project - " + project_file
				#if self.project_file is not None: # Clean up last project
				#	self.stop()

				if "projectrunner" in project_data:
					print(">> ProjectRunner settings detected")
					self.project_data = project_data['projectrunner']
					self.start()

	def start(self):
		if "start" in self.project_data and self.project_data['start'] != False:
			self.start_handler = StartHandler(self.project_data['start'], self.project_data['path'] or None, self.project_file)

	# tbd
	def stop(self):
		if True and self.start_handler is not None:
			self.start_handler.stop()