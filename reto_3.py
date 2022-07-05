a= list(map(int, input().split(" ")))
b=1
c=str()
d=str()
j=0
for i in a:
    if j>0 and a[j-1]==i:
        b +=1      
    if j==0:
        d +=str(i)+" "    
    elif a[j-1]!=i:
        c +=str(b)+" "
        d +=str(i)+" "
        b=1
    if j==len(a)-1:
        c +=str(b)+" "
    j+=1
print(d)
print(c)


#2 2 5 5 5 5 5 5 2 6 6 6 6 4 4 6 6 6 5 6 6 6 6
#2 5 2 6 4 6 5 6
#2 6 1 4 2 3 1 4