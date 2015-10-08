import sublime, sublime_plugin

class OnPreSave(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if view.find("    ", 0):
			view.run_command("unexpand_tabs")
