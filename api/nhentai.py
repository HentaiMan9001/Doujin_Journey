import ui
from scripts import app
from scripts.functions import make_soup
from core.client import Client
from core.book import Book

	
def get_gall_id(book):
	import re
	a = book.find('a')
	href = a.get('href')
	gall_id_finder = re.compile('/g/(\d+)/')
	gal_id = gall_id_finder.search(href).group(1)
	return gal_id
	
def get_books(soup):
	container_div = soup.find('div',{'class':'container index-container'})
	books = container_div.find_all('div',{'class':'gallery'})
	return books
	
def get_title(book):
	caption = book.find('div',{'class':'caption'})
	title = caption.get_text()
	return title
	
def get_thumb(book):
	import requests
	a = book.find('a')
	img = a.find('img')
	link = img.get('data-src')
	image_req = requests.get(link)
	raw_data = image_req.content
	return raw_data
	
def get_book_info(book):
	base_url = 'https://www.nhentai.net/'
	title = get_title(book)
	gal_id = get_gall_id(book)
	thumb = get_thumb(book)
	gall_url = base_url+'g/'+gal_id+'/'
	return {'title':title,'id':gal_id,'thumb':thumb,'link':gall_url}
		
def nhentai_search(url):
	
	soup = make_soup(url)
	books = get_books(soup)
	for book in books:
		
		info = get_book_info(book)
		the_book = Book(info)
		view.add_book(the_book)

def get_tags(sects):
	parts = {'Parody':0,'Character':1,'Tags':2,'Authors':3,'Groups':4,'Languages':5,'Catagories':6}
	info = {}
	names = list(parts.keys())
	for name in names:
		part = parts[name]
		li = []
		span = sects[part]
		tags = span.find_all('span')
		for tag in tags:
			for a in tag.find_all('a'):
				li.append(a.text)
		info.update({name:li})
	return info

@ui.in_background
def nhentai_gallery(url):
	req =requests.get(url)
	soup =BeautifulSoup(req.content,'html5lib')
	info_div = soup.find('div',{'id':'info'})
	tags = info_div.find('section',{'id':'tags'})
	tag_sections = info_div.find_all('div')
	info = get_tags(tag_sections)
	return info

def get_img_urls(soup):
	img_div = soup.find('div',{'class':'container','id':'thumbnail-container'})
	imgs = img_div.find_all('img',{'class':'lazyload'})
	urls = []
	for img in imgs:
		urls.append(img.get('data-src'))
	for i in range(len(urls)):
		url = urls[i]
		url = url.replace('//t','//i')
		url = url.replace('t.','.')
		urls[i] = url
	return urls
	
def download_raw(url):
	import requests
	req = requests.get(url)
	img_data = req.content
	return img_data
	
def save_book(soup, book):
	book_name = book.title
	img_urls = get_img_urls(soup)
	download_gallery(img_urls)

@ui.in_background
def nhentai_read(url):
	view = app.Reader
	import concurrent.futures
	soup = make_soup(url)
	img_urls = get_img_urls(soup)
	url_count = len(img_urls)
	view.set_reader(url_count)
	while view.is_reading:
		with concurrent.futures.ThreadPoolExecutor() as exicutor:
				results = exicutor.map(download_raw,img_urls)
				for raw_data in results:
					view.add_page(raw_data)
		if len(view.pages) == url_count:
			break

def get_download_links(gallery_link):
	soup = make_soup(gallery_link)
	urls = get_img_urls(soup)
	return urls

class Nhentai_Client(Client):
	def __init__(self):
		self.base_query_url = 'https://nhentai.net/search/?q={}&amp;page={}'
		self.hostname = 'nhentai'
		
	def read(self, Book):
		link = Book.link
		view = app.reader
		view.reset_reader()
		view.present('fullscreen',hide_title_bar = True)
		nhentai_read(link, view)
			
	def download_book(self, save_button, book):
		link = book.link
		title = book.title
		links = get_download_links(link)
		scripts.download_book(save_button, links, title)
	
	def set_url(self):
		tag_input = '+'.join(tags)
		self.search_url = self.base_query_url.format(tag_input,self.page)

	def get_books (self):
		nhentai_search(self.search_url,self.App.main_view)
		
if __name__ == '__main__':
	app.client.add_client(Nhentai_Client())
