def palin(b):
    r=''.join(reversed(b))
    if b==r:
        print "string is palindrom"
    else:
        print "not palindrom"
a=raw_input("enter a string : ")
palin(a)
