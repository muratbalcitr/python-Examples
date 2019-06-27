import random as rnd
import time

print("********************** \n sayi tahmin oyunu\n"
      "1-40 arasında sayıyıtahmin edin.")
rastgele_sayi =rnd.randint(1,40)

tahmin_hakki =7
while True:
      tahmin = int(input("sayi giriniz 1-40 arası : "))

      if tahmin > rastgele_sayi:
            print("bilgiler sorgulanıyor...")
            time.sleep(1)
            print("tahmin ettiğiniz sayı sonuc değerinden büyüktür")
            tahmin_hakki -=1

      elif tahmin < rastgele_sayi:
            print("bilgiler sorgulanıyor...")
            time.sleep(1)
            print("tahmin ettiğiniz sayı sonuc değerinden küçüktür")
            tahmin_hakki -=1
      else:
            print("doğru bildiniz")
            tahmin_hakki -=1
            break
      if tahmin_hakki == 0:
            print("maalesef bilemediniz... :( :( :(")
            break