def count(a):
    d=0
    c=0
    for i in a:
        b=i.isalpha()
        g=i.isdigit()
        if b==1:
            c+=1
        elif g==1:
            d+=1
        else:
            pass
    print "count of letters : ",c
    print "count of digits : ",d
a=raw_input("enter a string : ")
count(a)
