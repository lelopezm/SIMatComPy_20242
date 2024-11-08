from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Método de bisección
def biseccion(f,a,b,k):
    c = (a + b)/2
    Ea=np.abs(f(c))
    Iter=1
    S=[c]
    E=[Ea]
    I=[Iter]
    while Ea > 0.5*10**(-k):
        if f(c)*f(a) < 0:
            b=c
        else:
            a=c
        c=(a+b)/2
        Ea=np.abs(f(c))
        Iter+=1
        S.append(c)
        E.append(Ea)
        I.append(Iter)
    return S, E, I

# Función que ejecuta el método de bisección al presionar el botón
def ejecutar_biseccion():
    try:
        funcion_str = funcion_entry.get()
        a = float(intervalo_a_entry.get())
        b = float(intervalo_b_entry.get())
        k = int(decimales_entry.get())

        # Convertir la función ingresada a una función ejecutable
        f = lambda x: eval(funcion_str)

        # Ejecutar el método de bisección
        resultado, error, iteraciones = biseccion(f, a, b, k)

        # Mostrar los resultados en el cuadro de texto
        resultado_texto.delete(1.0, END)
        # Crear un DataFrame con los resultados
        resultados = pd.DataFrame({'Solución': resultado, 'Error': error, 'Iteraciones': iteraciones})

        # Mostrar el DataFrame en una ventana separada (ejemplo)
        top = tk.Toplevel()
        top.title("Resultados")
        tabla = tk.Label(top, text=resultados.to_string())
        tabla.pack()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(END, f"Error: {str(e)}")

# Función para borrar los campos de entrada y el cuadro de texto
def borrar_campos():
    funcion_entry.delete(0, END)
    intervalo_a_entry.delete(0, END)
    intervalo_b_entry.delete(0, END)
    decimales_entry.delete(0, END)
    resultado_texto.delete(1.0, END)

# Función para graficar la función
def graficar_funcion():
    try:
        funcion_str = funcion_entry.get()
        a = float(intervalo_a_entry.get())
        b = float(intervalo_b_entry.get())

        # Convertir la función ingresada a una función ejecutable
        f = lambda x: eval(funcion_str)

        # Crear el espacio de valores de x y calcular f(x)
        x = np.linspace(a, b, 400)
        y = f(x)

        # Graficar la función
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"f(x) = {funcion_str}")
        plt.axhline(0, color='black', linewidth=1)  # Línea en y=0
        plt.axvline(0, color='black', linewidth=1)  # Línea en x=0
        plt.title("Gráfica de la Función")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(END, f"Error al graficar: {str(e)}")

# Configuración de la ventana principal
raiz = Tk()
raiz.title("Método de Bisección de JuanMa")
raiz.resizable()
raiz.geometry("1100x600")
raiz.config(bg="black")
raiz.config(relief=GROOVE, border=20)
raiz.config(cursor="pirate")

# Frame principal
miFrame = Frame(raiz)
miFrame.pack(side=TOP, padx=20, pady=20)
miFrame.config(bg="blue", border=15, width=600, height=400)
miFrame.config(relief=GROOVE)

# Campos de entrada y etiquetas
Label(miFrame, text="Función f(x):", bg="blue", fg="white").grid(row=0, column=0, padx=10, pady=10)
funcion_entry = Entry(miFrame, width=30)
funcion_entry.grid(row=0, column=1, padx=10, pady=10)

Label(miFrame, text="Intervalo [a]:", bg="blue", fg="white").grid(row=1, column=0, padx=10, pady=10)
intervalo_a_entry = Entry(miFrame, width=30)
intervalo_a_entry.grid(row=1, column=1, padx=10, pady=10)

Label(miFrame, text="Intervalo [b]:", bg="blue", fg="white").grid(row=2, column=0, padx=10, pady=10)
intervalo_b_entry = Entry(miFrame, width=30)
intervalo_b_entry.grid(row=2, column=1, padx=10, pady=10)

Label(miFrame, text="Número de decimales:", bg="blue", fg="white").grid(row=3, column=0, padx=10, pady=10)
decimales_entry = Entry(miFrame, width=30)
decimales_entry.grid(row=3, column=1, padx=10, pady=10)

# Botones
graficar_btn = Button(miFrame, text="Ejecutar Bisección", command=ejecutar_biseccion, width=20, bg="green", fg="white")
graficar_btn.grid(row=4, column=0, padx=10, pady=10)

borrar_btn = Button(miFrame, text="Borrar", command=borrar_campos, width=15, bg="red", fg="white")
borrar_btn.grid(row=4, column=1, padx=10, pady=10)

grafica_btn = Button(miFrame, text="Graficar Función", command=graficar_funcion, width=20, bg="blue", fg="white")
grafica_btn.grid(row=4, column=2, padx=10, pady=10)

# Cuadro de texto para mostrar resultados
resultado_texto = Text(miFrame, width=80, height=10)
resultado_texto.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Ejecutar el bucle principal
raiz.mainloop()