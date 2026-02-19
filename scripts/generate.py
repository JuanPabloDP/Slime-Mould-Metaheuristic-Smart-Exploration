import numpy as np
import math as mt

import matplotlib.pyplot as plt

def generate(x,r):
    v=np.zeros(len(x))
    k=0
    for i in range(len(v)):
        prob=1/mt.factorial(k)
        u=np.random.rand()
        if u<=prob:
            v[i]=1
            k+=1
    V=np.random.permutation(v)
    U=np.random.rand(len(x))
    x_1=x+V*(U*2*r-r)
    return x_1

if __name__ == '__main__':
    #TEST
    x=np.array([0,0])
    r=5
    num_neighbours=10000
    neighbours=[]
    for _ in range(num_neighbours):
        neighbours.append(generate(x,r))
    x_axis=np.array([i[0] for i in neighbours])
    y_axis=np.array([i[1] for i in neighbours])
    plt.scatter(x_axis, y_axis)
    plt.show()