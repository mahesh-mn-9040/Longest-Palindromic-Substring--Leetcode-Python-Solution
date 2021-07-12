s=input()

res=""
reslen=0

for i in range(len(s)):
    #for odd length
    l, r=i, i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if (r-l+1)>reslen:
            res=s[l:r+1]
            reslen=r-l+1
        l-=1
        r+=1
    
    
    #for Even lenght
    l, r=i, i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        if (r-l+1)>reslen:
            res=s[l:r+1]
            reslen=r-l+1
        l-=1
        r+=1
print(res)  
