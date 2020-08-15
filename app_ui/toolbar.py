import ui
import scripts
import gestures

class Toolbar(ui.View):
	def __init__(self, App):
		self.scrollview = ui.ScrollView()
		self.items = list()
		
	def set_items(self, items):
		self.items = items
		self.layout()
		for item in items:
			self.scrollview.add_subview(item)
			
	def layout(self):
		self.scrollview.frame = self.bounds
		scripts.vert(view_list = self.items, parent_view = self.scrollview)
