def add(a,b=0):
    c=a+int(b)
    print "result is",c
def sum(a,b=0):
    c=a+int(b)
    if a:
        return 0
    print "result is",c
    return c

def list(a,b=0):
    c=a+int(b)
    if a:
        return 0,-1
    print "result is",c
    return c,a
add(1,0)
add(1,3)
add(1)
c = sum(100,100);
print "c is:",c

va,vb = list(100,100);
print "va  is:",va,"vb is:" , vb
