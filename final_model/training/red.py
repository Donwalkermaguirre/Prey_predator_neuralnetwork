import numpy as np

def redn(a,b,x):
    f = lambda x: 1 / (1.0 + np.exp(-x))
    out = f(np.dot(a, x) + b)
    return out
