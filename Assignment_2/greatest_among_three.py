x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=int(input("Enter third number :"))
if x>y and x>z:
	print("%d is greatest "%x)
elif y>x and y>z:
	print("%d is greatest "%y)
else:
	print("%d is greatest "%z)
