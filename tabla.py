import tkinter as tk
from tkinter import ttk

class Tabla:
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
            ('T1', 'Sistema distribuido', 2),
            ('T2', 'Rendimiento o tiempo de respuesta', 1),
            ('T3', 'Eficiencia del usuario final', 1),
            ('T4', 'Procesamiento interno complejo', 1),
            ('T5', 'El código debe ser reutilizable', 1),
            ('T6', 'Facilidad de instalación', 0.5),
            ('T7', 'Facilidad de uso', 0.5),
            ('T8', 'Portabilidad', 2),
            ('T9', 'Facilidad de cambio', 1),
            ('T10', 'Concurrencia', 1),
            ('T11', 'Características especiales de seguridad', 1),
            ('T12', 'Provee acceso directo a terceras partes', 1),
            ('T13', 'Se requieren facilidades especiales de entrenamiento a usuario', 1),
        ]

        for dato in self.datos:
            self.tree.insert('', tk.END, values=(dato[0], dato[1], dato[2], ""))

        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(fill='x', padx=5, pady=5)

        tk.Label(self.input_frame, text="Número (0-5)").grid(row=0, column=0, padx=5, pady=5)

        self.entry_numero = ttk.Entry(self.input_frame)
        self.entry_numero.grid(row=1, column=0, padx=5, pady=5)

        btn_agregar = ttk.Button(self.input_frame, text="Agregar Número", command=self.agregar_numero)
        btn_agregar.grid(row=1, column=1, padx=5, pady=5)

        btn_sumar = ttk.Button(self.input_frame, text="Sumar Números", command=self.sumar_numeros)
        btn_sumar.grid(row=1, column=2, padx=5, pady=5)

        btn_calcular_tcf = ttk.Button(self.input_frame, text="Calcular TCF", command=self.calcular_tcf)
        btn_calcular_tcf.grid(row=1, column=3, padx=5, pady=5)

        self.error_label = ttk.Label(self.input_frame, text="", foreground="red")
        self.error_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        self.suma_label = ttk.Label(self.input_frame, text="Suma: 0")
        self.suma_label.grid(row=1, column=4, padx=5, pady=5)

        self.tcf_label = ttk.Label(self.input_frame, text="TCF: 0")
        self.tcf_label.grid(row=1, column=5, padx=5, pady=5)

    def agregar_numero(self):
        numero = self.entry_numero.get()
        self.error_label.config(text="")  # Clear previous error message

        if numero:
            try:
                numero = float(numero)
                if 0 <= numero <= 5:
                    selected_item = self.tree.selection()
                    if selected_item:
                        self.tree.set(selected_item, 'Número', numero)
                        self.entry_numero.delete(0, tk.END)
                    else:
                        self.error_label.config(text="Seleccione una fila primero")
                else:
                    self.error_label.config(text="El número debe estar entre 0 y 5")
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

    def calcular_tcf(self):
        suma = 0.0
        for item in self.tree.get_children():
            numero = self.tree.item(item, 'values')[3]
            if numero:
                try:
                    suma += float(numero)
                except ValueError:
                    pass
        tcf = 0.6 + (0.01 * suma)
        self.tcf_label.config(text=f"TCF: {tcf}")
        return tcf

if __name__ == "__main__":
    root = tk.Tk()
    app = Tabla(root)
    root.mainloop()
