d1={1:'a',2:'b'}
c=raw_input("enter a key : ")
c2=raw_input("enter a value : ")
d=dict(zip(c,c2))
d1.update(d)
print d1
