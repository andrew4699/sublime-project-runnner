import sublime
import sublime_plugin

from .windowmanager import WindowManager

class ProjectRunner(sublime_plugin.EventListener):
	window_controllers = None

	def __init__(self):
		self.window_controllers = {}

	def on_activated(self, view):
		self.on_load(view)
		
	def on_load(self, view):
		win = view.window()

		if win is not None:
			winID = win.id()

			if winID not in self.window_controllers:
				print("New window")
				self.window_controllers[winID] = WindowManager(win)

			self.window_controllers[winID].on_load()

	'''def on_load(self, view):
		w = view.window()

		if w:
			print("onload, " + w.project_file_name())
		else:
			print("onload []")

	def on_new(self, view):
		w = view.window()

		if w:
			print("on_new, " + w.project_file_name())
		else:
			print("on_new []")

	def on_selection_modified(self, view):
		w = view.window()

		if w:
			print("on_selection_modified, " + w.project_file_name())
		else:
			print("on_selection_modified []")'''