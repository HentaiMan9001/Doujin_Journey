import sqlite3

class Database():
	_connection = sqlite3.connect('files/library.db')
	
	def add_book(self, book):
