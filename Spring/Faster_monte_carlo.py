import multiprocessing
from random import uniform
from math import sqrt
import time


pros = 4
iters = 1000000
size = 1000000

def in_count(n, size):
    x = 0 
    y = 0
    inners = 0

    for i in range(n):
        x = uniform(0,size)
        y = uniform(0,size)
        if sqrt(x**2 + y**2)<=size:
            inners+=1
    return inners

ins = 0
t_s = time.time()
with multiprocessing.Pool(processes=pros) as pool:
    res = [pool.apply_async(in_count,(iters,size)) for i in range(pros)]
    tmp = [rs.get() for rs in res]

for c in tmp:
    ins+=int(c)
Pi = ins/(size*pros)*4
print('with parallelysm: '+str(Pi)+'  time spent:'+str(time.time()-t_s))

ins = 0
Pi = 0
t_s = time.time()
for i in range(pros):
    ins+=in_count(iters,size)
Pi = ins/(size*pros)*4
print('without parallelysm: '+str(Pi)+'  time spent:'+str(time.time()-t_s))
