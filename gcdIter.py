def gcdIter(a,b):
    if(a>b):
        for i in range(b,0,-1):
            if(a%i==0 and b%i==0):
                return i
    else:
        for i in range(a,0,-1):
            if(a%i==0 and b%i==0):
                return i

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(gcdIter(a,b))
