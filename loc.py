from sympy import *

x = symbols('x')

func = input("Enter the expression of the curve\n")
function = sympify(func)

a = input("enter lower limit:\n ")
a = int(a)
b = input("enter upper limit:\n ")
b = int(b)

derivative = diff(function,x)
print("Derivative = ", derivative)

inte = sympify(sqrt(1 + (derivative)**2))

length = integrate(inte, (x,a,b))
print("length of the curve: ", length.evalf())
