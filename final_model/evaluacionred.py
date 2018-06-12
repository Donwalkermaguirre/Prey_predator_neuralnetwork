import numpy as np


import math

def devarray2(p):
    w = np.zeros([4, 2])
    w2 = np.zeros([4, 4])
    b2 = np.zeros(4)
    b = np.zeros(4)
    c = range(1, p.__len__() + 1)
    for i in c:
        if i <= 8:
            w[math.ceil(c[i] / 2) - 1, i % 2-1] = p[i - 1]

        if (i > 8) & (i <= 12):
            b[i - 9] = p[i - 1]

        if (i > 12) & (i <= 28):
            w2[math.ceil((c[i]-10) / 4) - 1, i % 4-1] = p[i - 1]



        if i>28:
            b2[i - 29] = p[i - 1]

    return w, b*0.1,w2,b2*0.1

def redn(a,b,x):
    f = lambda x: 1 / (1.0 + np.exp(-x))
    out = f(np.dot(a, x) + b)
    return out



def evalred(p,x):
    s=devarray2(p)
    w=s[0]
    b = s[1]
    w2 = s[2]
    b2 = s[3]
    x1=redn(w,b,x)

    out=redn(w2,b2,x1)

    return out