l1=[]
r=1
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

