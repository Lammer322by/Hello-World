p = int(input())

def factorial(n):
    res = 1
    while n>0:
        res*=n
        n-=1
    return res

def vilson(n):
    if (factorial(n-1)+1)%n == 0:
        return True
    else:
        return False

if vilson(p):
    print("Simple")
elif(p==1):
    print("Equals 1")
else:
    print("Not simple")
