"""
def inc(x):
    return x + 1

f = inc

#prediction: 11
print f(10)

#(lambda (a b) (+ a b))
#adds a and b

#(define foo (lambda (a b) (+ a b)))
#defines foo as a function which takes a and b, and then adds them

def h(x):
    return lambda y: x + y

print h(1)
print h(2)
print h(1)(3)
print h(2)(5)

b=h(1)
print b
print b(2)

def f(x):
    def g(y):
        return x + y
    return g
print f(1)
print f(2)
print f(1)(3)
print f(2)(5)
"""
def repeat(x):
    def r(y):
        t = ""
        for l in range(y):
                t+=x
        return t
    return r

r1=repeat('hello')
r2=repeat('goodbye')

print r1(2)
print r2(2)
print repeat("cool")(3)
