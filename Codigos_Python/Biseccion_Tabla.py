import numpy as np
import ecuaciones as eq
import pandas as pd

def f(x):
    return np.exp(-x)-x**2-2

#Metodo de biseccion
a=-2
b=-1
k=5
Sol, Error, Iteraciones = eq.biseccion_tabla(f,a,b,k)

df=pd.DataFrame({'Iteraciones':Iteraciones, 'Solución':Sol, 'Error':Error})
print(df)