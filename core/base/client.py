class Client():
	def __init__(self,App):
		self.base_query_url = 'https://nhentai.net/search/?q={}&amp;page={}'
		self.history = []
		self.page = 1
		self.App = App
		max_pages = {
			'type':'number',
			'title':'Max Pages:',
			'key':'max'
		}
		
		min_pages = {
			'type':'number',
			'title':'Max Pages:',
			'key':'max'
		}
		self.query_fields = [max_pages, min_pages]
		
	def read(self, Book):
		link = Book.link
		view = self.App.reader
		view.reset_reader()
		view.present('fullscreen',hide_title_bar = True)
		nhentai_read(link, view)
		
	def download_book(self, save_button, book):
		link = book.link
		title = book.title
		links = get_download_links(link)
		scripts.download_book(save_button, links, title)
		
	@ui.in_background
	def search(self, tags):
		self.page = 1
		#if self.App.
		self.tags = tags
		tag_input = '+'.join(tags)
		self.search_url = self.base_query_url.format(tag_input,self.page)
		nhentai_search(self.search_url,self.App.main_view)
		
	@ui.in_background
	def next_page(self):
		self.page += 1
		tag_input = '+'.join(self.tags)
		self.search_url = self.base_query_url.format(tag_input,self.page)
		nhentai_search(self.search_url,self.App.main_view)
	def open_gallery_page(self,book):
		pass
		
	@ui.in_background
	def previous_page(self):
		if self.page > 0:
			self.page -= 1
			self.search_url = self.base_query_url.format(self.tags,self.page)
			nhentai_search(self.search_url,self.App.main_view)
		else:
			pass
