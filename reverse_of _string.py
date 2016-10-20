a=raw_input("enter string : ")
if len(a)%4==0:
    print ''.join(reversed(a))
else:
    print a
