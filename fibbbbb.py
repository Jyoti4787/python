n=int(input("n"))
a=1
b=1
c=0
for i in range(2,n):
    c=a+b
    a=b
    b=c
if(n==1 or n==2):
    print("1")
else:
    print(c)
