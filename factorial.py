def myfact(n):
    if n==1:
        return n 
    else:
        return n*myfact(n-1)


#num=int(input("Enter your number: "))
num=5


if num<0:
    print('Factorial not possible')
elif num==0:
    print("Factorial is: 1")

else:
    print('The Factorial is:', myfact(num))