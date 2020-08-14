import ui
import scripts
import gestures

__all__ = ['Reader']

class Page_View_Delegate (object):
	def __init__(self, page_label):
		self.page_label = page_label	
	def scrollview_did_scroll(self, scrollview):
		page_width = scrollview.width
		x,y = scrollview.content_offset
		
		scrollview.page = (x//page_width) + 1
		self.page_label.text = str(int(scrollview.page))

class Progres_Indicator(ui.View):
	def __init__(self):
		self.max = 0
		self.count = 0

		self.corner_radius = 4
		self.background_color = 'grey'
		self.alpha = 0.8
		
		self.is_showing = False
		
		
		self.current_page = 0
		
		self.exit_button = exit_button = ui.Button()
		exit_button.image = ui.Image.named('iob:close_32')
		self.add_subview(exit_button)
		
		self.border_width = 1
		self.label = label = ui.Label()
		label.text = '0/0'
		label.alignment = ui.ALIGN_CENTER
		self.add_subview(label)
		
	def reset(self):
		self.max = 0
		self.count = 0
		self.set_label()
		
	def set(self, max):
		self.max = max
		self.set_label()
		
	def set_label(self):
		self.label.text = '%s/%s'%(self.count, self.max)
		
	def update(self):
		self.count += 1
		self.set_label()
		
	def layout(self):
		button = self.exit_button
		button.frame = (0, 0, self.height, self.height)
		
		label = self.label
		label.frame = (button.width,0, self.width - button.width, self.height)
		

class Reader(ui.View):
	def __init__(self, App):
		self.App = App
		self.background_color = 'white'
		
		self.is_reading = True
		
		self.page = page = ui.Label()
		page.text = '0'
		page.alignment = ui.ALIGN_CENTER
		page.bring_to_front()
		self.add_subview(page)
		
		self.page_view = page_view = ui.ScrollView()
		page_view.delegate = Page_View_Delegate(page)
		page_view.send_to_back()
		self.add_subview(page_view)
		page_view.shows_horizontal_scroll_indicator =False
		page_view.shows_vertical_scroll_indicator = False
		page_view.paging_enabled =True
		tap = gestures.tap(page_view, self.page_was_tapped)
		
		self.progress_bar = progress_bar = Progres_Indicator()
		progress_bar.exit_button.action = self.close_reader
		self.add_subview(progress_bar)
		
		self.page_holders = list()
		self.pages = list()
		
	def close_reader(self, button):
		self.is_reading = False
		self.close()
	
	def reset_reader(self):
		for view in self.page_view.subviews:
			self.page_view.remove_subview(view)
		self.page_holders.clear()
		self.pages.clear()
		self.progress_bar.reset()
		self.is_reading = True
		self.page.text = '1'
		self.page_view.content_offset = (0,0)

	#@ui.in_background
	def set_reader(self, page_count):
		self.progress_bar.set(page_count)
		w,h = ui.get_screen_size()
		size = lambda i: (w * i,h-18)
		self.page_view.content_size = size(page_count)
		'''
		for _ in range(page_count):
			holder = ui.ActivityIndicator()
			holder.style = ui.ACTIVITY_INDICATOR_STYLE_GRAY
			holder.start()
			holder.hides_when_stopped = True
			self.page_holders.append(holder)
			self.page_view.add_subview(holder)
		'''
			
	def add_page(self, image_data):
		
		w,h = ui.get_screen_size()
		frame = lambda i: (w*i,0,w,h-18)
		
		self.progress_bar.update()
		image_view = ui.ImageView()
		image = ui.Image.from_data(image_data)
		image_view.image = image
		self.pages.append(image_view)
		count = self.pages.index(image_view)
		image_view.frame = frame(count)
		image_view.send_to_back()
		#coresponding_holder = self.page_holders[count]
		self.page_view.add_subview(image_view)
	
	def page_was_tapped(self, data):
		progress_bar = self.progress_bar
		if progress_bar.is_showing:
			progress_bar.is_showing = False
		else:
			progress_bar.is_showing = True
		ui.animate(self.layout, duration = 0.5)
		
	def layout(self):
		spacer = 18
		
		page_view = self.page_view
		progress_bar = self.progress_bar
		progress_bar.height = 40
		progress_bar.width = self.width
		page_view.frame = (0, spacer, self.width, self.height - spacer)
		
		if progress_bar.is_showing:
			progress_bar.y = spacer
		else:
			progress_bar.y = - progress_bar.height
		
		page = self.page
		page.height = 20
		page.x = 0
		page.y = self.height - page.height
		page.width = self.width

def test():
	view = Reader(None)
	view.set_reader(10)
	view.present('fullscreen',hide_title_bar = True)
	

