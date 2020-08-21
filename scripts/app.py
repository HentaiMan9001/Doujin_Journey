#from strings import string

__all__ = ['App']
import api
import scripts
import app_ui
	
class App(object):
	def __init__(self):
		self.views = list()
	
	def __setattr__(self,name,value):
		self.__dict__[name] = value
		
	def __getattribute__(self,name):
		return  object.__getattribute__(self,name)
		
	def initialize(self):
		self.load_Gallery_Page()
		self.load_reader()
		self.prepare_client()
		self.load_main_menu()
		
	def load_Gallery_Page(self):
		self.page = app_ui.Gallery_Page(self)
		self.views.append(self.page)
	def prepare_client(self):
		self.client = api.Api_Controller(self)
		
	def load_reader(self):
		self.reader = app_ui.Reader(self)
		self.views.append(self.reader)
		
	def load_main_menu(self):
		self.nav = app_ui.nav_bar(self)
		self.views.append(self.nav)
		self.menu_bar = app_ui.menu_bar(self)
		self.views.append(self.menu_bar)
		self.search_bar = app_ui.input_ui(self)
		self.views.append(self.search_bar)
		self.Menu = app_ui.Menu(self)
		self.main_view = app_ui.Main_View(self)
		self.views.append(self.main_view)
		
	def run(self):
		self.main_view.present('fullscreen',hide_title_bar = True)
