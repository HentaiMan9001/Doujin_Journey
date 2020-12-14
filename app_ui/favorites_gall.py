import ui
import math
import gestures
import scripts
import app_ui

__all__=['Main_View']

def get_book_info(book_dir):
	

def get_favorites():
	books = os.listdir('books')
	for book in books:
		if book is not os.path.isdir(book):
			books.remove(book)
	return books

def make_book_objects():
	books = get_favorites()
	objs = []
class Main_View(ui.View):
	def __init__(self,App):
		self.books = []
		self.App = App
		
		self.Menu = App.Menu
		self.Menu.bring_to_front()
		self.add_subview(self.Menu)
		
		self.update_interval = 0.5
		self.bg_color='white'
		
		gestures.doubletap(self, self.close_self)
		
		scroll_view = ui.ScrollView()
		self.scrollview = scroll_view
		self.add_subview(scroll_view)
	
	
	def close_self(self, data):
		self.close()

	def add_books(self,book_obj):
		book = app_ui.Book_Icon(book_obj,self.App)
		self.books.append(book)
		self.layout()
		self.scrollview.add_subview(book)
		
	def reset(self):
		for book in self.books:
			self.scrollview.remove_subview(book)
		self.books.clear()
		self.layout()

	def layout(self):
		Menu = self.App.Menu
		Menu.width = self.width
		Menu.y = 18
		
		menu_bar = self.App.menu_bar
		menu_bar.height = 32
		
		scrollview = self.scrollview
		scrollview.width = self.width
		scrollview.y = Menu.y + menu_bar.height
		scrollview.height = self.height-menu_bar.height-Menu.y
		scrollview.send_to_back()
		
		scripts.grid(view_list = self.books, parent_view = scrollview, views_per_row = 3,aspect_ratio = 1.6)
		

#main()
