
import sqlite3

con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(ISIM TEXT,YAZAR TEXT, YAYIN_EV TEXT,SAYFA SAYISI INT)")
    con.commit()
create_table()

def Insert_Into():
    cursor.execute("Insert into kitaplik values('istanbul hatırası','ahmet ümit','everest',561)")
    con.commit()
Insert_Into()

def input_Insert(kitaplik,yazar_adi,yayin_evi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik values(?,?,?,?)",(kitaplik,yazar_adi,yayin_evi,sayfa_sayisi))
    con.commit()

kitaplik = input("kitap adını giriniz => ")
yazar_adi = input("yazar adı giriniz => ")
yayin_evi= input("yayın evi giriniz => ")
sayfa_sayisi = int(input("sayfa sayısı giriniz => "))

input_Insert(kitaplik,yazar_adi,yayin_evi,sayfa_sayisi)




def data_select() :
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print(liste)


data_select()
con.close()



