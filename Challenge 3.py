number = int(input("Give me any number "))
a=1
factors=[]
while a<=number:
    if number%a==0:
        factors.append(a)
        a+=1
    else:
        a+=1
print(factors)