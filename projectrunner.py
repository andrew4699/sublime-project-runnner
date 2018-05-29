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

			if winID not in self.window_controllers: # New window detected
				self.window_controllers[winID] = WindowManager(win)

			self.window_controllers[winID].on_load()