from sympy import *

x = symbols('x')

func = input("Enter the expression of the curve\n")
function = sympify(func)

a = input("enter lower limit:\n ")
a = int(a)
b = input("enter upper limit:\n ")
b = int(b)

derivative = diff(func,x)
print("Derivative = ", derivative)
area = integrate(func, (x,a,b))
print("area under the curve: ", area)
