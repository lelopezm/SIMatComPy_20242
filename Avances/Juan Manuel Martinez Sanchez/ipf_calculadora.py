import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Método de punto fijo
def pf(f, g, x0, k):
    Ea = np.abs(f(x0))
    Iter = 0
    S = [x0]
    E = [Ea]
    I = [Iter]
    while Ea > 0.5 * 10 ** (-k):
        xn = g(x0)
        En = np.abs(f(xn))
        Iter += 1
        Ea = En
        x0 = xn
        S.append(x0)
        E.append(Ea)
        I.append(Iter)

        if Ea > 10:
            raise RuntimeError("la función g(x) no es adecuada")
    return S, E, I


""" Convierte las funciones a objetos ejecutables usando eval. Luego:
Llama al método pf para realizar las iteraciones.
Presenta los resultados en un cuadro de texto y en una nueva ventana con formato tabular.
"""


def ejecutar_punto_fijo():
    try:
        funcion_f_str = funcion_f_entry.get()
        funcion_g_str = funcion_g_entry.get()
        x0 = float(x0_entry.get())
        k = int(decimales_entry.get())

        f = lambda x: eval(funcion_f_str)
        g = lambda x: eval(funcion_g_str)

        resultado, error, iteraciones = pf(f, g, x0, k)

        resultados = pd.DataFrame(
            {"Iteración": iteraciones, "Resultado": resultado, "Error": error}
        )

        ultimo_resultado = resultados.iloc[-1]

        resultado_texto.delete(1.0, END)
        resultado_texto.insert(
            END,
            f"Último resultado:\nIteración: {int(ultimo_resultado['Iteración'])}\nResultado: {ultimo_resultado['Resultado']:.5f}\nError: {ultimo_resultado['Error']:.6f}\n",
        )

        top = tk.Toplevel()
        top.title("Resultados del Método del Punto Fijo")
        tabla = tk.Label(top, text=resultados.to_string(index=False))
        tabla.pack()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(END, f"Error: {str(e)}")


def borrar_campos():
    funcion_f_entry.delete(0, END)
    funcion_g_entry.delete(0, END)
    x0_entry.delete(0, END)
    decimales_entry.delete(0, END)
    resultado_texto.delete(1.0, END)

    """ Este metodo lo que hace es graficarg(x) junto con y=x
(para verificar que la funcion escogida sea apta en el metodo de punto fijo).
    """


def graficar_funcion():
    try:
        funcion_g_str = funcion_g_entry.get()
        a = float(intervalo_a_entry.get())
        b = float(intervalo_b_entry.get())

        g = lambda x: eval(funcion_g_str)

        X = np.linspace(a, b, 500)
        Y = g(X)

        plt.figure(figsize=(8, 6))
        plt.plot(X, Y, "#2438e3", linewidth=1.5, label="$y=g(x)$")
        plt.plot(X, X, "#e33224", linewidth=1.5, label="$y=x$")
        plt.xlim([a, b])
        plt.ylim([a, b])
        plt.grid(True)
        plt.legend()
        plt.title("Gráfica de g(x) y y = x")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(
            END,
            f"Error se necesita la funcion g(x), este recuadro es para verificar si g(x) es la solucion: {str(e)}",
        )


