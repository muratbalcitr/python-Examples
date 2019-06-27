

liste = [12,1,2,3,4,5]

liste2 = [i for i in liste]

print(liste2)

print("-------------------------------")

liste3 = [i/2 for i in liste]

print(liste3)

print("-----------------------")

liste4 =[(1,2),(3,4),(5,89)]

list5 = [i*j for i,j in liste4]

print(list5)

print("-----------------------")


list = [[1,2,3,4,5,6],[1,2,3],[9,8,7]]
list6 = []
for i in list:
    for j in i:
        list6.append(j)
print(list6)

list_comp = [x for i in list for x in i]
print(list_comp)