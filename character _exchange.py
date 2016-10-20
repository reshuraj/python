a=raw_input("enter first string : ")
b=raw_input("enter second strin : ")
c,d=a,b
print a,b
a=a[:2]
b=b[:2]
print b[:2]+c[2:],a[:2]+d[2:]
