import tkinter as tk
import tkinter.messagebox

class EstimadorMcCall(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Estimación de McCall")
        self.geometry("650x500")

        # Lista de métricas de McCall con sus siglas divididas en dos columnas
        self.metricas_1 = [
            "Facilidad de auditoria (FA)", "Exactitud (EX)", "Estandarizacion de comunicaciones (EC)", 
            "Complecion (CM)", "Complejidad (CX)", "Consisicion (CN)", "Consistencia (CS)", 
            "Estandarizacion de datos (ED)", "Tolerancia al Error (TE)", "Eficiencia de ejecucion (EE)", 
            "Capacidad de expansion (CE)"
        ]
        self.metricas_2 = [
            "Generalidad (GE)", "Independicia de Hardwre (IH)", "Instrumentacion (IN)", "Modularidad (MD)", 
            "Operatividad (OP)", "Seguridad (SG)", "Autodocumentacion (AD)", "Simplicidad (SM)", 
            "Independencia del sistema Software (IS)", "Trazabilidad (TZ)", "Formacion o Entrenamientio (FM)"
        ]

        # Diccionarios para almacenar las entradas de peso
        self.entradas_peso = {}
        self.peso_defecto = 0

        # Crear la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Crear un contenedor para los widgets
        contenedor = tk.Frame(self)
        contenedor.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        # Crear encabezados de la tabla
        tk.Label(contenedor, text="Métrica", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=0, pady=0)
        tk.Label(contenedor, text="Peso (0-10)", font=('Helvetica', 12, 'bold')).grid(row=0, column=1, padx=5, pady=5)

        # Crear una columna para cada conjunto de métricas
        for i, (metrica1, metrica2) in enumerate(zip(self.metricas_1, self.metricas_2), start=1):
            tk.Label(contenedor, text=metrica1).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            tk.Label(contenedor, text=metrica2).grid(row=i, column=2, padx=5, pady=5, sticky=tk.W)

            # Entrada de texto para el peso
            entrada_peso1 = tk.Entry(contenedor, width=5)
            entrada_peso1.grid(row=i, column=1, padx=5, pady=5)
            self.entradas_peso[metrica1] = entrada_peso1

            entrada_peso2 = tk.Entry(contenedor, width=5)
            entrada_peso2.grid(row=i, column=3, padx=5, pady=5)
            self.entradas_peso[metrica2] = entrada_peso2

        # Crear un frame para los botones
        frame_botones = tk.Frame(self)
        frame_botones.grid(row=1, column=0, pady=10)

        # Botón para calcular todos los factores
        boton_calcular = tk.Button(frame_botones, text="Calcular Todos los Factores", command=self.calcular_todos_los_factores, font=('Helvetica', 14, 'bold'))
        boton_calcular.pack(pady=10)

    def obtener_valor_peso(self, metrica):
        valor = self.entradas_peso[metrica].get()
        if valor.strip() == "":
            return 0
        elif not valor.isdigit():
            return -1  # Marcar como valor inválido
        else:
            valor = int(valor)
            if valor < 0 or valor > 10:
                return -1  # Marcar como valor inválido
            else:
                return valor

    def calcular_todos_los_factores(self):
        resultados = []

        for metrica in self.entradas_peso.keys():
            valor = self.obtener_valor_peso(metrica)
            if valor == -1:
                tk.messagebox.showerror("Error", "Por favor, ingrese valores válidos (entre 0 y 10) para todas las métricas.")
                return

                # Calcular cada factor
        resultados.append(("Factor de Corrección", self.calcular_fc()))
        resultados.append(("Factor de Fiabilidad", self.calcular_ff()))
        resultados.append(("Factor de Eficiencia", self.calcular_fe()))
        resultados.append(("Factor de Seguridad", self.calcular_fs()))
        resultados.append(("Factor de Usabilidad", self.calcular_fu()))
        resultados.append(("Factor de Operación", self.calcular_fo()))

        # Mostrar los resultados en una nueva ventana
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, resultados):
        # Crear una nueva ventana para mostrar los resultados
        ventana_resultados = tk.Toplevel(self)
        ventana_resultados.title("Resultados de Estimación")
        ventana_resultados.geometry("400x300")

        # Mostrar los resultados en etiquetas
        for i, (nombre_factor, valor_factor) in enumerate(resultados, start=1):
            tk.Label(ventana_resultados, text=f"{nombre_factor}: {valor_factor:.2f}").pack(pady=5)

    def calcular_fc(self):
        # Calcular el Factor de Corrección
        cm = self.obtener_valor_peso("Complecion (CM)")
        cs = self.obtener_valor_peso("Consistencia (CS)")
        tz = self.obtener_valor_peso("Trazabilidad (TZ)")

        # Calcular el promedio
        fc = (cm + cs + tz) / 3

        return fc

    def calcular_ff(self):
        # Calcular el Factor de Fiabilidad
        ex = self.obtener_valor_peso("Exactitud (EX)")
        cx = self.obtener_valor_peso("Complejidad (CX)")
        cs = self.obtener_valor_peso("Consistencia (CS)")
        te = self.obtener_valor_peso("Tolerancia al Error (TE)")
        md = self.obtener_valor_peso("Modularidad (MD)")
        sm = self.obtener_valor_peso("Simplicidad (SM)")

        # Calcular el promedio
        ff = (ex + cx + cs + te + md + sm) / 6

        return ff

    def calcular_fe(self):
        # Calcular el Factor de Eficiencia
        cn = self.obtener_valor_peso("Consisicion (CN)")
        inn = self.obtener_valor_peso("Instrumentacion (IN)")
        sg = self.obtener_valor_peso("Seguridad (SG)")

        # Calcular el promedio
        fe = (cn + inn + sg) / 3

        return fe

    def calcular_fs(self):
        # Calcular el Factor de Seguridad
        fa = self.obtener_valor_peso("Facilidad de auditoria (FA)")
        inn = self.obtener_valor_peso("Instrumentacion (IN)")
        sg = self.obtener_valor_peso("Seguridad (SG)")

        # Calcular el promedio
        fs = (fa + inn + sg) / 3

        return fs

    def calcular_fu(self):
        # Calcular el Factor de Usabilidad
        op = self.obtener_valor_peso("Operatividad (OP)")
        fm = self.obtener_valor_peso("Formacion o Entrenamientio (FM)")

        # Calcular el promedio
        fu = (op + fm) / 2

        return fu
    
    def calcular_fo(self):
        # Calcular el Factor de Operación
        fc = self.calcular_fc()
        ff = self.calcular_ff()
        fe = self.calcular_fe()
        fs = self.calcular_fs()
        fu = self.calcular_fu()

        # Calcular el promedio
        fo = (fc + ff + fe + fs + fu) / 5

        return fo


if __name__ == "__main__":
    app = EstimadorMcCall()
    app.mainloop()

