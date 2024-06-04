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
    barra_menu = Menu(root)

    menu_metricas = Menu(barra_menu, tearoff=0)
    menu_metricas.add_command(label="Punto de Función", command=mostrar_punto_de_funcion)
    menu_metricas.add_command(label="Punto de Casos de Uso", command=mostrar_aplicacion_casos_usos)  # Vincular a la nueva función
    menu_metricas.add_command(label="Punto Objeto", command=lambda: mostrar_mensaje("Punto Objeto"))
    menu_metricas.add_command(label="McCall", command=lambda: mostrar_mensaje("McCall"))
    menu_metricas.add_command(label="Métricas", command=lambda: mostrar_mensaje("Métricas"))

    # Agregar el menú de Métricas a la barra de menú
    barra_menu.add_cascade(label="Métricas", menu=menu_metricas)

    # Configurar la barra de menú
    root.config(menu=barra_menu)

def main():
    global root  # Hacer root global para acceder desde la función mostrar_aplicacion_casos_usos
    root = tk.Tk()
    root.title("Software de Métricas de Software")
    root.geometry("1200x700")

    # Crear y configurar el menú
    crear_menu(root)

    root.mainloop()

if __name__ == "__main__":
    main()
