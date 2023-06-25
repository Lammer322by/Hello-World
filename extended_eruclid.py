def ext_gcd(a,b):
    if b == 0:
        return(1 , 0, a)
    x, y, d = ext_gcd(b, a%b)
    return(y, x-(a//b)*y, d)

PASSED = 0

from random import randint

for i in range(100000):
    a = randint(-1000, 1000000)
    b = randint(-1000, 1000000)
    x, y, d = ext_gcd(a,b)
    if(x*a + y*b == d):
        continue
    else:
        print("Function had failed on numbers {} and {}", format(a,b))
        PASS = -1

if PASSED == 0:
    print("Success!!")