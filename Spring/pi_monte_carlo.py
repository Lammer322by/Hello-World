from random import uniform
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def monte_carlo(n):
    x = 0 
    y = 0
    inners = 0
    Pi = 0

    size = 1000000
    set_x = []
    set_y = []
    set_x_in = []
    set_y_in = []
    for i in range(n):
        x = uniform(0,size)
        y = uniform(0,size)
        if sqrt(x**2 + y**2)<=size:
            inners+=1
            set_x_in.append(x)
            set_y_in.append(y)
        else:
            set_x.append(x)
            set_y.append(y)
    plt.scatter(set_x_in, set_y_in, s=10, color='red')
    plt.scatter(set_x, set_y, s=10, color='blue')
    Pi = inners/n * 4
    return Pi


if __name__ == '__main__':
    ITRS = 100000
    my_pi = monte_carlo(ITRS)
    print(my_pi)
    plt.title('Iterations = '+str(ITRS)+'   '+'Pi = '+str(my_pi))
    plt.legend()
    plt.show()

