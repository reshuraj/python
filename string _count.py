a=raw_input("enter a string : ")
dict={}
lst=a.split(" ")
for i in lst:
    key=dict.keys()
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print dict
