import ui,gestures
from scripts import Organize as Org

class Toolbar(ui.View):
	def __init__(self,App,gap = 4):
		self.scrollview = ui.ScrollView()
		self.items = []
		self.gap = gap
	def set_items(self,items):
		self.items = items
		for item in items:
			self.scrollview.add_subview(item)
		self.layout()
	def layout(self):
		self.scrollview.frame = self.bounds
		
		gap = self.gap
		button_width = self.width - 2*gap
		button_height = 50
		number_of_items = len(self.items)
		i = number_of_items
		
		height_taken_up = i*button_height + (i+1)*gap
		
		if height_taken_up < self.height:
			self.scrollview.content_size = (self.width,self.height)
		else:
			self.scrollview.content_size = (self.width,height_taken_up)
			
		item_dim = (button_width,button_height)
		Org.vert(self.items,dim = item_dim)
