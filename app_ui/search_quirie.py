import ui
import dialogs

max_field = {
	'title':'max',
	'type':'number',
	'key':'max'
}

min_field = {
	'title':'min',
	'type':'number',
	'key':'min'
}
fields = [max_field, min_field]

h = dialogs.form_dialog(title = 'test', fields = fields)

class query_view(ui.View):
	def __init__(self, App):
		self.App = App
		
		
