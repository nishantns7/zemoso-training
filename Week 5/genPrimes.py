def genPrimes():
    n=2
    while True:
        count=0
        for i in range(1,n//2+1):
            if n%i ==0:
                count+=1
        if count<2:
            yield n
        n+=1
