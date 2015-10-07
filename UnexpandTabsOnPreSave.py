import sublime, sublime_plugin

class OpenCommand(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if view.find("    ", 0):
			view.run_command("unexpand_tabs")
