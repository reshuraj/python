a=raw_input("enter a string seperated by comma: ")
dict={}
list=a.split(",")
list.sort()
for i in list:
    key=dict.keys()
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        print i

