import numpy as np
#Librerias para semillero referentes a ecuaciones no lineales

#Método de bisección
def biseccion(f,a,b,k):
    c = (a + b)/2
    Ea=np.abs(f(c))
    Iter=1
    while Ea > 0.5*10**(-k):
        if f(c)*f(a) < 0:
            b=c
        else:
            a=c
        c=(a+b)/2
        Ea=np.abs(f(c))
        Iter+=1

    return c, Ea, Iter

#Método de punto fijo
def pf(f,g,x0,k):
    Ea=np.abs(f(x0))
    Iter=0
    while Ea > 0.5*10**(-k):
        xn = g(x0)
        En = np.abs(f(xn))
        Iter+=1
        Ea = En
        x0 = xn
    
    return  x0, Ea, Iter