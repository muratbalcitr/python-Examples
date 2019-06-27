file_text = open("tester_2.txt", "w", encoding="utf-8")
file_text.write("deneme edemefdşl e dededklekldelk e")

file_text.close()

# bulunan  dosya üzerine ekleme


file_text = open("tester_2.txt", "a", encoding="utf-8")
file_text.write("\n murat \n ahment \n ayşe \n ")

file_text.close()

# yöntem1
file_text = open("tester_2.txt", "r", encoding="utf-8")
for i in file_text :
    print(i, end="")
file_text.close()
# yöntem2
file_text = open("tester_2.txt", "r", encoding="utf-8")
icerik = file_text.read()
print("iiasidi", icerik)
file_text.close()

# readline fonk satır satır okur
file_text = open("tester_2.txt", "r", encoding="utf-8")

i = 0
while i < 2 :
    print(file_text.readline(), end="")
    i += 1
file_text.close()

# otomatik dosya kapatma
with open("tester_2.txt", "r", encoding="utf-8")as file :
    for i in file :
        print(i)

# seek() =imleci istediğimiz noktaya götürür, tell => dosya imleci hangi bytte olduğunu gösterir.

with open("tester_2.txt", "r", encoding="utf-8")as file :
    cursor = file.tell()
    cursor2 = file.seek(20)
    print(cursor)
    print(cursor2)
# ornek2
with open("tester_2.txt", "r", encoding="utf-8")as file :
    file.seek(5)
    icerik = file.read(10)
    print(icerik)

# r+ => hem okuma hem üstüne yazma sağlar
with open("tester_2.txt", "r+", encoding="utf-8")as file :
    file.seek(10)
    file.write("teststesetsete")
    print(file.read())
# yeni satır ekleme
with open("tester_2.txt", "a", encoding="utf-8")as file :
    file.write("murat balıcı\n")

with open("tester_2.txt", "r+", encoding="utf-8")as file :
    print(file.read())

# dosya başına ekleme
with open("tester_2.txt", "r+", encoding="utf-8")as file :
    icerik = file.read()
    icerik = "mehmet muetad\n" + icerik
    file.write(icerik)

with open("tester_2.txt", "r+", encoding="utf-8")as file :
    print(file.read())

#dosyanın herhangi bir yerine değer ekleme
with open("tester_2.txt", "r+", encoding="utf-8")as file :
    liste =file.readlines()
    print(liste)
    liste.insert(3,"murat balcı \n")
    file.seek(0)
    for i in liste:
        file.write(i)

with open("tester_2.txt", "r+", encoding="utf-8")as file :
    print(file.read())