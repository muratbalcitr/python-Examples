

a = int(input("sayı 1 => "))
b = int(input("sayı 2 => "))
c = int(input("sayı 3 => "))
enb =0
liste = [a,b,c]
count =0
lent = len(liste)
while(count<lent):
    if(liste[count] > enb):
        enb = liste[count]
    count+=1
print(enb)