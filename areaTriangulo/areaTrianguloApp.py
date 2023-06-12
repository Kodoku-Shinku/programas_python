import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from areaTrianguloBackend import calcular_area_triangulo


def calcular_area(event=None):
    # Obtener los valores de los lados del triángulo desde las entradas
    try:
        a = float(ladoA_entry.get())
        b = float(ladoB_entry.get())
        c = float(ladoC_entry.get())

        # Validar que los lados sean positivos y formen un triángulo válido
        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror(
                "Error", "Los lados deben ser valores positivos.")
        elif a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror(
                "Error", "Los lados no forman un triángulo válido.")
        else:
            # Calcular el área del triángulo
            area = calcular_area_triangulo(a, b, c)

            # Mostrar el resultado
            resultado_area.config(text=f"El área del triángulo es: {area}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos.")


def resize_image(event):
    global background_image

    # Obtener el nuevo tamaño de la ventana
    width = event.width
    height = event.height

    # Redimensionar la imagen de fondo
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)

    # Actualizar la imagen de fondo
    background_label.configure(image=background_image)

    # Actualizar la posición del canvas del triángulo
    canvas.place(x=ladoA_entry.winfo_width() + 50, y=50)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del Área de un Triángulo")

# Obtener dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana
x = int((screen_width - 480) / 2)
y = int((screen_height - 260) / 2)

# Establecer la posición de la ventana
ventana.geometry(f"480x260+{x}+{y}")

# Cargar la imagen de fondo
original_image = Image.open("fondo_poligonal.jpg")
background_image = ImageTk.PhotoImage(original_image)

# Crear un widget Label para mostrar la imagen de fondo
background_label = tk.Label(ventana, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un widget Canvas para dibujar el triángulo de Herón
canvas_width = 240
canvas_height = 120
canvas = tk.Canvas(ventana, width=canvas_width, height=canvas_height)

# Coordenadas de los puntos del triángulo
x1, y1 = 0, canvas_height
x2, y2 = canvas_width - canvas_width/9, canvas_height
x3, y3 = canvas_width - canvas_width/3, canvas_height/5

# Dibujar el triángulo de Herón en el canvas
canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="aquamarine",
                      outline="black", width=2)

# Coordenadas de las etiquetas
x_label1, y_label1 = (x1 + x2) / 2, (y1 + y2) / 2
x_label2, y_label2 = (x2 + x3) / 2, (y2 + y3) / 2
x_label3, y_label3 = (x3 + x1) / 2, (y3 + y1) / 2

# Crear etiquetas para los lados del triángulo
ladoA_label = canvas.create_text(
    x_label2, y_label2, text="A: ", fill="black")
ladoB_label = canvas.create_text(
    x_label3, y_label3, text="B: ", fill="black")
ladoC_label = canvas.create_text(
    x_label1, y_label1, text="C: ", fill="black")

# Función para actualizar las posiciones de las etiquetas


def actualizar_posiciones_etiquetas():
    x_label1, y_label1 = (x1 + x2) / 2, (y1 + y2) / 2
    x_label2, y_label2 = (x2 + x3) / 2, (y2 + y3) / 2
    x_label3, y_label3 = (x3 + x1) / 2, (y3 + y1) / 2

    canvas.coords(ladoA_label, x_label2, y_label2)
    canvas.coords(ladoB_label, x_label3, y_label3)
    canvas.coords(ladoC_label, x_label1, y_label1)


# Crear los elementos de la interfaz
ladoA_label = tk.Label(ventana, text="Lado a:")
ladoA_entry = tk.Entry(ventana)

ladoB_label = tk.Label(ventana, text="Lado b:")
ladoB_entry = tk.Entry(ventana)

ladoC_label = tk.Label(ventana, text="Lado c:")
ladoC_entry = tk.Entry(ventana)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_area)

resultado_area = tk.Label(ventana)

# Crear etiquetas para mostrar los lados del triángulo
ladoA_value = tk.Label(ventana, text="Lado A:")
ladoB_value = tk.Label(ventana, text="Lado B:")
ladoC_value = tk.Label(ventana, text="Lado C:")

# Establecer el espaciado entre los elementos
ladoA_label.pack(anchor="w", padx=20, pady=5)
ladoA_entry.pack(anchor="w", padx=20, pady=5)
ladoB_label.pack(anchor="w", padx=20, pady=5)
ladoB_entry.pack(anchor="w", padx=20, pady=5)
ladoC_label.pack(anchor="w", padx=20, pady=5)
ladoC_entry.pack(anchor="w", padx=20, pady=5)
ladoA_value.pack(anchor="w", padx=20, pady=5)
ladoB_value.pack(anchor="w", padx=20, pady=5)
ladoC_value.pack(anchor="w", padx=20, pady=5)
boton_calcular.pack(anchor="w", padx=20, pady=10)
resultado_area.pack(anchor="w", padx=20, pady=5)

# Asociar la tecla Enter a la función de conversión
ventana.bind("<Return>", calcular_area)

# Asociar la función de redimensionar imagen al evento de redimensionar la ventana
ventana.bind("<Configure>", resize_image)

# Función para actualizar los valores de los lados en las etiquetas


def actualizar_valores_lados():
    ladoA_value.config(text="Lado A: " + ladoA_entry.get())
    ladoB_value.config(text="Lado B: " + ladoB_entry.get())
    ladoC_value.config(text="Lado C: " + ladoC_entry.get())


# Asociar la función de actualización de valores al evento de cambio en los Entry
ladoA_entry.bind("<KeyRelease>", lambda event: actualizar_valores_lados())
ladoB_entry.bind("<KeyRelease>", lambda event: actualizar_valores_lados())
ladoC_entry.bind("<KeyRelease>", lambda event: actualizar_valores_lados())

# Centrar la ventana en la pantalla
window_width = 480
window_height = 260
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 2
ventana.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

# Ejecutar el bucle de eventos de la ventana
ventana.mainloop()
