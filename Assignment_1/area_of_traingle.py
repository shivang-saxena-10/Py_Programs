a=int(input("Enter the 1st side of the triangle : "))
b=int(input("Enter the 2nd side of the triangle : "))
c=int(input("Enter the 3rd side of the triangle : "))
s=(a+b+c)/2  #semi-perimeter
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is :",area)
