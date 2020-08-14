import ui,concurrent.futures
import requests
from bs4 import BeautifulSoup
import  app_ui

__all__ = ['nhentai_api','nhentai_read','save_book','download_gallery']

def save(info):
	import json,os
	cwd = os.getcwd()
	files_dir = os.path.join(cwd,'files','lib.json')
	try:
		with open(files_dir,'r') as file:
			content = json.load(file)
			file.close()
		if info in content:
			pass
		else:
			content.update(info)
			with open(files_dir,'w') as file:
				json.dump(content,file)
				file.close()
	except:
		content = info
		with open(files_dir,'w') as file:
				json.dump(content,file)
				file.close()
				
def make_soup(url):
	import requests
	from bs4 import BeautifulSoup
	req = requests.get(url)
	soup = BeautifulSoup(req.content,'html5lib')
	return soup
	
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
	return {'data':raw_data}
	
def get_book_info(book):
	base_url = 'https://www.nhentai.net/'
	title = get_title(book)
	gal_id = get_gall_id(book)
	thumb = get_thumb(book)
	gall_url = base_url+'g/'+gal_id+'/'
	return {'title':title,'id':gal_id,'thumb':thumb,'link':gall_url}
	
def make_search_url(tags,page=1):
	base_search_url = 'https://www.nhentai.net/?q={}&amp;page={}'
	if tags == list():
		tags = '+'.join(tags)
		url = base_search_url.format(tags,page)
		return url
	else:
		print('Please form tags into a list and try again')
def check_for_title_in_photos_albums(title):
	import photos
	albums = photos.get_albums()
	titles = [album.title for album in albums]
	if title in titles:
		return True
	else:
		return False
class Book():
	def __init__(self,info):
		self.title = info['title']
		self.gallery_id = info['id']
		self.thumb_data = info['thumb']['data']
		self.link = info['link']
		self.is_pre = self.is_album_in_photos()
	def is_album_in_photos(self):
		return check_for_title_in_photos_albums(self.title)
		
def make_search_url(tags):
	base_url = 'https://nhentai.net/search/?q={}&amp;page=1'
	
	input_tags = '+'.join(tags)
	url = base_url.format(input_tags)
	return url
	
@ui.in_background
def old_nhentai_search(tags,view):
	url = make_search_url(tags)
	soup = make_soup(url)
	books = get_books(soup)
	for book in books:
		info = get_book_info(book)
		the_book = Book(info)
		view.add_book(the_book)
		
def nhentai_search(url,view):
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


def download(type,url):
	if type == 'full':
		
		import Image
		from io import BytesIO
		import requests
		req = requests.get(url)
		img_data = BytesIO(req.content)
		image = Image.open(img_data)
		return image
#download
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
	
def download_full(url):
	import requests, Image
	from io import BytesIO
	req = requests.get(url)
	img_data = BytesIO(req.content)
	img = Image.open(img_data)
	return img

def save_img_to_phone():
	pass

@ui.in_background
def download_gallery(save_button,link):
	import photos, Image, requests
	from io import BytesIO
	soup = make_soup(link)
	save_button.title = 'Soup Made'
	info_div = soup.find('div',{'id':'info'})
	title = info_div.find('h1').text
	urls = get_img_urls(soup)
	total_pages = len(urls)
	album = photos.create_album(title)
	save_button.title = 'Album Made'
	images = list()
	i = 0
	save_button.title = 'Begin'
	with concurrent.futures.ThreadPoolExecutor() as exicutor:
				results = exicutor.map(download_full,urls)
				for img in results:
					i += 1
					save_button.title = 'Saved: %s/%s'%(i,total_pages)
					images.append(img)
	
	for img in images:
		photos.save_image(img)
	assets = photos.get_assets()
	
	gall_assets = list()
	for i in range(-total_pages,0):
		gall_assets.append(assets[i])
	album.add_assets(gall_assets)
	save_button.title = 'Complete'
					
def save_book(soup, book):
	book_name = book.title
	img_urls = get_img_urls(soup)
	download_gallery(img_urls)

@ui.in_background
def nhentai_read(url,view):
	soup = make_soup(url)
	img_urls=get_img_urls(soup)
	url_count = len(img_urls)
	view.set_reader(url_count)
	while view.is_reading:
		with concurrent.futures.ThreadPoolExecutor() as exicutor:
				results = exicutor.map(download_raw,img_urls)
				for raw_data in results:
					view.add_page(raw_data)
		if len(view.pages) == url_count:
			break
				
@ui.in_background
def nhentai_download(url,view):
	
	soup = make_soup(url)
	img_urls=get_img_urls(soup)
	imgs = download('full',img_urls)

def save_book(title,url):
	title = title
	soup = make_soup(url)
	urls = get_img_urls(soup)
	info = {title:urls}
	save(info)
	
test_url = 'https://nhentai.net/g/311132/'

class nhentai_api():
	def __init__(self,App):
		self.name = 'nhentai client'
		self.base_query_url = 'https://nhentai.net/search/?q={}&amp;page={}'
		self.history = []
		self.page = 1
		self.App = App
		
	def read(self, Book):
		link = Book.link
		view = self.App.reader
		view.reset_reader()
		view.present('fullscreen',hide_title_bar = True)
		nhentai_read(link, view)
		
	def download_book(self,button,link):
		download_gallery(button,link)
		
	@ui.in_background
	def search(self,tags):
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

def main_test():
	book_list = []
	soup = make_soup('https://www.nhentai.net/search/?q=shota+yaoi+english')
	books = get_books(soup)
	for book in books:
		info = get_book_info(book)
		the_book = Book(info)
		book_list.append(the_book)
	
	return book_list
	
books = main_test()
