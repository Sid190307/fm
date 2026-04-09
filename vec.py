x='y'

n = int(input("Enter the no. of Elements you want to enter in the Vector:"))
v = []
for i in range(n):
    a = int(input("Enter the elements of the first vector:"))
    v.append(a)

print()

w = []
for i in range(n):
    b = int(input("Enter the elements of the second vector:"))
    w.append(b)

while x=='y':
    print("\nMenu")
    print("1.Addition of two Vectors")
    print("2.Subtraction of two Vectors")
    print("3.Saclar Multiplication")
    print("4.Dot Product of two Vectors")
    print("5.Negation of vectors")
    print()
    ch= int(input("Enter the choice"))

    def add (v,w,n):
        return [ v[i]+w[i] for i in range(n)]

    def sub (v,w,n):
        return [ v[i]-w[i] for i in range(n)]

    def scalar_multi (alpha, v, n):
        return [ alpha*v[i] for i in range(n)]

    def dot_product (v,w,n):
        return sum([ v[i]*w[i] for i in range(n)])

    def negation (v,n):
        return [ v[i]*(-1) for i in range(n)]

    if ch == 1:
        print("The addition of two vectors is: ", add(v,w,n))
       
    elif ch == 2:
        print("The subtraction of two vectors is: ", sub(v,w,n))
    
    elif ch == 3:
        m = int(input("Enter a number to multiply with the vector: "))
        print("The scalar multiplication of the vector ",v," is: ", scalar_multi(m,v,n))

    elif ch == 4:
        print("The dot product of two vectors is: ", dot_product(v,w,n))

    elif ch == 5:
        print("The negation of the vector ",v," is: ", negation(v,n))

    else:
        print("Enter the valid choice")
    print()

    x = str(input("Do you wish to continue (y/n): ")).lower()
