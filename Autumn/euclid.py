def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)


PASSED = 0

from random import randint

for i in range(100000):

    a = randint(-1000, 10000000)
    b = randint(-1000, 10000000)
    d = gcd(a,b)

    if(gcd(a/d, b/d) == 1):
        continue
    else:
        print("Function had failed on numbers {} and {}", format(a,b))
        PASS = -1

if PASSED == 0:
    print("Success!!")
