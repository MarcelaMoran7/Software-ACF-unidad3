import tkinter as tk
from tkinter import ttk, messagebox

class AplicacionPuntosObjeto:
    def __init__(self, root):
        self.root = root
        self.root.title("Estimación de Puntos de Objeto")

        # Valores para complejidad de pantallas e informes
        self.valores_complejidad_pantallas = {
            "Simple": 1,
            "Medio": 2,
            "Complejo": 3
        }
        
        self.valores_complejidad_reportes = {
            "Simple": 2,
            "Medio": 5,
            "Complejo": 8
        }

        # Marco para pantallas
        self.marco_pantallas = ttk.LabelFrame(root, text="Pantallas (Una linea representa una pantalla)")
        self.marco_pantallas.pack(fill="both", expand="yes", padx=10, pady=10)

        self.texto_pantallas = tk.Text(self.marco_pantallas, height=10, width=50)
        self.texto_pantallas.pack(padx=10, pady=10)

        self.combo_pantallas = ttk.Combobox(self.marco_pantallas, values=["Simple", "Medio", "Complejo"], width=20)
        self.combo_pantallas.set("Seleccione complejidad")
        self.combo_pantallas.pack(padx=10, pady=10)

        # Marco para reportes
        self.marco_reportes = ttk.LabelFrame(root, text="Cantidad de reportes")
        self.marco_reportes.pack(fill="both", expand="yes", padx=10, pady=10)

        self.entrada_reportes = ttk.Entry(self.marco_reportes, width=50)
        self.entrada_reportes.pack(padx=10, pady=10)

        self.combo_reportes = ttk.Combobox(self.marco_reportes, values=["Simple", "Medio", "Complejo"], width=20)
        self.combo_reportes.set("Seleccione complejidad")
        self.combo_reportes.pack(padx=10, pady=10)

        # Marco para complejidad general
        self.marco_complejidad = ttk.LabelFrame(root, text="Complejidad General")
        self.marco_complejidad.pack(fill="both", expand="yes", padx=10, pady=10)

        self.combo_complejidad = ttk.Combobox(self.marco_complejidad, values=["Simple", "Medio", "Complejo"], width=20)
        self.combo_complejidad.set("Seleccione complejidad")
        self.combo_complejidad.pack(padx=10, pady=10)

        # Botón para calcular
        self.boton_calcular = ttk.Button(root, text="Calcular Puntos de Objeto", command=self.calcular_puntos_objeto)
        self.boton_calcular.pack(padx=10, pady=10)

    def calcular_puntos_objeto(self):
        try:
            # Extrayendo datos de las áreas de texto
            pantallas = self.texto_pantallas.get("1.0", tk.END).strip()
            reportes = self.entrada_reportes.get().strip()

            # Verificar si el área de texto de pantallas está vacía
            if not pantallas:
                messagebox.showerror("Error", "Por favor, ingrese al menos una pantalla.")
                return

            # Asumiendo que cada línea representa una pantalla
            num_pantallas = len(pantallas.split("\n"))

            # Validar y convertir la cantidad de reportes a entero
            try:
                num_reportes = int(reportes) if reportes else 0
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número entero válido para la cantidad de reportes.")
                return

            # Verificar si se selecciona una opción en los comboboxes
            if (complejidad_pantallas := self.combo_pantallas.get()) == "Seleccione complejidad":
                messagebox.showerror("Error", "Por favor, seleccione la complejidad de las pantallas.")
                return
            if (complejidad_reportes := self.combo_reportes.get()) == "Seleccione complejidad":
                messagebox.showerror("Error", "Por favor, seleccione la complejidad de los reportes.")
                return
            if (complejidad_general := self.combo_complejidad.get()) == "Seleccione complejidad":
                messagebox.showerror("Error", "Por favor, seleccione la complejidad general.")
                return

            # Obtener valores de complejidad específicos para pantallas y reportes
            complejidad_pantallas = self.valores_complejidad_pantallas[complejidad_pantallas]
            complejidad_reportes = self.valores_complejidad_reportes[complejidad_reportes]
            complejidad_general = self.valores_complejidad_pantallas[complejidad_general]  # Suponiendo que la complejidad general sigue los valores de pantallas

            # Calcular puntos de objeto (fórmula de ejemplo)
            puntos_objeto = (num_pantallas * complejidad_pantallas + num_reportes * complejidad_reportes) * complejidad_general

            # Mostrar resultado
            messagebox.showinfo("Resultado", f"Puntos de Objeto Estimados: {puntos_objeto:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionPuntosObjeto(root)
    root.mainloop()
