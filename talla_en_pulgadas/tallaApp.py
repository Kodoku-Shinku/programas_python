import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tallaBackend as backend


def convertir_tallas(event=None):
    try:
        # Solicitar al usuario los datos
        pulgadas = float(pulgadas_entry.get())
        pies = float(pies_entry.get())

        # llamar al backend para procesar la informacion
        talla_pulgadas_cm = backend.convertir_pulgadas_a_centimetros(pulgadas)
        talla_pies_cm = backend.convertir_pies_a_centimetros(pies)

        # Mostrar el resultado de la conversion
        resultado_pulgadas.config(
            text=f"Talla en pulgadas: {talla_pulgadas_cm} cm")
        resultado_pies.config(text=f"Talla en pies: {talla_pies_cm} cm")
    except ValueError:
        # Mensaje de error si los datos son invalidos
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


# Crear la ventana
ventana = tk.Tk()
ventana.title("Conversión de Tallas")

# Obtener dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana
x = int((screen_width - 300) / 2)
y = int((screen_height - 240) / 2)

# Establecer la posición de la ventana
ventana.geometry(f"300x240+{x}+{y}")

# Cargar la imagen de fondo
original_image = Image.open("unidades_de_medida.jpg")
background_image = ImageTk.PhotoImage(original_image)

# Crear un widget Label para mostrar la imagen de fondo
background_label = tk.Label(ventana, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear los elementos de la interfaz
pulgadas_label = tk.Label(ventana, text="Talla en pulgadas:")
pulgadas_entry = tk.Entry(ventana)

pies_label = tk.Label(ventana, text="Talla en pies:")
pies_entry = tk.Entry(ventana)

convertir_button = tk.Button(
    ventana, text="Convertir", command=convertir_tallas)

resultado_pulgadas = tk.Label(ventana)
resultado_pies = tk.Label(ventana)

# Establecer el espaciado entre los elementos
pulgadas_label.pack(pady=5)
pulgadas_entry.pack(pady=5)
pies_label.pack(pady=5)
pies_entry.pack(pady=5)
convertir_button.pack(pady=10)
resultado_pulgadas.pack(pady=5)
resultado_pies.pack(pady=5)

# Asociar la tecla Enter a la función de conversión
ventana.bind("<Return>", convertir_tallas)

# Asociar la función de redimensionar imagen al evento de redimensionar la ventana
ventana.bind("<Configure>", resize_image)

# Centrar la ventana en la pantalla
window_width = 300
window_height = 240
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 2
ventana.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

# Iniciar el bucle de eventos
ventana.mainloop()
