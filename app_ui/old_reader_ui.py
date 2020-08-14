import ui,gestures

from scripts import *
from app_ui import *
	
	
__all__ = ['reader']

class reader(ui.View):
	def __init__(self, App):
		self.App = App
		
		gap = 4
		
		self.update_interval = 0.1

		self.background_color='#aeb5b5'
		
		self.labels = list()
		self.buttons = list()
		
		self.index = Indexer()
		
		self.is_reading = True
		
		progress = ui.Label()
		progress.text = 'Progress = n/a'
		progress.width = self.width
		progress.height = 40
		progress.corner_radius = 3
		progress.border_width = 1
		self.labels.append(progress)
		self.progress = progress
		self.add_subview(progress)
		
		download_button = ui.Button()
		download_button.background_image = ui.Image.named('iob:ios7_download_32')
		self.download_button = download_button
		download_button.action = self.download
		self.add_subview(download_button)
		
		page_label = ui.Label()
		page_label.text = '0'
		page_label.width = 30
		page_label.height = 30
		page_label.center = (self.width/2,self.height-page_label.width/2)
		self.labels.append(page_label)
		self.page_label = page_label
		self.add_subview(page_label)
		
		image_box = self.image_box = ui.ImageView()
		 
		
		self.scrollview = scrollview = ui.ScrollView()
		self.scrollview_height = self.height-progress.y -progress.height-gap
		scrollview.border_width = 1
		scrollview.width = self.width
		scrollview.x = 0
		scrollview.y = progress.y + progress.height+gap
		scrollview.bg_color = '#aeb5b5'
		scrollview.height = self.height-progress.y-progress.height-gap
		scrollview.is_filling_screen = False
		gestures.swipe(scrollview,self.next,direction=gestures.LEFT)
		gestures.swipe(scrollview,self.previous,direction=gestures.RIGHT)
		gestures.swipe(self,self.revert_scrollview,direction=gestures.DOWN)
		gestures.swipe(scrollview,self.fill_screen,direction=gestures.UP)
		
		scrollview.add_subview(image_box)
		self.add_subview(scrollview)
		
	def clear_book(self):
		self.image_box.image = None
		self.index.image_list.clear()
		self.progress.text = '0/0'
		self.page_label.text = '0'
		
	def set_book(self, book):
		self.image_box.image = ''
		
	def exp_ret_scrollview(self):
		scrollview = self.scrollview
		progress = self.progress
		gap = 4
		if scrollview._is_filling_screen:
			scrollview.frame = scrollview.filled_frame 
		else:
			scrollview.frame = self.not_filled_frame
	def revert_scrollview(self, data):
		scrollview = self.scrollview
		if scrollview.is_filling_screen:
			scrollview.is_filling_screen = False
		else:
			self.close_self()
			
	def close_self(self):
		self.is_reading = False
		self.clear_book()
		self.close()
			
	def fill_screen(self, data):
		scrollview = self.scrollview
		if scrollview.is_filling_screen:
			pass
		else:
			scrollview.is_filling_screen = True
		
	def download(self, button):
		scripts.save_book(self.progress, self.book_title, self.index.image_list)

	def check_scrollview(self):
		scrollview = self.scrollview
		if scrollview.is_filling_screen:
			scrollview.frame = scrollview.filled_frame
		else:
			scrollview.frame = scrollview.not_filled_frame
	def layout(self):
		
		scrollview = self.scrollview
		progress,page_label = self.progress,self.page_label
		image_box = self.image_box
		gap = 4
		
		base_height = 40
		
		
		for label in self.labels:
			label.alignment = ui.ALIGN_CENTER
		
		progress.x = gap
		progress.y = gap
		progress.width = self.width - 2*gap
		progress.height = base_height - 2* gap
		
		scrollview.filled_frame = self.bounds
		
		scrollview.not_filled_frame = (0, progress.y + progress.height + gap, self.width, self.height - (progress.y + progress.height + gap))
		
		self.check_scrollview()
		
		page_label.center = (self.width/2,self.height-page_label.height/2)
		page_label.bring_to_front()
		
		image_box.frame = scrollview.bounds
		
	def set(self, max):
		self.index.set(max)
		
	def update(self):
		self.page_label.text = str(self.index.count + 1)
		self.progress.text = 'Progress = %s/%s'%self.index.get()
		
	def update_reader(self, data):
		self.index.append(data)
		if len(self.index.image_list) == 1:
			self.image_box.image = ui.Image.from_data(data)
			self.update()
	
	def next(self,data):
		self.index.next()
		self.page_label.text = str(self.index.count+1)
		image = ui.Image.from_data(self.index.index())
		self.image_box.image = image

	def previous(self,data):
		self.index.previous()
		self.page_label.text = str(self.index.count+1)
		self.image_box.image = ui.Image.from_data(self.index.index())
