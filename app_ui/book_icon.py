import ui
import app_ui

__all__ = ['Book_Icon']

class Book_Icon(ui.View):
	def __init__(self, book, App):
		self.App = App
		self.bg_color='#c0cdde'
		self.border_width = 1
		self.corner_radius = 4
		self.book = book
		
		self.title_bar = title_bar = ui.Label()
		title_bar.bg_color = 'white'
		title_bar.text = book.title
		self.add_subview(title_bar)
		
		self.img_box = img_box = ui.Button()
		img_box.action = self.open_page
		img_box.background_image = book.thumb_image
		self.add_subview(img_box)

	def open_page(self, button):
		page = self.App.page
		page.set_info(self.book)
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
