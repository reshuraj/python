def sort(a):
    l1=a.split("-")
    l1.sort()
    st=""
    for i in l1:
        if st!="":
            st=st+'-'+i
        else:
            st=i
    print st
a=raw_input("enter hyphen seperated words : ")
sort(a)

