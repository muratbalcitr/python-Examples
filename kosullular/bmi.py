

print("************************************\n"
      "Vücutt Kitle İndexi\n"
      "************************")

boy = int(input("boyunuzu giriniz"))
kilo = int(input("kilonuzu giriniz"))

bmi = kilo/((boy/100)*(boy/100))

if(bmi<18.5):
    print("sonucunuc : {} => zayıf ".format(bmi))
elif(bmi>18.5 and bmi <= 25):
    print("sonucunuc : {} => normal ".format(bmi))
elif(bmi>25 and bmi<30 ):
    print("sonucunuc : {} => kilolu".format(bmi))
else:
    print("sonucunuc : {} => şişman ".format(bmi))