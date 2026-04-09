from sympy import *

x = symbols('x')

func1 = simplify(input("Enter the expression of the curve\n"))
func2 = simplify(input("Enter another expression of the curve\n"))

function = func1-func2

a = input("enter lower limit for the first expression:\n ")
a = int(a)
b = input("enter upper limit for the first expression:\n ")
b = int(b)

area = integrate(function, (x,a,b))
print("area between the curve: ", area)
