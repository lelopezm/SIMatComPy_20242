from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Método de Newton-Raphson
def newtonraphson(f, df, x0, k):
    Ea = np.abs(f(x0))
    Iter = 0
    S = [x0]
    E = [Ea]
    I = [Iter]
    while Ea > 0.5 * 10**(-k):
        xn = x0 - f(x0) / df(x0)
        En = np.abs(f(xn))
        Iter += 1
        Ea = En
        x0 = xn
        S.append(x0)
        E.append(Ea)
        I.append(Iter)
    return S, E, I

def ejecutar_newton_raphson():
    try:
        funcion_f_str = funcion_f_entry.get()
        funcion_df_str = funcion_df_entry.get()
        x0 = float(x0_entry.get())
        k = int(decimales_entry.get())

        # Convertir las funciones ingresadas a funciones ejecutables
        f = lambda x: eval(funcion_f_str)
        df = lambda x: eval(funcion_df_str)

        # Ejecutar el método de Newton-Raphson
        resultado, error, iteraciones = newtonraphson(f, df, x0, k)

        # Crear un DataFrame con los resultados
        resultados = pd.DataFrame(
            {"Iteración": iteraciones, "Resultado": resultado, "Error": error}
        )

        # Obtener el último resultado del DataFrame
        ultimo_resultado = resultados.iloc[-1]

        # Mostrar solo el último resultado en el cuadro de texto, formateado
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(
            END,
            f"Último resultado:\nIteración: {int(ultimo_resultado['Iteración'])}\nResultado: {ultimo_resultado['Resultado']:.5f}\nError: {ultimo_resultado['Error']:.6f}\n",
        )

        # Mostrar el DataFrame completo en una ventana separada
        top = tk.Toplevel()
        top.title("Resultados del Método de Newton-Raphson")
        tabla = tk.Label(top, text=resultados.to_string(index=False))
        tabla.pack()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(END, f"Error: {str(e)}")

# Función para borrar los campos de entrada y el cuadro de texto
def borrar_campos():
    funcion_f_entry.delete(0, END)
    funcion_df_entry.delete(0, END)
    x0_entry.delete(0, END)
    decimales_entry.delete(0, END)
    resultado_texto.delete(1.0, END)

# Configuración de la ventana principal
raiz = Tk()
raiz.title("Método de Newton-Raphson")
raiz.geometry("1100x600")
raiz.config(bg="black", relief=GROOVE, border=20, cursor="pirate")

# Frame principal
miFrame = Frame(raiz)
miFrame.pack(side=TOP, padx=20, pady=20)
miFrame.config(bg="blue", border=15, width=600, height=400, relief=GROOVE)

# Campos de entrada y etiquetas
Label(miFrame, text="Función f(x):", bg="blue", fg="white").grid(
    row=0, column=0, padx=10, pady=10
)
funcion_f_entry = Entry(miFrame, width=30)
funcion_f_entry.grid(row=0, column=1, padx=10, pady=10)

Label(miFrame, text="Función df(x):", bg="blue", fg="white").grid(
    row=1, column=0, padx=10, pady=10
)
funcion_df_entry = Entry(miFrame, width=30)
funcion_df_entry.grid(row=1, column=1, padx=10, pady=10)

Label(miFrame, text="Valor inicial (x0):", bg="blue", fg="white").grid(
    row=2, column=0, padx=10, pady=10
)
x0_entry = Entry(miFrame, width=30)
x0_entry.grid(row=2, column=1, padx=10, pady=10)

Label(miFrame, text="Número de decimales:", bg="blue", fg="white").grid(
    row=3, column=0, padx=10, pady=10
)
decimales_entry = Entry(miFrame, width=30)
decimales_entry.grid(row=3, column=1, padx=10, pady=10)

# Botones para ejecutar acciones
ejecutar_btn = Button(
    miFrame,
    text="Ejecutar Newton-Raphson",
    command=ejecutar_newton_raphson,
    width=20,
    bg="green",
    fg="white",
)
ejecutar_btn.grid(row=4, column=0, padx=10, pady=10)

borrar_btn = Button(
    miFrame, text="Borrar", command=borrar_campos, width=15, bg="red", fg="white"
)
borrar_btn.grid(row=4, column=1, padx=10, pady=10)

# Cuadro de texto para mostrar resultados
resultado_texto = Text(miFrame, width=80, height=10)
resultado_texto.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Ejecutar el bucle principal
raiz.mainloop()