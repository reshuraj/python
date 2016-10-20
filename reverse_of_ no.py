n=input("enter the no. : ")
a=0
while (n!=0):
    a=a*10
    a=a+n%10
    n=n/10
print a