def graficar_funcion_f():
    try:
        funcion_f_str = funcion_f_entry.get()
        a = float(intervalo_a_entry.get())
        b = float(intervalo_b_entry.get())

        f = lambda x: eval(funcion_f_str)

        X = np.linspace(a, b, 500)
        Y = f(X)

        plt.figure(figsize=(8, 6))
        plt.plot(X, Y, "#2ca02c", linewidth=1.5, label="$y=f(x)$")
        plt.xlim([a, b])
        plt.grid(True)
        plt.legend()
        plt.title("Gráfica de f(x)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(END, f"Se necesitan los intervalos: {str(e)}")


# Configuración de la ventana principal
raiz = Tk()
raiz.title("Método de Punto Fijo con Calculadora")
raiz.geometry("1200x700")
raiz.config(bg="black")


""" La interfaz está dividida en dos marcos principales:

Frame de entrada principal

Campos para:
f(x), g(x), a, b, x_0, y decimales.
Botones para ejecutar el método, graficar las funciones y borrar campos.
Una caja de texto para mostrar resultados.

Frame de la calculadora
Calculadora auxiliar con funciones básicas (+,-,x,÷) y avanzadas (sin,cos,tan,log,exp).
Los resultados de la calculadora pueden insertarse en los campos seleccionados.
"""
# Frame principal
miFrame = Frame(raiz, bg="blue", border=15, relief=GROOVE)
miFrame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

# Campos de entrada
Label(miFrame, text="f(x):", bg="blue", fg="white").grid(
    row=0, column=0, padx=10, pady=10
)
funcion_f_entry = Entry(miFrame, width=30)
funcion_f_entry.grid(row=0, column=1, padx=10, pady=10)

Label(miFrame, text="g(x):", bg="blue", fg="white").grid(
    row=1, column=0, padx=10, pady=10
)
funcion_g_entry = Entry(miFrame, width=30)
funcion_g_entry.grid(row=1, column=1, padx=10, pady=10)

Label(miFrame, text="a:", bg="blue", fg="white").grid(row=2, column=0, padx=10, pady=10)
intervalo_a_entry = Entry(miFrame, width=30)
intervalo_a_entry.grid(row=2, column=1, padx=10, pady=10)

Label(miFrame, text="b:", bg="blue", fg="white").grid(row=3, column=0, padx=10, pady=10)
intervalo_b_entry = Entry(miFrame, width=30)
intervalo_b_entry.grid(row=3, column=1, padx=10, pady=10)

Label(miFrame, text="Valor inicial:", bg="blue", fg="white").grid(
    row=4, column=0, padx=10, pady=10
)
x0_entry = Entry(miFrame, width=30)
x0_entry.grid(row=4, column=1, padx=10, pady=10)

Label(miFrame, text="Decimales correctos:", bg="blue", fg="white").grid(
    row=5, column=0, padx=10, pady=10
)
decimales_entry = Entry(miFrame, width=30)
decimales_entry.grid(row=5, column=1, padx=10, pady=10)

# Botones
Button(
    miFrame,
    text="Ejecutar Punto Fijo",
    command=ejecutar_punto_fijo,
    width=20,
    bg="green",
    fg="white",
).grid(row=6, column=0, padx=10, pady=10)
Button(
    miFrame, text="Borrar", command=borrar_campos, width=15, bg="red", fg="white"
).grid(row=6, column=1, padx=10, pady=10)
Button(
    miFrame,
    text="Graficar g(x)",
    command=graficar_funcion,
    width=20,
    bg="blue",
    fg="white",
).grid(row=6, column=2, padx=10, pady=10)
Button(
    miFrame,
    text="Graficar f(x)",
    command=graficar_funcion_f,
    width=20,
    bg="purple",
    fg="white",
).grid(row=6, column=3, padx=10, pady=10)

# Cuadro de texto para mostrar resultados
resultado_texto = Text(miFrame, width=80, height=10)
resultado_texto.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Frame para la calculadora
calc_frame = Frame(raiz, bg="white", relief=GROOVE, border=10)
calc_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

Label(calc_frame, text="Calculadora", bg="white", font=("Arial", 12)).grid(
    row=0, column=0, columnspan=4, pady=5
)

selected_field = StringVar(value="f(x)")
fields = {
    "f(x)": funcion_f_entry,
    "g(x)": funcion_g_entry,
    "a": intervalo_a_entry,
    "b": intervalo_b_entry,
    "Valor inicial": x0_entry,
    "Decimales": decimales_entry,
}
OptionMenu(calc_frame, selected_field, *fields.keys()).grid(
    row=1, column=0, columnspan=4, pady=5
)


def insertar_dato(campo, valor):
    campo.insert(END, valor)


def calcular(operacion):
    campo = fields[selected_field.get()]
    if operacion == "C":
        campo.delete(0, END)
    else:
        insertar_dato(campo, operacion)


buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    ".",
    "=",
    "+",
]

for i, button in enumerate(buttons):
    Button(
        calc_frame,
        text=button,
        command=lambda b=button: calcular(b),
        width=5,
        height=2,
        bg="lightblue",
    ).grid(row=(i // 4) + 2, column=i % 4)

# Botones para funciones avanzadas
advanced_buttons = ["sin", "cos", "tan", "log", "exp", "C"]
for i, button in enumerate(advanced_buttons):
    Button(
        calc_frame,
        text=button,
        command=lambda b=button: calcular(f"np.{b}(" if b not in ["=", "C"] else b),
        width=5,
        height=2,
        bg="orange",
    ).grid(row=(i // 3) + 5, column=i % 3)

raiz.mainloop()
