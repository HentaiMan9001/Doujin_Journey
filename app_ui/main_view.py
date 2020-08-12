import ui
import math
import gestures
import scripts
import app_ui

__all__=['Main_View']

class Main_View(ui.View):
	def __init__(self,App):
		self.books = []
		self.testing = 0
		self.name = 'main'
		w,h=	ui.get_screen_size()
		self.App = App
		
		self.Menu = App.Menu
		self.Menu.bring_to_front()
		self.add_subview(self.Menu)
		
		self.update_interval = 0.5
		print(w,h)
		self.width = w
		self.height = h
		self.bg_color='white'
		self.gap = 4
		self.cols = 3
		self.book = None
		self.starting_y = 0	
		self.base_starting_x = self.gap
		self.starting_x = self.base_starting_x
		self.base_starting_y = self.gap
		self.starting_y = self.base_starting_y
		
		gestures.doubletap(self,self.close_self)
		self.max_pic_width = (self.width-(self.cols+1)*self.gap)/self.cols
		print(self.max_pic_width)
		
		self.pic_height = (1/0.75)*self.max_pic_width
		#print(self.max_pic_width)
		
		scroll_view = ui.ScrollView()
		self.scrollview = scroll_view
		self.add_subview(scroll_view)
		
	def close_self(self,data):
		self.close()
		
	def place_book(self,book):
		i = self.books.index(book)
		
	def rearange_books(self):
		pass
		
	def add_book(self,book_obj):
		book = app_ui.Book_Icon(book_obj,self.App)
		self.scrollview.add_subview(book)
		self.books.append(book)
		#self.layout()
		
	def reset(self):
		for book in self.books:
			self.scrollview.remove_subview(book)
		self.books.clear()
		self.layout()
		
	def update(self):
		for book in self.books:
			if book.x or book.y == 0:
				self.layout()
			else:
				pass

	def set_scrollview_size(self):
		scrollview = self.scrollview
		gap = self.gap
		height = self.pic_height
		width = self.max_pic_width
		
		total_count = len(self.books)
		i = total_count
		total_rows = total_count//(scrollview.width//width)
		
		scroll_size = (scrollview.width,(total_rows+1)*height + (total_rows+3)*gap)
		if scrollview.content_size == scroll_size:
			pass
		else:
			scrollview.content_size = scroll_size

	def layout(self):
		Menu = self.App.Menu
		Menu.width = self.width
		Menu.y = 18
		
		menu_bar = self.App.menu_bar
		
		scrollview = self.scrollview
		scrollview.width = self.width
		scrollview.y = Menu.y + menu_bar.height
		scrollview.height = self.height-menu_bar.height-Menu.y
		scrollview.send_to_back()
		
		height = self.pic_height
		width = self.max_pic_width
		
		self.set_scrollview_size()
		
		scripts.grid(view_list = self.books, parent_view = scrollview, views_per_row = 3,aspect_ratio = 1.6)
		

#main()
