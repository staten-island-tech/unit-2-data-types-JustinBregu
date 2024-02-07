number1 = int(input('Give me a number'))
a=1
factors1=[]
while a<=number1:
    if number1%a == 0:
        factors1.append(a)
        a+=1
    else:
        a+=1
print(factors1)

number2 = int(input("Give me another number "))
a=1
factors2=[]
while a<=number2:
    if number2%a==0:
        factors2.append(a)
        a+=1
    else:
        a+=1
print(factors2)

for factors in factors1:
    if number1%a == 1:
        factors1.append(a)
        a+=1


print(factors)