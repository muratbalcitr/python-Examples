



print("************************************"
      "kullanıcı girişi"
      "************************************")

sys_username = "murat"
sys_parola ="12345"

inp_kullanici_Adi = input("kullanıcı adı : ")
inp_parola =input("parola: ")

if(sys_username == inp_kullanici_Adi and sys_parola !=inp_parola):
    print("parola hatalı")
elif(sys_username != inp_kullanici_Adi and sys_parola ==inp_parola):
    print("kullanıcı adı hatalı")
elif(sys_username != inp_kullanici_Adi and sys_parola !=inp_parola):
    print("kullanıcı adı ve parola hatalı")
else:
    print("başarıyla giriş yapıldı")