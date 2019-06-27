

print("-------------------------- \n"
      "Fibonacci serisi \n"
      "---------------------------")

a = 1
b = 1
count = 0
fibo_list_while = [a,b]

while count<10:
    a,b = b,a+b
    print("a : ",a,"b : ",b)
    fibo_list_while.append(b)
    count+=1
print("while ile yazılım : ",fibo_list_while)

a =1
b= 1
fibo_list2_for = [a,b]
for i in range(10):
    a,b = b,a+b
    print("a : {}, b : {}".format(a,b))
    fibo_list2_for.append(b)
print("for ile yazılım :",fibo_list2_for)