import ui
from scripts import *

__all__ = ['Menu','nav_bar','input_ui','menu_bar']


class nav_bar(ui.View):
	def __init__(self, App):
		self.name = 'nav'
		self.App = App
		
		next_button = ui.Button()
		next_button.background_image = ui.Image.named('iob:arrow_right_c_32')
		next_button.width = 32
		next_button.height = 32
		self.next_button = next_button
		self.add_subview(next_button)
		
		back_button = ui.Button()
		back_button.background_image = ui.Image.named('iob:arrow_left_c_32')
		back_button.width = 32
		back_button.height = 32 
		self.back_button = back_button
		self.add_subview(back_button)
		
		self.index = 1
		
		page = ui.Label()
		page.height = 32
		page.text = str(self.index)
		page.alignment = ui.ALIGN_CENTER
		self.page = page
		self.add_subview(page)
	def reset_index(self):
		self.index = 1
		self.page.text = str(self.index)
	def layout(self):
		back_button = self.back_button
		back_button.x = 0
		back_button.y = 0
		
		next_button = self.next_button
		next_button.x = self.width-next_button.width
		next_button.y = 0
		
		page = self.page
		page.x = back_button.width
		page.width = self.width-back_button.width-next_button.width
		
	def next(self, button):
		self.index += 1
		self.page.text = str(self.index) 
		self.App.client.next_page()

	def previous(self, button):
		self.index -= 1
		self.page.text = str(self.index) 
		self.App.client.previous_page()
		
		
class input_delegate (object):
	def __init__(self,App):
		self.App = App
		self.gap = 4
		self.starting_x = self.gap
	def set(self,App):
		self.App.sync(App)
		self.client = self.App.client
	def textfield_did_begin_editing(self,textfield):
		App = self.App
		App.search_bar.close_nav()
		App.search_bar.label.text = 'Search: '
		try:
			label_texts = []
			for label in self.labels:
				label_texts.append(label.text)
				textfield.remove_subview(label)
			text = ' '.join(label_texts)
			textfield.text = text
			textfield.remove_subview(self.search_button)
		except:
			pass
	def textfield_did_end_editing(self, textfield):
		
		import re
		self.labels = []
		gap = self.gap
		word_finder = re.compile('(\w+)')
		text = textfield.text
		textfield.text = ''
		words = word_finder.findall(text)
		self.tags = words
		self.starting_x = gap
		for i,word in enumerate(words):
			label = ui.Label()
			label.text = word
			w,h = ui.measure_string(word,font=('<system>', 20), alignment=ui.ALIGN_LEFT)
			label.alignment = ui.ALIGN_CENTER
			self.starting_x += gap
			label.x = self.starting_x
			self.starting_x += w
			label.y = gap
			label.height = textfield.height-2*gap
			label.width = w
			label.border_width=1
			label.corner_radius = 4
			self.labels.append(label)
			textfield.add_subview(label)
		search_button = ui.Button()
		search_button.title = 'Search'
		search_button.width = 60
		search_button.x = textfield.width -search_button.width
		search_button.y = gap
		search_button.height = textfield.height -2*gap
		search_button.border_width = 1
		search_button.corner_radius = 4
		self.search_button = search_button
		search_button.action = self.search
		textfield.add_subview(search_button)
	def search(self, button):
		App = self.App
		App.search_bar.open_nav()
		App.search_bar.label.text = ''
		App.main_view.reset()
		App.client.search(self.tags)

class input_ui(ui.View):
	def __init__(self,App):
		self.name = 'search bar'
		self.App = App
		self.is_open = False
		self.background_color = '#a2a2a2'
		self.App = App
		self.border_width=1
		self.corner_radius=4
		
		
		self.nav = nav = App.nav
		nav.width = 80
		nav.x = - nav.width
		self.add_subview(nav)
		
		
		
		label = ui.Label()
		label.text = 'Search: '
		label.alignment = ui.ALIGN_CENTER
		self.label = label
		self.add_subview(label)
		
		field = ui.TextField()
		field.border_width=1
		field.corner_radius = 4
		
		self.search_field = field
		
		field.delegate = input_delegate(self.App)
		self.add_subview(self.search_field)		
	def open_nav(self):
		ui.animate(self.nav_open,duration=0.5)
	def close_nav(self):
		ui.animate(self.nav_close,duration=0.5)
	def nav_close(self):
		App = self.App
		nav = App.nav
		nav.x = -nav.width
	def nav_open(self):
		App = self.App
		nav = App.nav
		nav.x = 0
	def layout(self):
		nav = self.nav
		nav.width = 80
		
		nav.y = 0
		nav.height = self.height
		
		label = self.label
		label.x = 0
		label.y = 0
		label.width = 80
		label.height = self.height
		
		field = self.search_field
		field.x = label.width
		field.width = self.width - label.width
		field.y = nav.y
		field.height = nav.height
		
		
	
class menu_bar(ui.View):
	def __init__(self,App):
		self.App = App
		self.name = 'menu bar'
		App.menu_bar = self
		self.background_color = '#c3c2d7'
		self.height = 32
		self.border_width = 1
		self.corner_radius = 4
		menu_button = ui.Button()
		menu_button.border_width=1
		menu_button.background_image = ui.Image.named('iob:more_32')
		menu_button.width = 32
		menu_button.height = 32
		self.menu_button = menu_button
		self.add_subview(menu_button)
		
		search_button = ui.Button()
		search_button.border_width = 1
		search_button.width = 32
		search_button.height = 32
		search_button.background_image = ui.Image.named('iob:ios7_search_strong_32')
		self.search_button = search_button
		search_button.action = self.drop_search_bar
		self.add_subview(search_button)
		
	def drop_search_bar(self,button):
		#print('test')
		search_bar = self.App.search_bar
		if not search_bar.is_open:
			search_bar.is_open = True
		else:
			search_bar.is_open = False
		ui.animate(self.App.Menu.update,duration=0.5)
	
	def layout(self):
		
		menu_button = self.menu_button
		menu_button.x = 0
		menu_button.y = 0
		
		search_button = self.search_button
		search_button.x = self.width-search_button.width
		search_button.y = 0
		
	
class Menu(ui.View):
	def __init__(self,App):
		self.name = 'menu'
		self.App = App
		#self.y = 0
		
		self.menu_bar = App.menu_bar
		self.add_subview(self.menu_bar)
		
		
		self.search_bar = App.search_bar
		self.add_subview(self.search_bar)
	
	def update(self):
		
		search_bar = self.App.search_bar
		menu_bar = self.App.menu_bar
		if search_bar.is_open:
			search_bar.y = menu_bar.y + menu_bar.height
		else:
			search_bar.y = menu_bar.y
		
	def layout(self):
		menu_bar = self.App.menu_bar
		search_bar = self.App.search_bar
		
		menu_bar.width = search_bar.width = self.width
		menu_bar.bring_to_front()
		search_bar.send_to_back()
		menu_bar.height = search_bar.height = 32
		
		
		
		
		
		
	
		

def test():
	view = ui.View()
	menu = Menu({})
	view.add_subview(menu)
	view.present()



