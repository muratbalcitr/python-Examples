
print("**************************\n"
      "Çarpım tablosu\n"
      "**************************")

for i in range(1,11):
    print("*******************")
    if i ==10 or i==9 or i==6 :
        print(i,".lar basamağı")
    else:
        print(i,".ler basamağı")
    for j in range(1,11):
        print("i*j => ",i*j)