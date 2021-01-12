import cmath
x=eval(input("Enter a complex number : "))
print(x.real , "is greater") if (x.real > x.imag) else print(x.imag, "is greater")
