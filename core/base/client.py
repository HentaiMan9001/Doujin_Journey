from scripts.app import App
import requests
import  ui

#this is imported in order to reduce the need to call it in other scripts

class Client():
	def __init__(self):
		self.base_query_url = ''
		self.page = 1	
	'''
	The read method 
	'''
		
	def Read(self, Book):
		self.Book = Book
		self.fetch_books()
		App.Reader.open()
		
	def fetch_books(self, page):
		
		soup =
		
		#this is where you place the functions to parse the html to find the books from the search page
	
	def get_pages(self, book_info):
		pass
		#this is where you place your functions to scrape/generate the links to the books pages
		
		
	def Request(self):
		from bs4 import BeautifulSoup
		import requests
		url = self.Make_Search_Url()
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html5lib')
		books = self.fetch_books(page)
	
	def Make_Search_Url(self):
		tags = self.tags
		#this is where you preform string manipulation to make your query url
		
	@ui.in_background
	def search(self, tags):
		#this sets your page to 1 and searches for the url
		#Note: the tags variable is a list of strings
		self.page = 1
		self.tags = tags
		self.Request()
		
	@ui.in_background
	def next_page(self):
		self.page += 1
		self.Request()
		
	def open_gallery_page(self, book):
		pass
		
	@ui.in_background
	def previous_page(self):
		if self.page > 0:
			self.page -= 1
			self.Request()
		else:
			pass
