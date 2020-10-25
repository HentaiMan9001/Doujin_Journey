import ui
import requests
from scripts import app

class Client:
	def __init__(self):
		self.page = 1
		self.base_query_url = None
		self.tag_seperator = None
		self.hostname
		
	def read(self, Book):
		pass
		
	def download_book(self, save_button, book):
		pass
		
	def set_url(self):
		pass

	@ui.in_background
	def get_books(self):
		pass
		
	def new_search(self):
		self.page = 1
		self.search()

	def search(self):
		self.set_url()
		self.get_books()
		
	def next_page(self):
		self.page += 1
		self.search()
		
	def open_gallery_page(self, book):
		pass
		
	def previous_page(self):
		if self.page > 0:
			self.page -= 1
			self.search()
		else:
			pass
