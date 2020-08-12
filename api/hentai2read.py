import requests
from bs4 import BeautifulSoup

__all__ = []
'''
gal image format

https://static.hentaicdn.com/hentai/32239/1/ccdn0001.jpg.                   gall id^

get gall id

gall_div = soup.find('div',{'class':'js-raty'})
gall_id = gall_div.get('data-manga-id')


get pages
base_url = https://static.hentaicdn.com/hentai/{gall_id}/1/ccdn{page_number}.jpg.  

'''

def get_gall_id(soup):
	gall_div = soup.find('div',{'class':'js-raty'})
	gall_id = gall_div.get('data-manga-id')
	return gall_id

def get_gall_info():
	pass

def make_page_list(gall_id):
	pass
'''
test_url = 'https://hentai2read.com/annoying_sister_needs_to_be_scolded/'

req = requests.get(test_url)
soup = BeautifulSoup(req.content,'html5lib')

ul = soup.find('ul',{'class':'list list-simple-mini'})

li = ul.find_all('li',{'class':'text-primary'})

parts = {'Parody':0,'Ranking':1,'Status':2,'Release Year':3,'View':4,'Pages':5,'Author':6,'Artist':7,'Catagory':8,'Content':9,'Characters':10,'Language':11,'Storyline':12}

names = list(parts.keys())

for name in names:
	parts.update({name:li[parts[name]].text})

'''

