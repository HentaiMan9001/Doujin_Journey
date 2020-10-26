import ui
from scripts import app

class Book(ui.View):
	def set_info(self, info):
		self.__dict__.update(info)
		
	def __init__(self, info):
		self.set_info(info)
		self.bg_color='#c0cdde'
		self.border_width = 1
		self.corner_radius = 4
		
		self.title_bar = title_bar = ui.Label()
		title_bar.bg_color = 'white'
		title_bar.text = self.title
		self.add_subview(title_bar)
		
		self.img_box = img_box = ui.Button()
		img_box.action = self.open_page
		img_box.background_image = ui.Image.from_data(self.cover)
		self.add_subview(img_box)

	def open_page(self, button):
		page = app.page
		page.set_info(self)
		page.present('fullscreen', hide_title_bar = True)
		
	def layout(self):
		title = self.title_bar
		img_box = self.img_box
		
		img_box.x = 0
		img_box.y = 0
		img_box.width = self.width
		img_box.height = self.height-20
		
		title.x = 0
		title.y = img_box.height
		title.width = self.width
		title.height = self.height-title.y

	@property
	def cover_image(self):
		return ui.Image.from_data(self.cover)
		
	def is_album_in_photos(self):
		if self.title is in app.gal_names:
			return True
		else:
			False
