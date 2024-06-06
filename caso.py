import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabla import Tabla
from tabla2 import Tabla2

class AplicacionCasosUsos:
    def __init__(self, root):
        self.root = root
        self.root.title("Estimación de Puntos de Objeto")
        self.root.geometry("700x900")  # Tamaño de la ventana ajustado

        # Crear un canvas y un scrollbar
        self.canvas = tk.Canvas(root)
        self.scrollbar_v = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar_h = ttk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)

        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar_v.set, xscrollcommand=self.scrollbar_h.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar_v.pack(side="right", fill="y")
        self.scrollbar_h.pack(side="bottom", fill="x")

        # Valores para complejidad de pantallas e informes
        self.valores_complejidad_pantallas = {
            "Simple": 1,
            "Medio": 2,
            "Complejo": 3
        }

        self.valores_complejidad_reportes = {
            "Simple": 5,
            "Medio": 10,
            "Complejo": 15
        }

        # Marco para pantalla uno
        self.marco_pantallasuno = ttk.LabelFrame(self.scrollable_frame, text="Pantalla actores")
        self.marco_pantallasuno.pack(fill="both", expand="yes", padx=10, pady=10)

        self.texto_pantallasuno = tk.Text(self.marco_pantallasuno, height=10, width=50)
        self.texto_pantallasuno.pack(padx=10, pady=10)

        self.combo_pantallasuno = ttk.Combobox(self.marco_pantallasuno, values=["Simple", "Medio", "Complejo"], width=20)
        self.combo_pantallasuno.set("Seleccione peso")
        self.combo_pantallasuno.pack(padx=10, pady=10)

        # Marco para pantalla dos
        self.marco_pantallas = ttk.LabelFrame(self.scrollable_frame, text="Pantalla casos de uso")
        self.marco_pantallas.pack(fill="both", expand="yes", padx=10, pady=10)

        self.texto_pantallas = tk.Text(self.marco_pantallas, height=10, width=50)
        self.texto_pantallas.pack(padx=10, pady=10)

        self.combo_pantallas = ttk.Combobox(self.marco_pantallas, values=["Simple", "Medio", "Complejo"], width=20)
        self.combo_pantallas.set("Seleccione peso")
        self.combo_pantallas.pack(padx=10, pady=10)

        # Botón para calcular
        self.boton_calcular = ttk.Button(self.scrollable_frame, text="Calcular Caso de uso", command=self.calcular_caso_uso_sin_ajustar)
        self.boton_calcular.pack(padx=10, pady=10)

        # Etiqueta para mostrar el resultado del caso de uso sin ajustar
        self.resultado_label = ttk.Label(self.scrollable_frame, text="Caso de uso sin ajustar: 0.00")
        self.resultado_label.pack(padx=10, pady=10)

        # Marco para la tabla de factores técnicos
        self.marco_tabla_tecnicos = ttk.LabelFrame(self.scrollable_frame, text="Tabla de Factores Técnicos")
        self.marco_tabla_tecnicos.pack(fill="both", expand="yes", padx=10, pady=10)

        self.tabla_tecnicos = Tabla(self.marco_tabla_tecnicos)  # Incluir la tabla dentro del marco

        # Marco para la tabla de factores ambientales
        self.marco_tabla_ambientales = ttk.LabelFrame(self.scrollable_frame, text="Tabla de Factores Ambientales")
        self.marco_tabla_ambientales.pack(fill="both", expand="yes", padx=10, pady=10)

        self.tabla_ambientales = Tabla2(self.marco_tabla_ambientales)  # Incluir la tabla dentro del marco
        
         # Botón para calcular
        self.boton_calcular = ttk.Button(self.scrollable_frame, text="Calcular UCP", command=self.calcular_ucp_sin_ajustar)
        self.boton_calcular.pack(padx=10, pady=10)

    def calcular_caso_uso_sin_ajustar(self):
        try:
            # Extrayendo datos de las áreas de texto
            pantallasuno = self.texto_pantallasuno.get("1.0", tk.END).strip()
            pantallas = self.texto_pantallas.get("1.0", tk.END).strip()

            # Asumiendo que cada línea representa una pantalla
            num_pantallasuno = len(pantallasuno.split("\n"))
            num_pantallas = len(pantallas.split("\n"))

            # Verificar si se selecciona una opción en los comboboxes
            if (complejidad_pantallas := self.combo_pantallasuno.get()) == "Seleccione peso":
                self.resultado_label.config(text="Error: Seleccione la complejidad de las pantallas.")
                return
            if (complejidad_reportes := self.combo_pantallas.get()) == "Seleccione peso":
                self.resultado_label.config(text="Error: Seleccione la complejidad de los reportes.")
                return

            # Obtener valores de complejidad específicos para pantallas y reportes
            complejidad_pantallas = self.valores_complejidad_pantallas[complejidad_pantallas]
            complejidad_reportes = self.valores_complejidad_reportes[complejidad_reportes]

            # Calcular puntos de objeto (fórmula de ejemplo)
            caso_uso_sin_ajustar = (num_pantallasuno * complejidad_pantallas) + (num_pantallas * complejidad_reportes)

            # Mostrar resultado en la etiqueta
            self.resultado_label.config(text=f"Caso de uso sin ajustar: {caso_uso_sin_ajustar:.2f}")
        except Exception as e:
            self.resultado_label.config(text=f"Error: {e}")
            
    def calcular_ucp_sin_ajustar(self):
        try:
            # Extrayendo datos de las áreas de texto
            pantallasuno = self.texto_pantallasuno.get("1.0", tk.END).strip()
            pantallas = self.texto_pantallas.get("1.0", tk.END).strip()

            # Asumiendo que cada línea representa una pantalla
            num_pantallasuno = len(pantallasuno.split("\n"))
            num_pantallas = len(pantallas.split("\n"))

            # Verificar si se selecciona una opción en los comboboxes
            if (complejidad_pantallas := self.combo_pantallasuno.get()) == "Seleccione peso":
                self.resultado_label.config(text="Error: Seleccione la complejidad de las pantallas.")
                return
            if (complejidad_reportes := self.combo_pantallas.get()) == "Seleccione peso":
                self.resultado_label.config(text="Error: Seleccione la complejidad de los reportes.")
                return

            # Obtener valores de complejidad específicos para pantallas y reportes
            complejidad_pantallas = self.valores_complejidad_pantallas[complejidad_pantallas]
            complejidad_reportes = self.valores_complejidad_reportes[complejidad_reportes]

            # Calcular puntos de objeto (caso de uso sin ajustar)
            caso_uso_sin_ajustar = (num_pantallasuno * complejidad_pantallas) + (num_pantallas * complejidad_reportes)
        
            # Calcular UCP multiplicando por TCF y ECF
            tcf = self.tabla_tecnicos.calcular_tcf()  # Llamar al método calcular_tcf de Tabla
            ecf = self.tabla_ambientales.calcular_ecf()  # Llamar al método calcular_ecf de Tabla2
            ucp = caso_uso_sin_ajustar * tcf * ecf

            # Mostrar el resultado en un messagebox
            messagebox.showinfo("Resultado", f"Puntos de Caso de Uso Ajustados (UCP): {ucp:.2f}")  
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionCasosUsos(root)
    root.mainloop()
