import ui
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
def save_image(image):
	import photos
	
	
