import numpy as np
from red import redn
from conversionarraycapa2 import devarray2

def evalred(p,x):
    s=devarray2(p)
    w=s[0]
    b = s[1]
    w2 = s[2]
    b2 = s[3]
    x1=redn(w,b,x)

    out=redn(w2,b2,x1)

    return out