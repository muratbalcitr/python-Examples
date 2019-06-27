# iki listeyi ziplemektedir.

liste1=[1,2,3,4,5,6,7,8]
liste2 = [2,3,4,5,6,8,99,0,7]
liste3 = list(zip(liste1,liste2))
print(liste3)

# liste üzerinde gezinme
a_list =["a","b","c","d"]
b_list=[1,2,3,4]

for i,j in zip(a_list,b_list):
    print("i => ",i,"j => ",j)



