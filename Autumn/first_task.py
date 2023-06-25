import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной ниже

if __name__ == "__main__":
    args = numpy.arange(0, 200, 0.1)
    mpp.plot(
        args,
        [math.sin(a) * math.sin(a/20.0) for a in args]
    )
    mpp.show
