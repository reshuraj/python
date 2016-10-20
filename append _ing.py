a=raw_input("enter the string : ")
if (a.endswith("ing",0,len(a))):
    print a.replace("ing","ly")
else:
    print a+"ing"
