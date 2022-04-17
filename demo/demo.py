import sqlite3
from tabulate import tabulate

import sys

#temp memory
#connection = sqlite3.connect(':memory:')

def show_all():
    #create a db
    connection = sqlite3.connect('demo.db')

    #cursor
    c = connection.cursor()

    #creating a table
    '''
    c.execute("""CREATE TABLE account (
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        location TEXT,
        password TEXT
    )
        """)


    #creating a list to execute many accounts in one go
    many_costumer = [
                        ('jb034', 'John', 'Bill', 'johnbill@hotmail.com', 'Ottawa, Canada', 'its@beautifulday'),
                        ('yoyo03', 'Yanik', 'Noak', 'noah.yanik@yahoo.com', 'Ottawa, Canada', 'irongold$$$'),
                        ('moonrea', 'Luna', 'Vera', 'luna@vera.com', 'Rio, Brazil', 'imoonheart'),
                        ('paleo', 'Greg', 'Bran', 'gregbran@yourservice.com', 'Pluto, Universe', 'weirdoME'),
                        ('crate768', 'Art', 'Tistic', 'artistic@gmail.com', 'Bali, Indonesia', 'creative@'),
                    ]

    #insert data into the table
    #will execute many                  (?,) indicator of the 7 columns
    c.executemany("INSERT INTO account VALUES (?,?,?,?,?,?)", many_costumer)

    print("\nSuccess!")
    '''

    c.execute("SELECT rowid, * FROM account")

    #print data
    result = c.fetchall()

    for data in result:
            #item = [data[0] , data[1] , data[2] , data[3] , data[4] , data[5]]
            #print (tabulate([data[0] , data[1] , data[2] , data[3] , data[4] , data[5]], headers=["USERNAME", "FIRSTNAME", "LASTNAME", "EMAIL", "LOCATION", "PASSWORD"]))
        print (data[0] , " | " , data[1] , " | " ,  data[2] ," | " , data[3] , " | " ,  data[4] , " | ",  data[5])





    #commmit our command
    connection.commit()


    try:
        print("\nConnected...")

    except Error as e:
        print (e)

    #close connection to the db
    connection.close()
    print("\nConnection Closed...")


#adding new record to the table
def add_one(username, first_name, last_name, email, location, password):
    connection = sqlite3.connect('demo.db')
    c = connection.cursor()

    c.execute("INSERT INTO account VALUES (?,?,?,?,?,?)", (username, first_name, last_name, email, location, password))

    connection.commit()
    try:
        print("\nConnected...")
    except Error as e:
        print (e)
    connection.close()
    print("\nConnection Closed...")

def delete_one(id):
    connection = sqlite3.connect('demo.db')
    c = connection.cursor()

    c.execute("DELETE from account  WHERE rowid = (?)", id)

    connection.commit()
    try:
        print("\nConnected...")
    except Error as e:
        print (e)
    connection.close()
    print("\nConnection Closed...")