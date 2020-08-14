import ui
import gestures
import scripts

__all__ = ['Gallery_Page']

class section(ui.View):
	def __init__(self, name):
		self.name = name
		title = ui.Label()
		title.text = name
		self.title = title
		self.items = []
		self.add_subview(title)
		
		self.gap = 3
	
		scrolls = ui.ScrollView()
		scrolls.border_width = 1
		scrolls.corner_radius = 4
		self.scrolls = scrolls
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
	def __init__(self, App):
		self.App = App
		
		self.bg_color = 'white'
		title = ui.Label()
		title.text = 'n/a'
		title.alignment = ui.ALIGN_CENTER
		self.title = title
		title.border_width=1
		title.corner_radius=4
		self.add_subview(title)
		gestures.swipe(self,self.close_self,direction=gestures.DOWN)
		
		
		cover = ui.ImageView()
		self.cover = cover
		gestures.long_press(cover, self.set_url)
		cover.border_width=1
		self.add_subview(cover)
		
		author = section('Author')
		self.author = author
		self.add_subview(author)
		
		read_button = ui.Button()
		read_button.title = 'Read'
		self.read_button = read_button
		read_button.action = self.read
		self.add_subview(read_button)
		
		add_button = ui.Button()
		add_button.title='Add to Collection'
		self.add_button = add_button
		add_button.action = self.add
		self.add_subview(add_button)
		
		save_button = ui.Button()
		save_button.title = 'Save'
		save_button.action = self.save
		self.save_button = save_button
		self.add_subview(save_button)
		
		tags = section('Tags')
		self.tags = tags
		self.add_subview(tags)
		
	def set_url(self,data):
		import clipboard
		clipboard.set(self.book.link)
		
	def close_self(self,data):
		self.close()
		
	def set_info(self,book):
		#self.views = views
		self.book = book
		self.cover.image = ui.Image.from_data(book.thumb_data)
		self.title.text = book.title
		
	def add(self,button):
		url = self.book.link
		title = self.book.title
		save_book(title,url)
		
	def read(self,button):
		self.App.client.read(self.book)
		
	def save(self,button):
		link = self.book.link
		self.App.client.download_book(self.save_button, link)
		
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
