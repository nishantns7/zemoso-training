def gcdRecur(a,b):
    if(b==0):
        return a
    else:
        return gcdRecur(b,a%b)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if(a>b):
    print(gcdRecur(a,b))
else:
    print(gcdRecur(b,a))
