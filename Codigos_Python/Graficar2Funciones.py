import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sympy import symbols, lambdify

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Gráfica de funciones")

# Funciones para graficar las funciones ingresadas
def graficar():
    plot.clear()
    x_vals = np.linspace(float(min_entry.get()), float(max_entry.get()), 400)
    
    try:
        x = symbols('x')
        
        expr_f = entrada_funcion_f.get()
        f = lambdify(x, expr_f, "numpy")
        y_vals_f = f(x_vals)
        
        expr_g = entrada_funcion_g.get()
        g = lambdify(x, expr_g, "numpy")
        y_vals_g = g(x_vals)
        
        plot.plot(x_vals, y_vals_f, label=f'$f(x) = {expr_f}$')
        plot.plot(x_vals, y_vals_g, label=f'$g(x) = {expr_g}$')
        plot.set_xlabel('x')
        plot.set_ylabel('y')
        plot.legend()
        canvas.draw()
    except Exception as e:
        print("Error:", e)

# Crear un lienzo para el gráfico
fig = Figure(figsize=(6, 4), dpi=100)
plot = fig.add_subplot(1, 1, 1)

# Crear widgets para ingresar las funciones y los valores de rango
funcion_f_label = tk.Label(root, text="Función f(x):")
funcion_f_label.pack()
entrada_funcion_f = tk.Entry(root)
entrada_funcion_f.pack()

funcion_g_label = tk.Label(root, text="Función g(x):")
funcion_g_label.pack()
entrada_funcion_g = tk.Entry(root)
entrada_funcion_g.pack()

min_label = tk.Label(root, text="Valor mínimo de x:")
min_label.pack()
min_entry = tk.Entry(root)
min_entry.pack()

max_label = tk.Label(root, text="Valor máximo de x:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.pack()

# Crear el botón para graficar
graficar_button = tk.Button(root, text="Graficar", command=graficar)
graficar_button.pack()

# Incorporar la gráfica en un widget de tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Ejecutar el bucle principal de tkinter
tk.mainloop()
