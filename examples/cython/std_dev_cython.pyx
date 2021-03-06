cimport cython

cdef extern from "math.h":
    double sqrt(double m)

@cython.locals(a=list, mean=cython.double, i=cython.int, sum2=cython.double)
@cython.boundscheck(False)
def std_dev(a):
    mean = 0
    for i in a:
        mean += i
    mean = mean / len(a)
    sum2 = 0
    for i in a:
        sum2 += (i - mean)**2
    return sqrt(sum2 / len(a))
