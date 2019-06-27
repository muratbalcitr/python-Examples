import sys


def kok_bulma(a, b, c) :
    delta = b ** 2 - 4 * a * c
    if delta < 0 :
        print("reel kök yoktur")
    else :
        x1 = (-b - delta ** 0.5)/(2*a)
        x2 = (-b + delta ** 0.5)/(2*a)
        return x1,x2
if len(sys.argv)==4:
   print("kök bulma", kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("lütfen doğru değerler giriniz")
    sys.stderr.flush()

