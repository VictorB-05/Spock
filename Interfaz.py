import tkinter
from cProfile import label
from tkinter import *

import logica
import simbolo

raiz = Tk()
raiz.resizable(width=False, height=False)

raiz.geometry('1000x600')

frame1 = Frame(raiz,width=1000,height=600,bg="#ffb0c8",borderwidth=10,relief="ridge")
frame1.place(x=0,y=0)

Piedra = Button(frame1, width=12, bg="blue", text="Piedra", command=lambda : logica.juego(simbolo.Simbolo.Piedra))
Piedra.place(x=15, y= 400)
Papel = Button(frame1, width=12,bg="blue",text="Papel" ,command=lambda : logica.juego(simbolo.Simbolo.Papel))
Papel.place(x=214, y= 400)
Tijeras = Button(frame1, width=12,bg="blue",text="Tijeras" ,command=lambda : logica.juego(simbolo.Simbolo.Tijeras))
Tijeras.place(x=432, y= 400)
Lagarto = Button(frame1, width=12,bg="blue",text="Lagarto" ,command=lambda : logica.juego(simbolo.Simbolo.Lagarto))
Lagarto.place(x=650, y= 400)
Spok = Button(frame1, width=12,bg="blue",text="Spok" ,command=lambda : logica.juego(simbolo.Simbolo.Spok))
Spok.place(x=858, y= 400)
resultado = tkinter.StringVar()
label1 = Label(frame1,textvariable=resultado, font=("Arial",30))
label1.place(x=0,y=0)
# Esperamos a que la ventana se renderice para medir el ancho
raiz.update()  # Se asegura que los widgets se hayan renderizado

# Imprimimos el tamaño del botón en píxeles
print(Piedra.winfo_width())

raiz.mainloop()
