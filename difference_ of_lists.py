a=raw_input("first list : ")
l1=list(a)
l1=a.split(" ")
#l1=list(a.split(" "))
b=raw_input("second list  : ")
l2=list(b)
l2=b.split(" ")
print l1
print l2
print set(l1)-set(l2)
