import ui
from app_ui.search_bar import Search_Bar
from scripts import app
	
class menu_bar(ui.View):
	def __init__(self):
		self.background_color = '#c3c2d7'
		self.border_width = 1
		self.corner_radius = 4
		
		menu_button = ui.Button()
		menu_button.border_width=1
		menu_button.image = ui.Image.named('iob:more_32')
		self.menu_button = menu_button
		self.add_subview(menu_button)
		
		search_button = ui.Button()
		search_button.border_width = 1
		search_button.image = ui.Image.named('iob:ios7_search_strong_32')
		self.search_button = search_button
		search_button.action = self.drop_search_bar
		self.add_subview(search_button)
		
	def drop_search_bar(self, button):
		search_bar = app.search_bar
		if search_bar.is_open:
			search_bar.is_open = False
		else:
			search_bar.is_open = True
		ui.animate(app.Menu.layout, duration = 0.5)

	def layout(self):
		menu_button = self.menu_button
		menu_button.x = 0
		menu_button.y = 0
		
		search_button = self.search_button
		search_button.x = self.width-search_button.width
		search_button.y = 0
		
		menu_button.height = search_button.height = self.height
		menu_button.width = search_button.width = self.height
	
class Menu(ui.View):
	def __init__(self):
		self.name = 'menu'
		self.alpha = 0.8
		app.menu_bar = menu_bar()
		self.add_subview(app.menu_bar)
		
		app.search_bar = Search_Bar()
		self.add_subview(app.search_bar)
		
	def layout(self):
		menu_bar = app.menu_bar
		search_bar = app.search_bar
		
		menu_bar.width = search_bar.width = self.width
		menu_bar.bring_to_front()
		search_bar.send_to_back()
		search_bar.height = menu_bar.height
		
		if search_bar.is_open:
			search_bar.y = menu_bar.y + menu_bar.height
		else:
			search_bar.y = 0
		
		self.height = search_bar.height + menu_bar.height
		
if __name__ == '__main__':
	app.menu_bar = menu_bar()
	app.Menu = Menu()
