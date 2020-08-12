def make_DJ_dir():
	import os
	
	os.mkdir('Doujin_Journey')

guthub_file_list_url = 'https://github.com/HentaiMan9001/Doujin_Journey/find/master'


def get_file_tree(url):
	import requests
	from bs4 import BeautifulSoup
	
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html5lib')
	
	tree = soup.find('fuzzy-list', attrs = {'class':'js-tree-finder'})
	return tree
	
a = get_file_tree(guthub_file_list_url)

i = a.find_all('a')
