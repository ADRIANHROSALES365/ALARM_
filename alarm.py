#Una alarma sencilla que pedirá al usuario una fecha y un dia para sonar 
#Importamos tkinter que es una libreria para interfaces graficas de python
#Importamos y decimos que vamos a usar tkinter como tk
from tkinter import *
import tkinter as tk
#importamos el calendario que vamos a usar en la alarma
from calendar_widget import Calendar
#importamos la libreria winsound para el sonido de la alarma
import winsound
#Importamos libreria para el tiempo y fecha
import datetime 
#Importamos una libreria para dar un delay al programa para que no este consumiendo siempre CPU
import time

#Hacemos una variable del tipo tk que es para crear la ventana principal de la aplicacion
app=tk.Tk()
#Creamos el objeto tipo calendario para desplegar en nuestra app
Calendar=Calendar(app)
#Creamos las variables en donde vamos a capturar las entradas del usuario
texto1= tk.StringVar(app)
entrada=tk.StringVar(app)
#Dimensionamos la ventana de nuestra aplicacion ('Ancho x Alto')
app.geometry("300x600")
#Configuramos un color para el fondo
app.config(background="black")
#Cambio el nombre de la ventana llamando el metodo de tk llamado windows manager
tk.Wm.wm_title(app,'Alarma python')

#Creamos una funcion para el boton
def imp():
        print('Hola como estas , todavia no hago lo que me pides')

minutos_totales=0
horas_totales=0

def imprimir_minutos_totales():
       global minutos_totales
       print(minutos_totales)
#Funcion que nos ayuda a incrementar los minutos y a mostrarlos en pantalla
def incrementar_minutos():
            global minutos_totales
            global horas_totales
            if minutos_totales>=0 and minutos_totales<59:
                minutos_totales= minutos_totales+1
                var.set(minutos_totales)
                #print(minutos_totales)
            else:
                minutos_totales=0
                # horas_totales+=1
                var.set(minutos_totales)
                # var2.set(horas_totales)

            return minutos_totales

#Funcion que nos ayuda a decrementar los minutos y a mostrarlos en pantalla
def decrementar_minutos():
            global minutos_totales
            if minutos_totales>0 and minutos_totales<=60:
                minutos_totales= minutos_totales-1
                var.set(minutos_totales)
                #print(minutos_totales)
            else:
                minutos_totales=60
                var.set(minutos_totales)

            return minutos_totales

################################FUNCIONES PARA HORAS#######################
#Funcion para incrementar horas
def incrementar_horas():
       global horas_totales
       if horas_totales>=0 and horas_totales<24:
            horas_totales+=1
            var2.set(horas_totales)
       else:
            horas_totales=0
            var2.set(horas_totales) 

#Funcion para decrementar las horas      
def decrementar_horas():
       global horas_totales
       if horas_totales>0 and horas_totales<=24:
            horas_totales-=1
            var2.set(horas_totales)
       else:
            horas_totales=24
            var2.set(horas_totales) 
def funcion_forever():
      while True:
            getdates()
            time.sleep(2)
      
#Creamos una funcion para extraer la fecha del calendario
def getdates():
    #Comparamos fechas y horas de alarma y actual para saber cuando reproducir el sonido , lo ponemos en un bucle infinito para que siempre este activo
       dia_alarma=str(Calendar.day_num)
       mes_alarma=str(Calendar.month)
       anio_alarma=str(Calendar.year)
    #Obtenemos los datos de la fecha y hora actual
       fecha_ahora=datetime.datetime.now()
       dia_de_hoy=str(fecha_ahora.day)
       mes_actual=str(fecha_ahora.month)
       anio_actual=str(fecha_ahora.year)
       hora_actual=fecha_ahora.hour
       min_actuales=fecha_ahora.minute
       if(dia_alarma==dia_de_hoy and mes_alarma==mes_actual and anio_alarma==anio_actual and horas_totales==hora_actual and minutos_totales ==min_actuales):
            while True:
                frecuency=2500
                duration=1000
                winsound.Beep(frecuency,duration)#Agregue un beep con en un bucle infinito para que una vez que la alarma suene no se detenga hasta que el usuario cierre el programa
                print('Alarm sound!!') 
            
    
 #Se crea una variable para mostrarla en minutos como tipo String Var         
var=tk.StringVar()
var.set(str(minutos_totales))

#Creamos una String var para mostrarla como horas en el label
var2=tk.StringVar()
var2.set(str(horas_totales))

#Creamos nuestra label para Horas
label_horas=tk.Label(
    app,
    textvariable=var2,
    fg='White',
    background='Black',  
    font=("Courier" ,65), #Decimos el tipo de letra y tama;o que tendra el boton 
    justify='center',
).place(x=40 , y=300)


#Creamos nuestra label para Minutos
label_minutos=tk.Label(
    app,
    textvariable=var,
    fg='White',
    background='Black',  
    font=("Courier" ,65),
    justify='center',
).place(x=150, y=300)

#Boton para incrementar la hora 
tk.Button(
    app, #Decimos en que ventana se va a poner este boton
    text=">",
    font=("Courier" ,14), #Decimos el tipo de letra y tama;o que tendra el boton 
    bg='blue', #Decimos el color del fondo del boton
    fg='White', #Decimos el color del texto del boton
    command=incrementar_horas#Esta es la accion que queremos que realice cuando clickemos un boton por lo general se tiene que pasar una funcion pero como objeto no como call

).place(x=100 , y = 420)

#Boton para decrementar la hora 
tk.Button(
    app, #Decimos en que ventana se va a poner este boton
    text="<",
    font=("Courier" ,14), #Decimos el tipo de letra y tama;o que tendra el boton 
    bg='blue', #Decimos el color del fondo del boton
    fg='White', #Decimos el color del texto del boton
    command=decrementar_horas,#Esta es la accion que queremos que realice cuando clickemos un boton por lo general se tiene que pasar una funcion pero como objeto no como call

).place(x=60 , y = 420)

#Boton para incrementar los minutos
tk.Button(
    app, #Decimos en que ventana se va a poner este boton
    text=">",
    font=("Courier" ,14), #Decimos el tipo de letra y tama;o que tendra el boton 
    bg='blue', #Decimos el color del fondo del boton
    fg='White', #Decimos el color del texto del boton
    command=incrementar_minutos,#Esta es la accion que queremos que realice cuando clickemos un boton por lo general se tiene que pasar una funcion pero como objeto no como call

).place(x=220 , y = 420)

#Boton para decrementar los minutos
tk.Button(
    app, #Decimos en que ventana se va a poner este boton
    text="<",
    font=("Courier" ,14), #Decimos el tipo de letra y tama;o que tendra el boton 
    bg='blue', #Decimos el color del fondo del boton
    fg='White', #Decimos el color del texto del boton
    command=decrementar_minutos,#Esta es la accion que queremos que realice cuando clickemos un boton por lo general se tiene que pasar una funcion pero como objeto no como call

).place(x=180 , y = 420)



#Creamos un boton para la aplicacion
tk.Button(
    app, #Decimos en que ventana se va a poner este boton
    text="Set alarm",
    font=("Courier" ,14), #Decimos el tipo de letra y tama;o que tendra el boton 
    bg='blue', #Decimos el color del fondo del boton
    fg='White', #Decimos el color del texto del boton
    command=funcion_forever,#Esta es la accion que queremos que realice cuando clickemos un boton por lo general se tiene que pasar una funcion pero como objeto no como call

).place(x=90 , y = 500)



#Llamamos el metodo minloop para que la aplicacion se este refrescando cada cierto tiempo y nos muestre si hay cambios
app.mainloop()



