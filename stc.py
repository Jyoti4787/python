Number = int(input("Enter the number : "))
def fibonacci(Num):
    if(Num==0):
        return 0
    elif(Num==1):
        return 1
    else:
         return (fibonacci(Num-1) +  fibonacci(Num-2));
for j in range(0,Number):
    f = fibonacci(j)
    print(f)