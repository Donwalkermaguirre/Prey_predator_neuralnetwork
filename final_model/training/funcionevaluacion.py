import numpy as np
import matplotlib.pyplot as plt
from red import redn
import math
from conversionarray import devarray
from binary2angle import dirpresa
from evaluacionred import evalred
"""l=50
v=l"""
"""xd=np.array([l*np.random.rand(),l*np.random.rand()])
xp=np.array([l*np.random.rand(),l*np.random.rand()])"""
"""xdp=[xd[0]]
ydp=[xd[1]]"""


"""vp=np.array([0.1,5])*0.18"""
"""w=np.random.rand(4,2)
b=np.random.rand(4)
p=np.random.rand(12)"""


def dispd(a,b):
    d=(a-b)/(np.sqrt(np.dot(a-b,a-b)))
    return d

"""plt.axis([0, l, 0, v])
plt.ion()"""
def evalfun(p):
    l = 50
    v = l
    """xd = np.array([l * np.random.rand(), l * np.random.rand()])
    xp = np.array([l/2, l/2])"""
    xp = np.array([l / 2, l / 2])
    c = np.random.rand()
    xd = np.array([math.cos(2 * math.pi * c), math.sin(2 * math.pi * c)])
    xd = 0.5 * l * xd
    xd = xp + xd
    cond = np.sqrt(np.dot(xd - xp, xd - xp))
    t=0
    vd=0.7
    dt=1
    """s=devarray(p)
    w=s[0]
    b=s[1]"""
    while cond > 3:
        xd = xd + vd * dispd(xp, xd) * dt
        """" xdp.append(xd[0])
            ydp.append(xd[1])"""
        vp=0
        if np.sqrt(np.dot(xd - xp, xd - xp)) < 20:
            vpp = evalred(p,dispd(xp, xd))
            vpp=vpp.round()
            vp=dirpresa(vpp)
            "vp = np.array([vpp[0] - vpp[1], vpp[2] - vpp[3]])"
            "vp = vp / np.sqrt(np.dot(vp, vp))"
            vp=0.6*vp
            t = t + dt
        xp = xp + vp * dt
        """print(t)"""
        """xdplt=np.array([xd[0]-l*math.floor(xd[0]/l),xd[1]-l*math.floor(xd[1]/l)])
        xpplt = np.array([xp[0] - l * math.floor(xp[0] / l), xp[1] - l * math.floor(xp[1] / l)])
        plt.scatter(xdplt[0], xdplt[1])
        plt.scatter(xpplt[0], xpplt[1],color='red')
        print(xpplt[0],xpplt[1])
        plt.pause(0.05)"""
        cond = np.sqrt(np.dot(xd - xp, xd - xp))
        if t > 1000:
            cond = 0
    return t


"print( evalfun([0, -4, 6, -1, 8, -4, 4, -9, 9, 5, -8, 3, 7, 6, -5, -2, 5, -9, 5, 0, 4, -5, -3, 9, 2, -2, -6, 4, -8, 1, -5, 5]))"