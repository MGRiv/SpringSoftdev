import time

def wrapper( f ):
    t = time.time()
    def inner( *arg ):
        print f.func_name + ":"
        return f( *arg )
    t2 = time.time() - t
    print "time:" + str(t2)
    return inner

@wrapper
def foo(*x):
    print x
    
foo(10,12345342,2345,3451)
