import numpy as np
import matplotlib.pyplot as plt
import ecuaciones as eq

def f(x):
    return x**3 - x - 1

def g(x):
    return (x+1)**(1/3)

#intervalo donde esta la solución
a=1
b=2

#Solución
k=5
x0=1.5
Sol, Error, Iteraciones = eq.pf(f,g,x0,k)
print('La solución es x=%1.5f con %i iteraciones y %1.1e'%(Sol[-1],Iteraciones[-1],Error[-1]))

#grafica de g(x) en [a,b]
X=np.linspace(a,b,500)
Y=g(X) #función g
plt.plot(X,Y,'#2438e3',linewidth=1.5,label='$y=g(x)$')
plt.plot(X,X,'#e33224',linewidth=1.5,label='$y=x$')
plt.xlim([a,b])
plt.ylim([a,b])
plt.grid()
plt.legend()
plt.show()

