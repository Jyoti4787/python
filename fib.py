#higher order function ----- map function
str=["computer", "science", "student"]
print(list(map(lambda x:x.upper(),str)))
list1=[]
for x in str :
    list1.append(x.upper())
print(list1)