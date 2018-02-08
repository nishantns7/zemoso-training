s='eaipgonaipnpbobaenopigbneaipbobobaefuibh'

i=1
l=len(s)
c=0
while(i<l-1):
    if (s[i-1]=='b' and s[i]=='o' and s[i+1]=='b'):
        c+=1
    i+=1
print("Number of times bob occurs is: "+ str(c))
