import requests
from bs4 import BeautifulSoup
#from scripts.classes import Book
from scripts.client import client
import re


search_url = "https://beta.imagefap.com/gallery.php"

search_string ="?search={}"

url = search_url + search_string.format('Ass')+'&page=1'


req = requests.get(url)

soup = BeautifulSoup(req.content,'html5lib')


def make_books(sets):
	books = list()
	for gallery,pic in sets:
		book = dict()
		book['title'] = gallery.find('a').get('title')
		book['id'] = gallery.get('id')
		book['thumb'] = pic.find('img').get('src')
		book['link'] = 'https://www.imagefap.com' + gallery.find('a').get('href') + '&view=2'
		
		books.append(book)
	return books

def get_galleries(soup):
	main_div = soup.find('div',id="main")
	
	id_matcher = re.compile(r'\d{7}')
	
	galleries = main_div.find_all('tr',id = id_matcher)
	pics = main_div.find_all('table')[13:34]
	return make_books(zip(galleries,pics))





	
	
books = 
	
test_url = books[19]['link'].replace('www','beta')
s = BeautifulSoup(requests.get(test_url).content)
	
def get_image_url_from_image_page(soup):
	return soup.find('span',{'itemprop':'contentUrl'}).text
	
def get_gallery_images(soup):
	gal = s.find('div',{'id':'gallery'})
	
	tds = gal.find('table').find_all('td')
	
	
	items_to_use = list()
	
	for td in tds:
		if td.find('table'):
			items_to_use.append(td)
	
	sets = [{'src':td.find('img').get('src'),'href':'https://www.imagefap.com'+td.find('a').get('href')} for td in items_to_use]





link_list = list()

for set in sets:
	page_url = set['href']

	soup = BeautifulSoup(requests.get(page_url).content)
	
	link_list.append(get_image_url_from_image_page(soup))
	
import photos, ui


for link in link_list:
	photos.save_image(ui.Image.from_data(requests.get(link).content))
	

