import numpy as np
import math
"inputbinario"
"b=np.array([0,1,0,1])"
"""b=np.array([0.1,0.8,0.1,0.1])
b=b.round()"""
"b=b.astype(int)"
"""angulo unidad"""
a=(2*math.pi)/16

"""n: angulo 1-16"""

"conversion binario entero"
def bin2int(u):
    c=''.join(map(str,u))
    n=int(c,2)+1

    return n

"linealizado"


"""funcion vector direccion presa"""
def dirpresav(n):
    vp=np.array([math.cos((n-1)*a),math.sin((n-1)*a)])
    return vp
"funcion a llamar"
def dirpresa(s):
    s=s.astype(int)
    n=bin2int(s)


    vp = np.array([math.cos((n - 1) * a), math.sin((n - 1) * a)])


    return vp


"print(dirpresa(b))"