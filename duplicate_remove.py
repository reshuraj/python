a=raw_input("enter items : ")
dict={}
list=a.split(" ")
for i in list:
    if i in dict:
        break
    else:
        dict[i]=1
        print i

