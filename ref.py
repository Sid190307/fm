def reflexive(s,relation):
    ns = { (a,b) for a in s for b in s if a==b}
    if R>=ns:
        print("it is reflexive")
    else:
        print("it is not reflexive")

A = {1,2,3}
R = {(1,1),(2,2),(3,3)}
print("the given relation ",R)
reflexive(A,R)
