

print("************ \n "
      "kullanıcı girişi \n"
      "*****************")

sys_username = "murat"
sys_parola = "12345"
login_count =3
while(True):
    username = input("username : ")
    parola =input("parola : ")
    if(username != sys_username and parola == sys_parola ):
        print("hatalor username")
        login_count-=1

    elif (username == sys_username and parola != sys_parola):
        print("hatalı parola")
        login_count-=1

    elif (username != sys_username and parola != sys_parola):
        print("error username and password ")
        login_count -= 1

    else:
        print("login is succesfully")

    if login_count == 0 :
        print("3 error login. program exiting")
        break