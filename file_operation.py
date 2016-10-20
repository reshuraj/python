fp=open("simple.txt","w+",0)
fp.write("this is python")
d=fp.read()
print d
e=fp.read(10)
print e
fp.close()
