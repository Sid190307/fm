def transitive(relation):
    for (a,b) in relation:
        for (c,d) in relation:
            if b==c:
                if (a,d) not in relation:
                    print("It is not transitive")
                    return
    print("It is transitive")

A = {1,2,3}
R = { (1,1), (1,2), (1,3), (2,3) }
print("The given relation is : ",R)
transitive(R)
