import numbers
import math

class QuaternionTypeError(TypeError):
    pass

class Quaternion():
    _isReal = False
    def __init__(self, re, i, j, k):
        if (isinstance(re, numbers.Number)):
            self.re = re
        else:
            raise QuaternionTypeError("Ошибка инициализации")
        if (isinstance(i, numbers.Number)):
            self.i = i
        if (isinstance(j, numbers.Number)):
            self.j = j
        if (isinstance(k, numbers.Number)):
            self.k = k
        if(self.i == 0 and self.j == 0 and self.k == 0):
            self._isReal == True
        else:
            self._isReal == False


    def __abs__(self):
        return (self.re**2 + self.i**2 + self.j**2 + self.k**2) ** 0.5


    def __invert__(self):
        return(Quaternion(self.re, -self.i, -self.j, -self.k))


    def __neg__(self):
        return(Quaternion(-self.re, -self.i, -self.j, -self.k))


    def __eq__ (self, other):
        if(isinstance(other, Quaternion)):
            if(self.re == other.re and self.i == other.i and self.j == other.j and self.k == other.k):
                return True        
            else:
                return False
        elif(isinstance(other, numbers.Number)):
            if (self._isReal):
                if (self.re == other):
                    return True
                else:
                    return False
        else:
            raise QuaternionTypeError("Неккоректное сравнение")


    def __add__ (self, other):        
        if (isinstance(other, numbers.Number)):
            return(Quaternion(self.re+other, self.i, self.j, self.k))
        
        elif (isinstance(other, Quaternion)):
            return(Quaternion(self.re + other.re, self.i + other.i, self.j + other.j, self.k + other.k))
        
        else:
            raise QuaternionTypeError("Can't add " + type(other) + " to the Quaternion")
        
    
    def __sub__(self, other):
        return(self + (-other))
    

    def __radd__(self, other):
        return(self + other)
    

    def __rsub__(self, other):
        return((-self) + other)
    

    def __mul__(self, other):
        if(isinstance(other, numbers.Number)):
            return(Quaternion(self.re*other, self.i*other, self.j*other, self.k*other))
        elif(isinstance(other, Quaternion)):
            out_re = self.re * other.re - self.i*other.i - self.j*other.i - self.k*other.k
            out_i = self.re*other.i + self.i*other.re + self.j*other.k - self.k*other.j
            out_j = self.re*other.j - self.i*other.k + self.j*other.re + self.k*other.i
            out_k = self.re*other.k + self.i*other.j - self.j*other.i +self.k*other.re
            return(Quaternion(out_re, out_i, out_j, out_k))
        

    def __rmul__(self, other):
        if(isinstance(other, numbers.Number)):
            return(self*other)
        elif(isinstance(other, Quaternion)):
            out_re = other.re * self.re - other.i*self.i - other.j*self.i - other.k*self.k
            out_i = other.re*self.i + other.i*self.re + other.j*self.k - other.k*self.j
            out_j = other.re*self.j - other.i*self.k + other.j*self.re + other.k*self.i
            out_k = other.re*self.k + other.i*self.j - other.j*self.i +other.k*self.re
            return(Quaternion(out_re, out_i, out_j, out_k))


    def __truediv__(self, other):
        if(isinstance(other, numbers.Number)):
            return(Quaternion(self.re/other, self.i/other, self.j/other, self.k/other))
        elif(isinstance(other, Quaternion)):
            return(self*(~other/abs(other)))
        
    
    def __str__(self):
        if (self._isReal):
            return(self.re)
        else:
            res = ''
            if (self.re!=0):
                res+=str(self.re)
            if (self.i!=0):
                if (self.re!=0):
                    res+=' + '
                res+=str(self.i)+'*i '
            if (self.j!=0):
                if (self.re!=0 or self.i!=0):
                    res+=' + '
                res+=str(self.j)+'*j '
                if (self.k!=0):
                    res+=' + '
            if (self.k!=0):
                res+=str(self.k)+'*k '
            return res
    

a = Quaternion(2,2,2,2)
b = Quaternion(0,1,0,1)

print(abs(a))
print(str(a*b))
print(str(a/b))
print(a=='c')
print(a-b)

