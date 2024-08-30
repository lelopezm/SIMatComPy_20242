import numpy as np
import matplotlib.pyplot as plt
import ecuaciones as eq

def f(x):
    return np.exp(-x)-x**2-2

#Metodo de biseccion
a=-2
b=-1
k=5
Sol, Error, Iteraciones = eq.biseccion(f,a,b,k)
print('La solución es x=%1.5f con %i iteraciones y %1.1e'%(Sol,Iteraciones,Error))

#Dominio para graficar f
#dominio [x0,xf]
x0=-3
xf=3
X=np.linspace(x0,xf,500)
Y=f(X) #función f
plt.plot(X,Y,'#0B0FF2',linewidth=1.5,label='$y=f(x)$')
plt.grid()
plt.show()
