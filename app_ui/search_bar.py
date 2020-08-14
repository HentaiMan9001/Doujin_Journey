import ui

__all__ = ['nav_bar', 'input_ui']

class nav_bar(ui.View):
	def __init__(self, App):
		self.name = 'nav'
		self.App = App
		self.height = 32
		self.is_closed = True
		
		next_button = ui.Button()
		next_button.image = ui.Image.named('iob:arrow_right_c_32')
		self.next_button = next_button
		self.add_subview(next_button)
		
		back_button = ui.Button()
		back_button.image = ui.Image.named('iob:arrow_left_c_32')
		self.back_button = back_button
		self.add_subview(back_button)
		
		self.index = 1
		
		page = ui.Label()
		page.text = str(self.index)
		page.alignment = ui.ALIGN_CENTER
		self.page = page
		self.add_subview(page)
		
	def reset_index(self):
		self.index = 1
		self.page.text = str(self.index)
			
	def set_button_size(self, button):
		button.width = button.height = self.height
		
	def set_label_size(self):
		text = self.page.text
		w,h = ui.measure_string(text, font=('<system>', 20))
		self.page.width = w
		self.page.height = self.height
	def layout(self):
		
		back_button = self.back_button
		back_button.x = 0
		back_button.y = 0
		self.set_button_size(back_button)
		
		next_button = self.next_button
		next_button.y = 0
		self.set_button_size(next_button)
		
		
		page = self.page
		page.x = back_button.width
		self.set_label_size()
		
		next_button.x = page.x + page.width
		
		self.width = sum([view.width for view in self.subviews])
		
	def next(self, button):
		self.index += 1
		self.page.text = str(self.index) 
		self.App.client.next_page()

	def previous(self, button):
		self.index -= 1
		self.page.text = str(self.index) 
		self.App.client.previous_page()

class input_delegate (object):
	def __init__(self, App, textfield):
		self.App = App
		self.textfield = textfield
		self.gap = gap = 4
		self.starting_x = self.gap
		
		search_button = ui.Button()
		search_button.title = 'Search'
		search_button.width = 60
		search_button.y = gap
		search_button.border_width = 1
		search_button.corner_radius = 4
		self.search_button = search_button
		search_button.action = self.search
		
	def replace_labels_with_text(self):
		textfield = self.textfield
		label_texts = []
		for label in self.labels:
			label_texts.append(label.text)
			textfield.remove_subview(label)
		text = ' '.join(label_texts)
		textfield.text = text
		
	def get_tags(self):
		import re
		textfield = self.textfield
		word_finder = re.compile('(\w+)')
		text = textfield.text
		self.words = word_finder.findall(text)
		self.tags = self.words
		textfield.text = ''
		
	def place_tag_labels(self):
		textfield = self.textfield
		self.labels = []
		gap = self.gap
		self.starting_x = gap
		for i,word in enumerate(self.words):
			label = ui.Label()
			label.text = word
			w,h = ui.measure_string(word,font=('<system>', 20), alignment=ui.ALIGN_LEFT)
			label.alignment = ui.ALIGN_CENTER
			self.starting_x += gap
			
			label.frame =(self.starting_x, gap,w,textfield.height-2*gap)
			
			self.starting_x += w
			
			
			label.border_width = 1
			label.corner_radius = 4
			self.labels.append(label)
			textfield.add_subview(label)
			
	def textfield_did_begin_editing(self,textfield):
		App = self.App
		search_button = self.search_button
		App.nav.is_closed = True
		App.search_bar.layout()
		App.search_bar.label.text = 'Search: '
		try:
			self.replace_labels_with_text()
		except:
			pass
		search_button.x = textfield.width - search_button.width - 2 * self.gap
		search_button.height = textfield.height - 2 * self.gap
		textfield.remove_subview(self.search_button)

	def textfield_did_end_editing(self, textfield):
		self.get_tags()
		self.place_tag_labels()
		textfield.add_subview(self.search_button)
		
	def search(self, button):
		App = self.App
		App.nav.is_closed = False
		App.search_bar.layout()
		App.search_bar.label.text = ''
		App.main_view.reset()
		App.client.search(self.tags)

class input_ui(ui.View):
	def __init__(self,App):
		self.App = App
		
		self.is_open = False
		self.background_color = '#a2a2a2'
		self.App = App
		self.border_width = 1
		self.corner_radius = 4
		
		self.nav = nav = App.nav
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
		field.delegate = input_delegate(self.App,field)
		self.add_subview(self.search_field)

	def open_nav(self):
		self.nav.nav_is_closed = False
		self.layout()
		
	def close_nav(self):
		self.nav.nav_is_closed = True
		self.layout()
		
	def move_nav_right(self):
		nav = self.nav
		if nav.y == 0:
			pass
		else:
			nav.y = 0
			
	def move_nav_left(self):
		nav = self.nav
		if nav.y == - nav.width:
			pass
		else:
			nav.y = - nav.width
			
	def layout(self):
		nav = self.nav
		nav.height = self.height
		
		label = self.label
		label.width = 80
		label.height = self.height
		
		field = self.search_field
		field.x = label.width
		field.width = self.width - nav.width
		field.height = nav.height
		
		if nav.is_closed:
			ui.animate(self.move_nav_left, duration = 0.5)
		else:
			ui.animate(self.move_nav_right, duration = 0.5)
