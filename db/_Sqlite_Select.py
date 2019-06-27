import sqlite3

con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()

def data_select() :
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

data_select()
