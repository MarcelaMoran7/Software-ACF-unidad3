import tkinter as tk
from tkinter import ttk

class Tabla2:
    def __init__(self, root):
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill='both', expand=True)

        self.tree = ttk.Treeview(self.frame, columns=('Factor tecnico', 'Descripcion', 'Peso', 'Número'), show='headings')
        self.tree.pack(fill='both', expand=True)

        self.tree.heading('Factor tecnico', text='Factor tecnico')
        self.tree.heading('Descripcion', text='Descripcion')
        self.tree.heading('Peso', text='Peso')
        self.tree.heading('Número', text='Número')

        self.tree.column('Factor tecnico', width=150)
        self.tree.column('Descripcion', width=300)
        self.tree.column('Peso', width=100)
        self.tree.column('Número', width=100)

        self.datos = [
            ('E1', 'Familiaridad con el modelo proyectado', 2),
            ('E2', 'Personal tiempo parcial', 1),
            ('E3', 'Capacidad del analista lider', 1),
            ('E4', 'Experiencia en la aplicacion', 1),
            ('E5', 'Experiencia en orientacion a objetos', 1),
            ('E6', 'Motivacion', 0.5),
            ('E7', 'Dificultad de lenguaje de programacion', 0.5),
            ('E8', 'Estabilidad de los requerimientos', 2)
        ]

        for dato in self.datos:
            self.tree.insert('', tk.END, values=(dato[0], dato[1], dato[2], ""))

        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(fill='x', padx=5, pady=5)

        tk.Label(self.input_frame, text="Número (-10-10)").grid(row=0, column=0, padx=5, pady=5)

        self.entry_numero = ttk.Entry(self.input_frame)
        self.entry_numero.grid(row=1, column=0, padx=5, pady=5)

        btn_agregar = ttk.Button(self.input_frame, text="Agregar Número", command=self.agregar_numero)
        btn_agregar.grid(row=1, column=1, padx=5, pady=5)

        btn_sumar = ttk.Button(self.input_frame, text="Sumar Números", command=self.sumar_numeros)
        btn_sumar.grid(row=1, column=2, padx=5, pady=5)

        btn_calcular_tcf = ttk.Button(self.input_frame, text="Calcular ECF", command=self.calcular_ecf)
        btn_calcular_tcf.grid(row=1, column=3, padx=5, pady=5)

        self.error_label = ttk.Label(self.input_frame, text="", foreground="red")
        self.error_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        self.suma_label = ttk.Label(self.input_frame, text="Suma: 0")
        self.suma_label.grid(row=1, column=4, padx=5, pady=5)

        self.tcf_label = ttk.Label(self.input_frame, text="ECF: 0")
        self.tcf_label.grid(row=1, column=5, padx=5, pady=5)

    def agregar_numero(self):
        numero = self.entry_numero.get()
        self.error_label.config(text="")  # Clear previous error message

        if numero:
            try:
                numero = float(numero)
                if -10 <= numero <= 10:
                    selected_item = self.tree.selection()
                    if selected_item:
                        self.tree.set(selected_item, 'Número', numero)
                        self.entry_numero.delete(0, tk.END)
                    else:
                        self.error_label.config(text="Seleccione una fila primero")
                else:
                    self.error_label.config(text="El número debe estar entre -10 y 10")
            except ValueError:
                self.error_label.config(text="El número debe ser un valor numérico")

    def sumar_numeros(self):
        suma = 0.0
        for item in self.tree.get_children():
            numero = self.tree.item(item, 'values')[3]
            if numero:
                try:
                    suma += float(numero)
                except ValueError:
                    pass
        self.suma_label.config(text=f"Suma: {suma}")

    def calcular_ecf(self):
        suma = 0.0
        for item in self.tree.get_children():
            numero = self.tree.item(item, 'values')[3]
            if numero:
                try:
                    suma += float(numero)
                except ValueError:
                    pass
        ecf = 1.4 + (-0.03 * suma)
        self.tcf_label.config(text=f"ECF: {ecf}")
        return ecf

if __name__ == "__main__":
    root = tk.Tk()
    app = Tabla2(root)
    root.mainloop()