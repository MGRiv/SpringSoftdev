def union(l1,l2):
    r = setdifference(l1,l2)
    return r + l2

def intersection(l1,l2):
    return [x for x in l1 if x in l2]

def setdifference(l1,l2):
    return [x for x in l1 if x not in l2]

def symmetricdifference(l1,l2):
    r1 = setdifference(l1,l2)
    r2 = setdifference(l2,l1)
    return r1 + r2

def cartesianproduct(l1,l2):
    return [(x,y) for x in l1 for y in l2]

print symmetricdifference([1,2,5],[1,6,3541234])
