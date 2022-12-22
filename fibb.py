n=int(input("n"))

a=1
b=1
c=2
for i in range(2,n):
    a=b
    b=c
    c=a+b 
    print(c)