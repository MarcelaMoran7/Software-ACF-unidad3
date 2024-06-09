from tkinter import *
import tkinter as tk
from tkinter import ttk

#autor kevin dominguez 2024

class PuntoDeFuncion():

    # MÉTODO INIT DE LA CLASE PUNTO DE FUNCION
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Estimación de Puntos de Objeto")
        self.root.geometry("1000x700")

        # Crear un canvas y un scrollbar
        self.canvas = tk.Canvas(self.root)
        self.scrollbar_v = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar_h = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
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
        
        #PARTES DE LA VENTANA PRINCIPAL
        self.diseño_punto_sin_ajustar(self.scrollable_frame)
        self.diseño_punto_funcion_ajustado(self.scrollable_frame)
        
        self.frame_respuesta = ttk.Frame(self.scrollable_frame)
        self.frame_respuesta.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        aceptar = Button(self.frame_respuesta, text="Calcular PFA", command=lambda: self.obtener_valores(self.frame_respuesta))
        aceptar.grid(row=0, columnspan=3)
       
    # DISEÑO DE PUNTO DE FUNCIÓN SIN AJUSTAR
    def diseño_punto_sin_ajustar(self, scrollable_frame):
        # Marco Sin Ajustar
        self.marco_sin_ajustar = ttk.LabelFrame(scrollable_frame, text="Punto De Función Sin Ajustar")
        self.marco_sin_ajustar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        subtitulos = ["Entradas Externas (EI)", "Salidas Externas (EO)", "Consultas Externas (EQ)", \
                     "Archivos Logicos I. (ILF)", "Archivos Interfaces E. (EIF)"]
        def etiquetas(fila):
            Label(self.marco_sin_ajustar, text="Simple").grid(row=fila, column=0, padx=(25, 0), pady=0, sticky="w")
            Label(self.marco_sin_ajustar, text="Medio").grid(row=fila, column=1, padx=(25, 0), pady=0, sticky="w")
            Label(self.marco_sin_ajustar, text="Complejo").grid(row=fila, column=2, padx=(25, 0), pady=0, sticky="w")
        
        def crear_entry(fila, rango):
            conteo = 0
            for i in range(rango, rango+3):
                globals()['entry' + str(i)] = Entry(self.marco_sin_ajustar)
                globals()['entry' + str(i)].grid(row=fila, column=conteo, padx=(25, 20), pady=(0,15), sticky="ew")
                conteo += 1
    
        conteo = 0
        for i in range(1, 15, 3):  
            Label(self.marco_sin_ajustar, text=subtitulos[conteo], font=("Helvetica", 14)).grid(row=i, column=0, padx= (10,0), sticky="w", pady=(10,0))
            etiquetas(i+1)
            crear_entry(i+2, i)
            conteo+= 1

    # DISEÑO DE PUNTO DE FUNCIÓN AJUSTADO
    def diseño_punto_funcion_ajustado(self, scrollable_frame):
        # Marco ajustar
        self.marco_ajustado = ttk.LabelFrame(scrollable_frame, text="Factores De Complejidad. peso (0-5)")
        self.marco_ajustado.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        factores = ["1- Respaldo Y Recuperación", "2- Cominucación De Datos", "3- Procesamiento Distribuido", \
                    "4- Rendimiento Crítico", "5- Existencia De Entorno Operativo", "6- Entrada De Datos En Línea", \
                    "7- Transacción De Entrada Sobre Múltiples Pantallas", "8- Archivos Maestros Actualizados En Línea", \
                    "9- Complejo De Valores De Dominio Interno", "10- Complejo De Procesamiento Interno", "11- Código Diseñado Para Reuso", \
                    "12- Conversión/Instalación En Diseño", "13- Instalaciones Múltiples", "14- Aplicación Diseñada Para Cambio"]

        fila = 19
        for i in factores:
            Label(self.marco_ajustado, text= i ).grid(row=fila, column=0, padx=(25, 0), pady=5, sticky="w")
            globals()['entry' + str(fila)] = Entry(self.marco_ajustado)
            globals()['entry' + str(fila)].grid(row=fila, column=1, padx=(25, 5), pady=0, sticky="ew")
            fila += 1
    
    # REALIZA LOS CALCULOS NECESARIOS Y LOS MUESTRA
    def calcular_punto_ajustado(self, ufc, fav, root):
        Label(root, text="PUNTO DE FUNCIÓN AJUSTADO").grid(row=1, columnspan=3, padx=(10, 0), pady=(10, 0))
        Label(root, text="PFA = UFC * [0.65 + (0.01 * FAV)]").grid(row=2, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        Label(root, text="PFA = "+ str(ufc) +" * [0.65 + (0.01 * "+ str(fav) +")]").grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        Label(root, text="PFA = "+ str(ufc) +" * "+ str(0.65 + (0.01 * float(fav)))).grid(row=4, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        Label(root, text="PFA = "+ str(float(ufc) * 0.65 + (0.01 * float(fav)))).grid(row=5, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

    # SE REALIZA TODOS LOS CALCULOS NECESARIOS Y SE LLAMA DESDE EL BOTON CALCULAR PFA
    def obtener_valores(self, frame_respuesta):
        self.valoresDefecto = [3,4,6,4,5,7,3,4,6,7,10,15,5,7,10]
        self.data = []

        for self.i in range(1, 15, 3):
            self.obj = {
                'simple': globals()['entry' + str(self.i)].get(),
                'medio': globals()['entry' + str(self.i+1)].get(),
                'complejo': globals()['entry' + str(self.i+2)].get(),
                'simpleDefecto': self.valoresDefecto[self.i-1],
                'medioDefecto': self.valoresDefecto[self.i],
                'complejoDefecto': self.valoresDefecto[self.i+1]
            }
            self.data.append(self.obj)

        # CALCULAR UFC CON DATOS POR DEFECTO
        self.ufc = 0
        for self.dat in self.data:
            self.multipl = self.dat
            self.ufc = self.ufc + int(self.multipl['simple']) * int(self.multipl['simpleDefecto']) + int(self.multipl['medio']) * int(self.multipl['medioDefecto']) + int(self.multipl['complejo']) * int(self.multipl['complejoDefecto'])
    
        # CALCULAR LA SUMATORIA DE FAV PREGUNTAS DE FACTORES
        self.fav = 0
        for self.i in range(19, 33, 1):
            self.fav = self.fav + int(globals()['entry' + str(self.i)].get())

        self.calcular_punto_ajustado(self.ufc, self.fav, frame_respuesta)