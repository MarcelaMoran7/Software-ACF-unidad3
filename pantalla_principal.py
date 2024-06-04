import tkinter as tk
from tkinter import ttk, Menu, messagebox
from punto_de_funcion import mostrar_punto_de_funcion
from caso import AplicacionCasosUsos  # Importar la clase AplicacionCasosUsos

# Autor: Kevin Dominguez 2024

def mostrar_mensaje(metric):
    message = f"Seleccionaste {metric}"
    messagebox.showinfo("Información", message)

def mostrar_aplicacion_casos_usos():
    # Crear una nueva ventana para la aplicación de casos de uso
    new_window = tk.Toplevel(root)
    app = AplicacionCasosUsos(new_window)

def crear_menu(root):
    barra_menu = Menu(root, background='#3e4149', foreground='white', activebackground='#2d2f33', activeforeground='white')
    root.config(menu=barra_menu)

def estilo_personalizado():
    style = ttk.Style()
    style.theme_use('clam')

    # Estilos para botones
    style.configure('TButton', font=('Arial', 12), padding=10)
    
    # Estilos para etiquetas
    style.configure('TLabel', font=('Arial', 12))

    # Estilos para el marco
    style.configure('TFrame', background='#f0f0f0')

def main():
    global root  # Hacer root global para acceder desde la función mostrar_aplicacion_casos_usos
    root = tk.Tk()
    root.title("Software de Métricas de Software")
    root.geometry("1200x700")

    # Aplicar estilos personalizados
    estilo_personalizado()

    # Crear y configurar el menú
    crear_menu(root)

    # Crear un marco principal
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)

    # Agregar un título en el centro de la ventana
    titulo = ttk.Label(main_frame, text="Bienvenido al Software de Métricas de Software", font=("Arial", 24))
    titulo.pack(pady=20)

    # Agregar una imagen de fondo (opcional)
    # bg_image = tk.PhotoImage(file="no pude ponerle la imagen") 
    # bg_label = ttk.Label(main_frame, image=bg_image)
    # bg_label.place(relwidth=1, relheight=1)

    # Marco para los botones
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20)

    # Botón de Métricas
    metricas_button = ttk.Menubutton(button_frame, text="Métricas")
    metricas_menu = Menu(metricas_button, tearoff=0)
    metricas_menu.add_command(label="Punto de Función", command=mostrar_punto_de_funcion)
    metricas_menu.add_command(label="Punto de Casos de Uso", command=mostrar_aplicacion_casos_usos)  # Vincular a la nueva función
    metricas_menu.add_command(label="Punto Objeto", command=lambda: mostrar_mensaje("Punto Objeto"))
    metricas_menu.add_command(label="McCall", command=lambda: mostrar_mensaje("McCall"))
    metricas_menu.add_command(label="Métricas", command=lambda: mostrar_mensaje("Métricas"))
    metricas_button.config(menu=metricas_menu)
    metricas_button.pack(side="left", padx=10)

    # Botón de salida
    exit_button = ttk.Button(button_frame, text="Salir", command=root.quit)
    exit_button.pack(side="left", padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
