n=int(input("enter the number of elements:"))
a=0
b=1
sum=0
print(b)
for i in range(0,n+1):
    a = b
    b = sum
    sum = a + b
    print(sum)
