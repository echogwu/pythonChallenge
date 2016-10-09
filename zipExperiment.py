#Actually this is a function definition for built-in function zip
#I changed the name of zip to zz

def zz(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    print iterables
    iterators = [iter(it) for it in iterables]
    while iterators:
        print "right after the while"
        print iterators
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
            print("result: %s" % result)
        yield tuple(result)
        print "right after a yield"

x=[1,2,3]
y=['a','b','c']
print list(zz(x,y))



