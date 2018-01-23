s='azcbobobegghakl'

i=0
l=len(s)
max=0
while(i<l-1):
    c=0
    j=i
    while(s[i]<=s[i+1] and i<l-1):
        c+=1
        print(i)
        i+=1
    if(c>max):
        max=c
        l=j
        u=i
    i+=1
sub=''
for i in range(l,u+1):
    sub+=s[i]
print("Longest substring in alphabetical order is: "+sub)
