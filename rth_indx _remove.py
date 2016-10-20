a=raw_input("enter the string : ")
r=input("enter an index : ")
for i in range(0,len(a)):
    if a[i]==a[r]:
        print a.replace(a[r],"")
