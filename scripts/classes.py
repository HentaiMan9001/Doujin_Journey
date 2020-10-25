__all__ = ['Book','Settings']

class Settings:
	def __init__(self):
		import os
		cwd = os.getcwd()
		self.file_path =  os.join(cwd,'files','settings.json')
		self.load_settings_file()
		
	def load_settings_file(self):
		import json
		with open(self.file_path, 'r', encoding = 'utf-8') as file:
			settings = json.load(file)
			file.close()
		self.__dict__.update(settings)
	
	def save_settings_file(self):
		import json
		with open(self.file_path, 'w', encoding = 'utf-8') as file:
			json.dump(self.__dict__)
			file.close()



class Indexer():
	def __init__(self):
		self.debug = 0
		self.count = 0
		self.max = 0
		self.allowed = 0
		self.image_list = list()
	def reset(self):
		self.debug = 0
		self.count = 0
		self.max = 0
		self.allowed = 0
		self.image_list = []
	def set(self,max):
		
		self.max = max
		if self.debug == 1:
			self.allowed = self.max
	def append(self,image):
		self.image_list.append(image)
		self.allowed = len(self.image_list)-1
		
	def next(self):
		
		if self.count < self.allowed:
			self.count += 1
		elif self.count == self.allowed:
			pass
		if self.debug == 1:
			return self.count
			
	def previous(self):
		if self.count > 0:
			self.count -= 1
		elif self.count == 0:
			pass
		if self.debug == 1:
			return self.count
	def index(self):
		item = self.image_list[self.count]
		return item
	def get(self):
		info = (len(self.image_list),self.max)
		return info
