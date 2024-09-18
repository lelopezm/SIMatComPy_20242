import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definir la función f(x) y la función iterativa g(x) desde el input del usuario
def definir_funcion(func_str):
    try:
        return lambda x: eval(func_str)
    except Exception as e:
        messagebox.showerror("Error", f"Función no válida. {e}")
        return None

# Método de punto fijo
def punto_fijo(f, g, x0, k):
    x = x0
    for i in range(k):
        x_new = g(x)
        error = abs(x_new - x)
        if error < 1e-7:
            return x_new, i+1, error
        x = x_new
    return x, k, error

# Función para graficar f(x) en el rango [a, b]
def graficar_funcion(f, a, b):
    try:
        # Crear un rango de valores de x entre a y b
        X = np.linspace(a, b, 500)
        
        # Evaluar la función f(x) para cada valor de X
        Yf = f(X)
        
        # Crear la gráfica
        fig, ax = plt.subplots(figsize=(6, 4))

        # Graficar la función f(x)
        ax.plot(X, Yf, label='$f(x)$', color='blue', lw=2)

        # Estilizar la gráfica
        ax.set_title("Gráfica de f(x)", fontsize=14)
        ax.set_xlabel("x", fontsize=12)
        ax.set_ylabel("f(x)", fontsize=12)
        ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)

        # Añadir la leyenda
        ax.legend()

        return fig

    except Exception as e:
        messagebox.showerror("Error", f"Error al graficar la función. {e}")
        return None

# Función para calcular el punto fijo cuando se presiona el botón "Calcular"
def calcular_punto_fijo():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        x0 = float(entry_x0.get())
        k = int(entry_k.get())
        funcion_f_str = entry_funcion_f.get()
        funcion_g_str = entry_funcion_g.get()

        f = definir_funcion(funcion_f_str)
        g = definir_funcion(funcion_g_str)
        if f is None or g is None:
            return

        # Calcular punto fijo
        sol, iteraciones, error = punto_fijo(f, g, x0, k)

        # Mostrar resultados
        resultado_label.config(text=f"x ≈ {sol:.6f}\nIteraciones: {iteraciones}\nError: {error:.1e}")

        # Graficar solución
        fig = graficar_funcion(f, a, b)
        if fig is not None:
            canvas = FigureCanvasTkAgg(fig, master=ventana_principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=8, column=0, columnspan=4)

    except ValueError:
        messagebox.showerror("Error", "Verifica que todos los valores sean correctos.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

# Función para graficar f(x) solo con a y b
def graficar():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        funcion_f_str = entry_funcion_f.get()

        f = definir_funcion(funcion_f_str)
        if f is None:
            return

        # Graficar
        fig = graficar_funcion(f, a, b)
        if fig is not None:
            canvas = FigureCanvasTkAgg(fig, master=ventana_principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=9, column=0, columnspan=4)

    except ValueError:
        messagebox.showerror("Error", "Verifica que los límites a y b sean correctos.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

# Configuración de la ventana
ventana_principal = Tk()
ventana_principal.title("Método de Punto Fijo")
ventana_principal.geometry("700x600")

# Etiquetas y entradas para los datos
Label(ventana_principal, text="Función f(x):").grid(row=0, column=0, padx=10, pady=10)
entry_funcion_f = Entry(ventana_principal)
entry_funcion_f.grid(row=0, column=1, padx=10, pady=10)

Label(ventana_principal, text="Función g(x):").grid(row=1, column=0, padx=10, pady=10)
entry_funcion_g = Entry(ventana_principal)
entry_funcion_g.grid(row=1, column=1, padx=10, pady=10)

Label(ventana_principal, text="Valor de a:").grid(row=2, column=0, padx=10, pady=10)
entry_a = Entry(ventana_principal)
entry_a.grid(row=2, column=1, padx=10, pady=10)

Label(ventana_principal, text="Valor de b:").grid(row=3, column=0, padx=10, pady=10)
entry_b = Entry(ventana_principal)
entry_b.grid(row=3, column=1, padx=10, pady=10)

Label(ventana_principal, text="Valor inicial x0:").grid(row=4, column=0, padx=10, pady=10)
entry_x0 = Entry(ventana_principal)
entry_x0.grid(row=4, column=1, padx=10, pady=10)

Label(ventana_principal, text="Iteraciones k:").grid(row=5, column=0, padx=10, pady=10)
entry_k = Entry(ventana_principal)
entry_k.grid(row=5, column=1, padx=10, pady=10)

# Botón para calcular el punto fijo
boton_calcular = Button(ventana_principal, text="Calcular", command=calcular_punto_fijo)
boton_calcular.grid(row=6, column=0, columnspan=2, pady=10)

# Botón para graficar f(x) solo con a y b
boton_graficar = Button(ventana_principal, text="Graficar f(x)", command=graficar)
boton_graficar.grid(row=7, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar resultados
resultado_label = Label(ventana_principal, text="")
resultado_label.grid(row=6, column=2, columnspan=2, pady=10)

# Iniciar la ventana
ventana_principal.mainloop()