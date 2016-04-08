import time

t= time.time()
t2 = time.time()

def wrapper( f ):
    def inner( *arg ):
        t = time.time()
        q = f( *arg )
        t2 = time.time()
        print f.func_name + ":\ntime:" + str(t2-t) + "\n"
        return q
    return inner

@wrapper
def foo(*x):
    print x
    
foo(10,12345342,2345,3451)
