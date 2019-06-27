
def double(sayi):
    return sayi*2

liste = map(double, [1,2,3,4,5,6,7])
print(list(map(double, [1,2,3,4,5,6,7])))

liste2 = list(map(lambda x: x**2,(1,2,3,4,5)))
print(liste2)

list1=[1,2,3,4,5,6]
list2 =[2,4,6,8,10]
liste3 = list(map(lambda x,y : x*y,list1,list2))
print(liste3)





