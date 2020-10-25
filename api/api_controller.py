from scripts import app
#__all__ = ['Api_Controller']

class Api_Controller():
	def __getitem__(self, key):
		return self.apis[key]
		
	def __setitem__(self, key, value):
		self.apis[key] = value
		
	def __init__(self):
		self.nhentai = api.nhentai_api(App)
		self.apis = dict()
	def add_client(self, client):
		self.apis.update{client.hostname:client}
		
	def get_clients(self):
		return list(self.apis.keys())
		
	def switch(self, choice):
		self.current_api = self.apis[choice]
		
	def search(self, tags):
		self.App.nav.reset_index()
		self.current_api.search(tags)
		
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
			
if __name__ == '__main__':
	app.client = Api_Controller()
