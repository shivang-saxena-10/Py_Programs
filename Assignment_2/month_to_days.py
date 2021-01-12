x=int(input("Enter the numeric value of month : "))
if x<=7:
	if x==2:
		print("28")
	elif x%2!=0:
		print("31")
	else:
		print("30")
else:
	if x%2==0:
		print("31")
	else:
		print("30")
