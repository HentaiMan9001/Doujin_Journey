from scripts import app
from api.nhentai import Nhentai_Client

class Client_Controller():
	apis = dict()
	def __getitem__(self, key):
		return self.apis[key]
		
	def __setitem__(self, key, value):
		self.apis[key] = value
		
	def __init__(self):
		self.apis['nhentai'] = Nhentai_Client()
		self.current_api = self.apis['nhentai']
		
	def get_clients(self):
		return list(self.apis.keys())
		
	def switch(self, choice):
		self.current_api = self.apis[choice]
		
	def search(self):
		app.nav.reset_index()
		self.current_api.search()
		
	def next_page(self):
		self.current_api.next_page()
		
	def previous_page(self):
		self.current_api.previous_page()
		
	def read(self, Book):
		self.current_api.read(Book)
		
	def download_book(self, button, book):
		if book.is_album_in_photos():
			import console
			console.alert('Alert','The book titled "%s" is already an album in photos'%(book.title))
		else:
			self.current_api.download_book(button, book)
			
