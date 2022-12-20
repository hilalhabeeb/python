class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return self.length+self.breadth
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
o=rectangle(l,b)
x=o.area()
y=o.perimeter()
print("arae of rectanle:",x)
print("perimeter of rectangle:",y)

l1=int(input("enter the length:"))
b1=int(input("enter the breadth:"))
o1=rectangle(l1,b1)
a=o1.area()
print("arae of rectanle",a)

if(x>a):
    print("first rectangle is greater than second")
elif(x==a):
    print("have same length")
else:
    print("second rectangele is greater than first")

