s='azcbobobegghakl'

i=0
length=len(s)
max=0
while(i<length-1):
    c=0
    j=i
    while(s[i]<=s[i+1]):
        c+=1
        i+=1
        if(i==length-1):
            break
    if(c>max):
        max=c
        lower=j
        upper=i
    i+=1
sub=''
for k in range(lower,upper+1):
    sub+=s[k]
print("Longest substring in alphabetical order is: "+sub)
