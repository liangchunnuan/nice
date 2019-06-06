import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE data
       (company           INT    NOT NULL,
       COUNT(company)         INT    NOT NULL,
       SUM(weight)         INT    NOT NULL,
       SUM(weight*price)         INT    NOT NULL);''')
print("Table created successfully")
print("Table created successfully2222")
print("Table created successfully33333")
conn.commit()
conn.close()
