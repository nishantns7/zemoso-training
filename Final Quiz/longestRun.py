def longestRun(L):
    longest=0
    counter=1
    for i in range(len(L)-1):
        if L[i]<=L[i+1]:
            counter+=1
        else:
            counter=1
        if counter>longest:
            longest=counter
    print(longest)
