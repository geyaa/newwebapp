import sqlite3

#temp memory
#connection = sqlite3.connect(':memory:')

#create a db
connection = sqlite3.connect('db_paqt.db')

#cursor
c = connection.cursor()

#creating a table
'''
c.execute("""CREATE TABLE account (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    location TEXT,
    password TEXT
)
    """)
'''

#insert data into the table
#c.execute("INSERT INTO account VALUES ('2', 'yoyo03', 'Yanik', 'Noak', 'noah.yanik@yahoo.com', 'Ottawa, Canada', 'irongold$$$')")

print("\nSuccess!")

c.execute('''SELECT * from account''')

#print data
result = c.fetchall()
print(result)

#commmit our command
connection.commit()

try:
    print("\nConnected...")

except Error as e:
    print (e)

connection.close()