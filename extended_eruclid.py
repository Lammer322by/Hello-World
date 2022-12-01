def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(12,18))

def ext_gcd(a,b):
    if b == 0:
        return(1 , 0, a)
    x, y, d = ext_gcd(b, a%b)
    return(y, x-(a//b)*y, d)

print(ext_gcd(25, 11))
