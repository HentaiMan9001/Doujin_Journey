import ui
__all__ = ['save_book']

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


