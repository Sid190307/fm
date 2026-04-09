def symmetric(s,relation):
    for (a,b) in relation:
        if (b,a) not in relation:
            print("It is not symmetric")
            return
    print("It is symmetric")

A={1,2,3}
R = { (1,1),(1,2),(1,3),(2,1),(3,1) }
print("the given relation ",R)
symmetric(A,R)
