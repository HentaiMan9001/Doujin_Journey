class test:
	def __init_(self):
		self._a = None
		self._b = None
	
	@property
	def info(self, info):
		''' this is the 'a' property '''
		return self._a, self._b
		
	@info.setter
	def info(self, info):
		self._a, self._b = info
	
	@info.getter
	def info(self):
		return self._a, self._b
