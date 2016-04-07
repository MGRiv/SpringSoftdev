def union(l1,l2):
    r = setdifference(l1,l2)
    for x in l2:
        r.append(x)
    return r

def intersection(l1,l2):
    return [x for x in l1 if x in l2]

def setdifference(l1,l2):
    return [x for x in l1 if x not in l2]

def symmetricdifference(l1,l2):
    r1 = setdifference(l1,l2)
    r2 = setdifference(l2,l1)
    for x in r2:
        r1.append(x)
    return r1

def cartesianproduct(l1,l2):
    return [(x,y) for x in l1 for y in l2]

print union([1,2,5],[1,6,3541234])
