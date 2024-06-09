import tkinter as tk
from tkinter import ttk

class CosmicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Método COSMIC")
        self.root.geometry("400x800")  # Establecer un tamaño inicial
        self.root.resizable(True, True)  # Permitir redimensionar la ventana

        self.cells = []
        self.options = ["Entradas", "Salidas", "Lecturas", "Escrituras"]

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.container = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.container, anchor="nw")

        self.container.bind("<Configure>", self.on_configure)

        self.label = ttk.Label(self.container, text="      Ingrese los datos:", font=("Arial", 10, "bold"))
        self.label.grid(row=0, column=0, pady=(10, 5), sticky='n')

        self.inputs_label = ttk.Label(self.container, text="Defina y digite las Entradas, Salidas y \n      Lecturas en cada celda nueva")
        self.inputs_label.grid(row=1, column=0, columnspan=2, sticky='n')

        self.add_initial_cell()

        self.sum_label = ttk.Label(self.container, text="Suma total de Puntos de Función COSMIC (CFP): 0", font=("Arial", 10, "bold"))
        self.sum_label.grid(row=2, column=0, pady=(10, 5), sticky='n')

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_initial_cell(self):
        cell_frame = ttk.Frame(self.container)
        cell_frame.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        cell_entry = ttk.Entry(cell_frame, width=40)  # Modificar el ancho de la entrada
        cell_entry.grid(row=0, column=0, padx=5, pady=5, sticky='ew')  

        option_var = tk.StringVar()
        option_combobox = ttk.Combobox(cell_frame, textvariable=option_var, values=self.options, state="readonly", width=15)  # Modificar el ancho del combobox
        option_combobox.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        option_combobox.current(0)

        self.cells.append((cell_frame, cell_entry, option_var))

        # Agregar los botones debajo de la nueva celda
        self.add_buttons(row=4)

    def add_cell(self):
        cell_frame = ttk.Frame(self.container)
        cell_frame.grid(row=len(self.cells) + 3, column=0, padx=5, pady=5, sticky='w')

        cell_entry = ttk.Entry(cell_frame, width=40)  # Modificar el ancho de la entrada
        cell_entry.grid(row=0, column=0, padx=5, pady=5, sticky='ew')  

        option_var = tk.StringVar()
        option_combobox = ttk.Combobox(cell_frame, textvariable=option_var, values=self.options, state="readonly", width=15)  # Modificar el ancho del combobox
        option_combobox.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        option_combobox.current(0)

        self.cells.append((cell_frame, cell_entry, option_var))

        # Agregar los botones debajo de la nueva celda
        self.add_buttons(row=len(self.cells) + 4)

    def add_buttons(self, row):
        if not hasattr(self, 'button_frame'):
            self.button_frame = ttk.Frame(self.container)
            self.button_frame.grid(row=row, column=0, columnspan=2, sticky='w')
            
            self.add_cell_button = ttk.Button(self.button_frame, text="Agregar Celda", command=self.add_cell)
            self.add_cell_button.pack(side='left', padx=5, pady=5)
            
            self.delete_cell_button = ttk.Button(self.button_frame, text="Eliminar Celda", command=self.delete_cell)
            self.delete_cell_button.pack(side='left', padx=5, pady=5)
            
            self.calculate_button = ttk.Button(self.button_frame, text="Calcular", command=self.calculate)
            self.calculate_button.pack(side='left', padx=5, pady=5)
        else:
            self.button_frame.grid(row=row, column=0, columnspan=2, sticky='w')

    def delete_cell(self):
        if len(self.cells) > 1:
            cell_frame, cell_entry, option_var = self.cells[-1]
            cell_frame.destroy()
            del self.cells[-1]

    def calculate(self):
        try:
            total_cfp = len(self.cells)
            self.sum_label.config(text=f"Suma total de Puntos de Función COSMIC (CFP): {total_cfp}")

        except ValueError:
            # Manejo de errores si los cálculos no pueden realizarse
            pass

def main():
    root = tk.Tk()
    app = CosmicCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
