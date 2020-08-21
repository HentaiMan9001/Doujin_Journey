import ui

__all__ = ['Stepper']

class Stepper (ui.View):
	def __init__(self):
		self.action = None
		self.update_interval = 0.5
		
		self.down = down = ui.Button()
		down.image = ui.Image.named('iob:arrow_down_a_32')
		down.change = -1
		down.action = self.step
		self.add_subview(down)
		
		self.counter = counter = ui.Label()
		self.add_subview(counter)
		
		self.up = up = ui.Button()
		up.image = ui.Image.named('iob:arrow_up_a_32')
		down.change = 1
		down.action = self.step
		self.add_subview(up)
		
	def update(self):
		if self.counter.text != str(self.value):
			self.counter.text = str(self.value)
		else:
			pass
	
	def step(self, button):
		if self.value + button.change < 0:
			pass
		else:
			self.value += change
			
		self.action()
		
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
		

