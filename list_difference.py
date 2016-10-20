a=raw_input("first list : ")
l1=list(a)
l1=a.split(" ")
b=raw_input("second list  : ")
l2=list(b)
l2=b.split(" ")
print l1
print l2
k=[]
for i  in range(0,len(l1)):
    c=int(l1[i])-int(l2[i])
    k.append(c)
print k
