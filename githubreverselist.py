x=[]
a=0
while a<5:
    elements=input(f"enter elements{a+1} ")
    x.append(int(elements))
    a+=1
print((x))


y=[]

for i in range(len(x)-1,-1,-1):

    y.append(x[i])

print(y)






