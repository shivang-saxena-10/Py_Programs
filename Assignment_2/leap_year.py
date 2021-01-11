x=int(input("Enter the year : "))
if x%4==0 or x%100==0 or x%400==0:
	print("The year is a leap year")
else:
	print("The year is not a leap year")
