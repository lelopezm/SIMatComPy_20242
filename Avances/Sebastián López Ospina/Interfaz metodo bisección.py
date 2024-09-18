import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definir una función desde el input del usuario
def definir_funcion(func_str):
    try:
        return lambda x: eval(func_str)
    except Exception as e:
        messagebox.showerror("Error", f"Función no válida. {e}")
        return None

# Método de bisección simplificado
def biseccion(f, a, b, k):
    for i in range(k):
        c = (a + b) / 2
        if f(c) == 0 or abs(b - a) < 1e-7:
            return c, i+1, abs(b - a)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, k, abs(b - a)

# Función para graficar f(x) y la solución
def graficar_funcion(f, a, b, sol):
    X = np.linspace(a, b, 500)
    Y = f(X)

    fig, ax = plt.subplots(figsize=(6, 4))

    # Gráfico de la función en azul con una línea continua gruesa
    ax.plot(X, Y, label='$f(x)$', color='blue', lw=2)

    # Resaltar el eje x con una línea punteada negra
    ax.axhline(0, color='black', lw=1, ls='--')
    
    # Resaltar el eje y con una línea punteada negra
    ax.axvline(0, color='black', lw=1, ls='--')

    # Añadir el punto de la solución en rojo
    ax.scatter(sol, 0, color='red', zorder=5, label=f'Solución: x={sol:.4f}', s=100, edgecolor='black')

    # Gráfico de la línea de error en el eje X (donde está la solución)
    ax.vlines(sol, ymin=min(Y), ymax=0, colors='orange', linestyles='dashed', lw=1.5, label='Error')

    # Estilizar la gráfica
    ax.set_title("Método de Bisección", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("f(x)", fontsize=12)
    ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)

    # Leyenda
    ax.legend()

    return fig

# Cálculo y graficado cuando se presiona el botón
def calcular_biseccion():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        k = int(entry_k.get())
        funcion_str = entry_funcion.get()

        f = definir_funcion(funcion_str)
        if f is None:
            return

        # Calcular bisección
        sol, iteraciones, error = biseccion(f, a, b, k)

        # Mostrar resultados
        resultado_label.config(text=f"x ≈ {sol:.6f}\nIteraciones: {iteraciones}\nError: {error:.1e}")

        # Graficar
        fig = graficar_funcion(f, a, b, sol)
        canvas = FigureCanvasTkAgg(fig, master=ventana_principal)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=0, columnspan=4)
        
    except ValueError:
        messagebox.showerror("Error", "Verifica que todos los valores sean correctos.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

# Configuración de la ventana
ventana_principal = Tk()
ventana_principal.title("Método de Bisección Simplificado")
ventana_principal.geometry("700x500")

# Etiquetas y entradas para los datos
Label(ventana_principal, text="Función f(x):").grid(row=0, column=0, padx=10, pady=10)
entry_funcion = Entry(ventana_principal)
entry_funcion.grid(row=0, column=1, padx=10, pady=10)

Label(ventana_principal, text="Valor de a:").grid(row=1, column=0, padx=10, pady=10)
entry_a = Entry(ventana_principal)
entry_a.grid(row=1, column=1, padx=10, pady=10)

Label(ventana_principal, text="Valor de b:").grid(row=2, column=0, padx=10, pady=10)
entry_b = Entry(ventana_principal)
entry_b.grid(row=2, column=1, padx=10, pady=10)

Label(ventana_principal, text="Iteraciones k:").grid(row=3, column=0, padx=10, pady=10)
entry_k = Entry(ventana_principal)
entry_k.grid(row=3, column=1, padx=10, pady=10)

# Botón para calcular
boton_calcular = Button(ventana_principal, text="Calcular", command=calcular_biseccion)
boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar resultados
resultado_label = Label(ventana_principal, text="")
resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar la ventana
ventana_principal.mainloop()