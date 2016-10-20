d={1:'a',2:'b',3:'a'}
r={}
for key,value in d.items():
    if value not in r.values():
        r[key]=value
print r
