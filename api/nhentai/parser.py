
import requests
from bs4 import BeautifulSoup
import re
#from scripts.functions import make_soup

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
	return raw_data
	
def get_book_info(book):
	base_url = 'https://www.nhentai.net/'
	title = get_title(book)
	gal_id = get_gall_id(book)
	thumb = get_thumb(book)
	gall_url = base_url+'g/'+gal_id+'/'
	return {'title':title,'id':gal_id,'thumb':thumb,'link':gall_url}
		
def nhentai_search(url,view):
	import scripts
	soup = make_soup(url)
	books = get_books(soup)
	for book in books:
		the_book = scripts.Book()
		info = get_book_info(book)
		the_book.data = info
		view.add_book(the_book)

def get_tags(sects):
	parts = {'Parody':0,'Character':1,'Tags':2,'Authors':3,'Groups':4,'Languages':5,'Catagories':6}
	info = {}
	for name, part in parts.items:
		part = parts[name]
		li = []
		span = sects[part]
		tags = span.find_all('span')
		for tag in tags:
			for a in tag.find_all('a'):
				li.append(a.text)
		info.update({name:li})
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
	

def get_download_links(gallery_link):
	soup = make_soup(gallery_link)
	urls = get_img_urls(soup)
	return urls

def get_sections(tag_section):
	sections = tag_section.find_all('div', {'class':'tag-container field-name '})
	return sections
	
def get_section_name(section):
	name_finder = re.compile(r'(?<=\t)(\w+)')

	section_name = name_finder.findall(section.contents[0])[0]
	
	return section_name
	
def get_tags(section):

	section_span = section.find('span')
	
	tags = section_span.find_all('a')
	tag_names = list()
	
	for tag in tags:
		tag_name = tag.find('span').text
		tag_names.append(tag_name)
	return tag_names
	
url = 'https://nhentai.net/g/334828/'
def get_gallery_info(book):
	url = book.link
	soup = make_soup(url)
	
	info_div = soup.find('div', {'id':'info'})
	info = dict()
	tag_section = info_div.find('section', {'id':'tags'})
	
	sections = get_sections(tag_section)
	for section in sections:
		section_name = get_section_name(section)
		section_tags = get_tags(section)
		info.update({section_name:section_tags})
	book.info = info

