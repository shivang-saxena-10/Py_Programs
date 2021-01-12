l1=[]
r=1
per=0
summation=0
if(True):
	for i in range(1,6):
		a=int(input("Enter %d number : "%(i)))
		l1.append(a)
	for i in l1:
		if i>33:
			pass
		else:
			print("Result : FAIL")
			r=0
if r==1:
	print("Result : PASS")
	for i in l1:
		summation+=i
	per=summation/5
	print("The percentage is : %f percent"%(per))
	if per>=60:
		print("YaY !! You got first division")
	elif per>38 and per<60:
		print("Umm !! You got second division")
	else:
		print("You got third division")
