import sqlite3

conn = sqlite3.connect('shopping.sqlite')
cur = conn.cursor()

cur.execute('update tItems set need = 0')
conn.commit()
conn.close()
