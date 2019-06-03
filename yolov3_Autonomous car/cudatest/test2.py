import numpy as np
from timeit import default_timer as timer
from numba import jit

@jit
def VectorAdd(a,b,c):
    for i in range(len(a)):
        c.append(a[i]+b[i])

@jit
def inital(A,B):
    for i in range(3200000):
        A.append(3200000)
        B.append(3200000)

def main():
    N = 32000000
    #A=np.ones(N, dtype=np.float32)
    #B=np.ones(N,dtype=np.float32)
    A=[]
    B=[]
    inital(A,B)
    C=[0,]
    #C=np.zeros(N,dtype=np.float32)

    start = timer()
    VectorAdd(A,B,C)
    #C=VectorAdd(A,B)
    vectoradd_timer = timer()-start
    #print("C[:5]= "+str(C[:5]))
    #print("C[-5:]= "+str(C[-5:]))
    print("VectorAdd tokk %f seconds"%vectoradd_timer)

if __name__=='__main__':
    main()