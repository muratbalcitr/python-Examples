

result = 4 in [1,2,3,4,4,4,2,2]
print(result)


liste =[1,3,5,7,9,11,13,15,17]
toplam =0
for eleman in liste:
    toplam += eleman
    print("eleman : {} toplamı : {} ".format(eleman,toplam))


liste2 = [(1,2),(3,4),(5,6),(7,8)]
for (i,j) in liste2:
    print("elamanlar 2 {},{}".format(i,j))


liste3 = [(1,2,4),(3,4,3),(5,6,1),(7,8,4)]
for (i,j,k) in liste3:
    print("elamanlar 3 =>  {}, {}, {}".format(i,j,k))

