import ui
__all__ = ['save_book', 'check_for_title_in_photos_albums', 'save_book_in_lib', 'download_book','load_settings_file']

def save_settings_file():
	pass
def load_settings_file():
	import json
	import os
	cwd = os.getcwd()
	path = os.join(cwd,'files','settings.json')
	with open(path, 'r', encoding = 'utf-8') as file:
		settings = json.load(file)
		file.close()
	return settings

def download_full(url):
	import requests, Image
	from io import BytesIO
	req = requests.get(url)
	img_data = BytesIO(req.content)
	img = Image.open(img_data)
	return img

@ui.in_background
def save_book(view, title, img_list):
	max = len(img_list)
	
	import photos, Image
	from io import BytesIO
	
	album = photos.create_album(title)
	
	for i, img in enumerate(img_list):
		img_data = BytesIO(img)
		image = Image.open(img_data)
		view.text = 'Saved = %s/%s'%(i+1,max)
		photos.save_image(image)
	assets = photos.get_assets()
	pic_assets = list()
	for i in range(-max,-1):
		pic_assets.append(assets(i))
	album.add_assets(pic_assets)
	view.text = 'Complete'

def check_for_title_in_photos_albums(title):
	import photos
	albums = photos.get_albums()
	titles = [album.title for album in albums]
	if title in titles:
		return True
	else:
		return False
		
def save_book_in_lib(info):
	import os
	import json
	
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

@ui.in_background
def download_book(save_button, links, title):
	import photos
	import Image
	import requests
	from io import BytesIO
	import concurrent.futures
	
	total_pages = len(links)
	album = photos.create_album(title)
	save_button.title = 'Album Made'
	images = list()
	
	i = 0
	save_button.title = 'Begin'
	with concurrent.futures.ThreadPoolExecutor() as exicutor:
				results = exicutor.map(download_full,links)
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
