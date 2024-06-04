from tkinter import *

#autor kevin dominguez 2024

def mostrar_punto_de_funcion():
    ventana_punto_funcion = Toplevel()
    ventana_punto_funcion.title("Punto de Función")
    ventana_punto_funcion.geometry("800x600")
    
    subtitulos = ["Entradas Externas (EI)", "Salidas Externas (EO)", "Consultas Externas (EQ)", "Archivos Logicos Internos (ILF)", "Archivos De Interfaz Externa (EIF)"]

    def etiquetas(fila):
        Label(ventana_punto_funcion, text="Simple").grid(row=fila, column=0, padx=(25, 0), pady=0, sticky="w")
        Label(ventana_punto_funcion, text="Medio").grid(row=fila, column=1, padx=(25, 0), pady=0, sticky="w")
        Label(ventana_punto_funcion, text="Complejo").grid(row=fila, column=2, padx=(25, 0), pady=0, sticky="w")
        
    Label(ventana_punto_funcion, text="Calcular Punto de Función", font=("Helvetica", 16)).grid(row=0, column=1, sticky="ew", pady=(10,0))

    def crear_entry(fila, rango):
        conteo = 0
        for i in range(rango, rango+3):
            globals()['entry' + str(i)] = Entry(ventana_punto_funcion)
            globals()['entry' + str(i)].grid(row=fila, column=conteo, padx=(25, 5), pady=0, sticky="ew")
            conteo += 1
    
    conteo = 0
    for i in range(1, 15, 3):  
        Label(ventana_punto_funcion, text=subtitulos[conteo], font=("Helvetica", 14)).grid(row=i, column=0, padx= (10,0), sticky="w", pady=(20,0))
        etiquetas(i+1)
        crear_entry(i+2, i)
        conteo+= 1

    def obtener_valores():

        valoresDefecto = [3,4,6,4,5,7,3,4,6,7,10,15,5,7,10]
        data = []

        for i in range(1, 15, 3):
            obj = {
                'simple': globals()['entry' + str(i)].get(),
                'medio': globals()['entry' + str(i+1)].get(),
                'complejo': globals()['entry' + str(i+2)].get(),
                'simpleDefecto': valoresDefecto[i-1],
                'medioDefecto': valoresDefecto[i],
                'complejoDefecto': valoresDefecto[i+1]
            }
            data.append(obj)

        #print(data)
        Label(ventana_punto_funcion, text="UFC = " + str(multiplicar(data))).grid(row=17, column=0, padx=(25, 0), pady=0, sticky="w")
        #print(multiplicar(data))

    def multiplicar(data):
        suma = 0
        for dat in data:
            multipl = dat
            suma = suma + int(multipl['simple']) * int(multipl['simpleDefecto']) + int(multipl['medio']) * int(multipl['medioDefecto']) + int(multipl['complejo']) * int(multipl['complejoDefecto'])
        return suma

    aceptar = Button(ventana_punto_funcion, text="Calcular PFSA", command=obtener_valores)
    aceptar.grid(row=16, column=0, padx=(25,0), pady=(30,0), sticky="w")
