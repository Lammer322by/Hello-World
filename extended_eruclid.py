def ext_gcd(a,b):
    if b == 0:
        return(1 , 0, a)
    x, y, d = ext_gcd(b, a%b)
    return(y, x-(a//b)*y, d)

print(ext_gcd(2717, 2405))
