from tkinter import *
import tkinter as tk
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

        if Ea > 10 :
            raise RuntimeError("la función g(x) no es adecuada")
    return S, E, I


def ejecutar_punto_fijo():
    try:
        funcion_f_str = funcion_f_entry.get()
        funcion_g_str = funcion_g_entry.get()
        x0 = float(x0_entry.get())
        k = int(decimales_entry.get())

        # Convertir las funciones ingresadas a funciones ejecutables
        f = lambda x: eval(funcion_f_str)
        g = lambda x: eval(funcion_g_str)

        # Ejecutar el método de punto fijo
        resultado, error, iteraciones = pf(f, g, x0, k)

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
        top.title("Resultados del Método del Punto Fijo")
        tabla = tk.Label(top, text=resultados.to_string(index=False))
        tabla.pack()

    except Exception as e:
        resultado_texto.delete(1.0, END)
        resultado_texto.insert(END, f"Error: {str(e)}")


# Función para borrar los campos de entrada y el cuadro de texto
def borrar_campos():
    funcion_f_entry.delete(0, END)
    funcion_g_entry.delete(0, END)
    x0_entry.delete(0, END)
    decimales_entry.delete(0, END)
    resultado_texto.delete(1.0, END)


# Función para graficar las funciones g(x) y f(x)
def graficar_funcion():
    try:
        funcion_g_str = funcion_g_entry.get()
        a = float(intervalo_a_entry.get())
        b = float(intervalo_b_entry.get())

        # Convertir la función g(x) ingresada a una función ejecutable
        g = lambda x: eval(funcion_g_str)

        # Crear el espacio de valores de x
        X = np.linspace(a, b, 500)
        Y = g(X)

        # Graficar la función g(x) y la línea y=x
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


# Función para graficar la función f(x)
def graficar_funcion_f():
    try:
        funcion_f_str = funcion_f_entry.get()
        a = float(intervalo_a_entry.get())
        b = float(intervalo_b_entry.get())

        # Convertir la función f(x) ingresada a una función ejecutable
        f = lambda x: eval(funcion_f_str)

        # Crear el espacio de valores de x
        X = np.linspace(a, b, 500)
        Y = f(X)

        # Graficar la función f(x)
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
raiz.title("Método de Punto Fijo")
raiz.geometry("1100x600")
raiz.config(bg="black", relief=GROOVE, border=20, cursor="pirate")

# Frame principal
miFrame = Frame(raiz)
miFrame.pack(side=TOP, padx=20, pady=20)
miFrame.config(bg="blue", border=15, width=600, height=400, relief=GROOVE)

# Campos de entrada y etiquetas
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

Label(miFrame, text="a:", bg="blue", fg="white").grid(
    row=2, column=0, padx=10, pady=10
)
intervalo_a_entry = Entry(miFrame, width=30)
intervalo_a_entry.grid(row=2, column=1, padx=10, pady=10)

Label(miFrame, text="b:", bg="blue", fg="white").grid(
    row=3, column=0, padx=10, pady=10
)
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

# Botones para ejecutar acciones
ejecutar_btn = Button(
    miFrame,
    text="Ejecutar Punto Fijo",
    command=ejecutar_punto_fijo,
    width=20,
    bg="green",
    fg="white",
)
ejecutar_btn.grid(row=6, column=0, padx=10, pady=10)

borrar_btn = Button(
    miFrame, text="Borrar", command=borrar_campos, width=15, bg="red", fg="white"
)
borrar_btn.grid(row=6, column=1, padx=10, pady=10)

grafica_btn = Button(
    miFrame,
    text="Graficar g(x)",
    command=graficar_funcion,
    width=20,
    bg="blue",
    fg="white",
)
grafica_btn.grid(row=6, column=2, padx=10, pady=10)

grafica_f_btn = Button(
    miFrame,
    text="Graficar f(x)",
    command=graficar_funcion_f,
    width=20,
    bg="purple",
    fg="white",
)
grafica_f_btn.grid(row=6, column=3, padx=10, pady=10)

# Cuadro de texto para mostrar resultados
resultado_texto = Text(miFrame, width=80, height=10)
resultado_texto.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Ejecutar el bucle principal
raiz.mainloop()
