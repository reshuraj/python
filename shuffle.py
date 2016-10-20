import random
a=raw_input("enter items : ")
l=list(a)
l=a.split(" ")
random.shuffle(l)
print l
