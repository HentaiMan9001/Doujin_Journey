import sqlite3

conn = sqlite3.connect('library.db')

conn.execute('CREATE TABLE test(page INT AUTO_INCREMENT, title TEXT)')

