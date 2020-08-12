#from strings import string

__all__ = ['App']
import api
from scripts import *
from app_ui import *
	
class App(object):
	def __setattr__(self,name,value):
		self.__dict__[name] = value
		
	def __getattribute__(self,name):
		return  object.__getattribute__(self,name)
		
	def initialize(self):
		self.load_reader()
		self.prepare_client()
		self.load_main_menu()
		
	def prepare_client(self):
		self.client = api.Api_Controller(self)
		
	def load_reader(self):
		self.reader = reader(self)
		
	def load_main_menu(self):
		self.nav = nav_bar(self)
		self.menu_bar = menu_bar(self)
		self.search_bar = input_ui(self)
		self.Menu = Menu(self)
		self.main_view = Main_View(self)
		
	def run(self):
		self.main_view.present('fullscreen',hide_title_bar = True)
