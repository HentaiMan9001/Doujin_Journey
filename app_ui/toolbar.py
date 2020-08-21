import ui
import scripts

__all__ = ['Toolbar']

class Toolbar(ui.View):
	def __init__(self, App):
		self.scrollview = ui.ScrollView()
		self._items = list()
		
	@property
	def items(self):
		return self.items
		
	@items.setter
	def items(self, items):
		self._items = items
		self.layout()
		for item in self._items:
			self.scrollview.add_subview(item)
			
		
	def layout(self):
		self.scrollview.frame = self.bounds
		
		if len(self._items) is not 0:
			scripts.vert(view_list = self._items, parent_view = self.scrollview)
		else: pass
