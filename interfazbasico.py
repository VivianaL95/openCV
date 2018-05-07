from tkinter import *
import time

def parpadear():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

def imprimir():
    print("Acabas de presionar el boton imprimir")

def saludar():
    print("Hola " +nombre.get() + " "+ apellido.get() )



ventana = Tk()

#variables
nombre= StringVar()
apellido = StringVar()
numero = IntVar()
opcion = IntVar()
comboVar = StringVar()
comboVar2 = StringVar()

ventana.title('Titulo de la ventana')
ventana.geometry('400x300')
boton = Button(ventana,text="Minimizar",command=parpadear).grid(row=0,column=0)
boton2 = Button(ventana,text="Salir", command=ventana.quit).grid(row=0,column=1)
boton3 = Button(ventana,text="Imprimir", command=imprimir).grid(row=0,column=2)
boton4 = Button(ventana,text="Posicion").grid(row=1,column=1)
boton5 = Button(ventana,text="Saludo",command=saludar).grid(row=4,column=1)

etiqueta= Label(ventana,text="Posicionamiento").grid(row=1,column=0)
etiqueta1= Label(ventana, text="Nombre").grid(row=2,column=0)
etiqueta2= Label(ventana, text="Apellido").grid(row=3,column=0)
etiqueta4= Label(ventana, text="Numero").grid(row=4,column=0)
etiqueta5= Label(ventana, text="Opcion").grid(row=5,column=0)
etiqueta6= Label(ventana, text="Combo").grid(row=6,column=0)
etiqueta7= Label(ventana, text="Combo 2").grid(row=7,column=0)

entrada1 = Entry(ventana,textvariable = nombre).grid(row=2,column=1)
entrada2 = Entry(ventana,textvariable = apellido).grid(row=3,column=1)
entrada4 = Entry(ventana,textvariable = numero).grid(row=4,column=1)

opcion1 = Radiobutton(ventana,text="Femenino",value=1,variable=opcion).grid(row=5,column=1)
opcion2 = Radiobutton(ventana,text="Masculino",value=2,variable=opcion).grid(row=5,column=2)

combo1 = Spinbox(ventana,values=("uno","dos","tres"),textvariable = comboVar).grid(row=6,column=1)
combo2 = Spinbox(ventana,from_=1,to=10,textvariable = comboVar2).grid(row=7,column=1)

ventana.mainloop()