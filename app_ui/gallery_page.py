import ui
import gestures
import scripts
from scripts import app

__all__ = ['Gallery_Page']

class section(ui.View):
	def __init__(self, name):
		self.name = name
		title = ui.Label()
		title.text = name
		self.title = title
		self.items = []
		self.add_subview(title)
	
		self.scrolls = scrolls = ui.ScrollView()
		scrolls.border_width = 1
		scrolls.corner_radius = 4
		self.add_subview(scrolls)
		
	def set(self, info):
		self.book_info = info
		self.items = info[self.name]
		
	def layout(self):
		title = self.title
		title.alignment = ui.ALIGN_CENTER
		title.width = self.width
		title.height = 20
		
		scrolls = self.scrolls
		scrolls.y = title.height
		scrolls.width = self.width
		scrolls.height = self.height-title.height
		
		#scripts.vert(view_list = self.items)
		
class Gallery_Page(ui.View):
	def __init__(self):
		app.Gallery_Page = self
		self.update_interval = 1
		self.bg_color = 'white'
		self.title = title = ui.Label()
		title.text = 'n/a'
		title.alignment = ui.ALIGN_CENTER
		title.border_width=1
		title.corner_radius=4
		self.add_subview(title)
		gestures.swipe(self,self.close_self,direction=gestures.DOWN)
		
		
		self.cover = cover = ui.ImageView()
		gestures.long_press(cover, self.set_url)
		cover.border_width=1
		self.add_subview(cover)
		
		self.author = author = section('Author')
		self.add_subview(author)
		
		self.read_button = read_button = ui.Button()
		read_button.title = 'Read'
		read_button.action = self.read
		self.add_subview(read_button)
		
		self.add_button = add_button = ui.Button()
		add_button.title='Add to Collection'
		add_button.action = self.add
		self.add_subview(add_button)
		
		self.save_button = save_button = ui.Button()
		save_button.title = 'Save'
		save_button.action = self.save
		self.add_subview(save_button)
		
		self.tags = tags = section('Tags')
		self.add_subview(tags)
		
	def set_url(self, data):
		import clipboard
		import dialogs
		clipboard.set(self.book.link)
		dialogs.alert('Clipboard set', 'The url for this book was sey to your clipboard.')
	def update(self):
		if self.save_button.title != 'Save':
			self.save_button.title = 'Save'
	def close_self(self,data):
		self.close()
	
	def reset(self):
		self.book = None
		self.cover.image = None
		self.title.text = ''
		
	def set_info(self, book):
		self.reset()
		self.book = book
		self.cover.image = book.cover
		self.title.text = book.title
		
	def add(self,button):
		url = self.book.link
		title = self.book.title
		save_book(title,url)
		
	def read(self,button):
		app.client.read(self.book)
		
	def save(self,button):
		app.client.download_book(self.save_button, self.book)
		
	def layout(self):
		gap = 3
		
		title = self.title
		title.frame = (gap,gap,self.width-2*gap,50)
		
		cover = self.cover
		cover.frame = (gap,title.y+title.height+gap,self.width/2-6,self.height/2-title.y-title.height-gap)
		
		read_button = self.read_button
		read_button.y = cover.y
		read_button.border_width = 1
		read_button.corner_radius = 4
		read_button.x =cover.x+cover.width+gap
		read_button.width = cover.width/4
		read_button.height = 40
		
		save_button = self.save_button
		save_button.width = read_button.width*3
		save_button.x = read_button.x + read_button.width + gap
		save_button.border_width = 1
		save_button.corner_radius = 4
		save_button.bring_to_front()
		save_button.height = read_button.height
		save_button.y = read_button.y
		
		
		
		add_button = self.add_button
		add_button.y = read_button.y + read_button.height + gap
		add_button.x = read_button.x
		add_button.width = cover.width
		add_button.border_width=1
		add_button.corner_radius=4
		add_button.height = read_button.height
		
		author = self.author
		author.y = add_button.y+add_button.height+gap
		
		author.x = cover.x+cover.width+gap
		author.width = cover.width
		author.height = 60
		
		tags = self.tags
		tags.x = author.x
		tags.y = author.y + author.height + gap
		tags.width = cover.width
		tags.height = 80

def load():
	Gallery_Page()
