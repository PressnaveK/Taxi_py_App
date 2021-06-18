import sqlite3
conn = sqlite3.connect('TBS.db')
c = conn.cursor()
for x in c.execute("SELECT Username FROM Driver "):
   print( x[0])


