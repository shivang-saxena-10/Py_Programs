a=int(input("Enter the coefficient of x^2 : "))
b=int(input("Enter the coefficient of x : "))
c=int(input("Enter the third coefficient : "))
if b**2-(4*a*c)>0:
	print("Two distinct real roots")
elif b**2-(4*a*c)<0:
	print("No real roots")
else:
	print("Two equal real roots")
