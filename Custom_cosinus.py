from math import cos

CONST = 100

def cosinus(x):
    res = 0
    x_st = 1
    n_factorial = 1
    
    for n in range(0,CONST):
        if n == 0:
            res+=1
        else:
            x_st *= x**2
            if n == 1:
                n_factorial = 2
            else:
                n_factorial *= (n+1) * (n+2)
            res+=((-1**n)/n_factorial) * x_st
    return res

print(cosinus(0.75))
print(cos(0.75))
