class Gallery():
	def __init__(self, title = str(), *args, **kwargs):
		self.title = title
	def is_album_in_photos(self):
		import photos
		
		albums = photos.get_albums()
		titles = list()
		for album in albums:
			titles.append(album.title)
		
		return self.title in titles
	def make_album(self):
