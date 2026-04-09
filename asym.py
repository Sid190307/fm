def antisymmetric(relation):
    for (a,b) in relation:
        if (b,a) in relation and a!=b:
            print("It is not anti-symmetric")
            return
    print("It is anti-symmetric")

A={1,2,3}
R = { (1,1), (1,2), (1,3), (2,1)}
print("the given relation: ",R)
antisymmetric(R)
