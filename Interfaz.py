import random
import tkinter
from tkinter import *
import simbolo


def juego(opcion):
    numero_aleatorio = random.randint(1, 5)
    cpu = simbolo.Simbolo(numero_aleatorio)
    print(cpu.name)
    rel = opcion.comparar(cpu)
    if rel == 1:
        resultado.set("Has ganado")
        jugada.set(f"{opcion.name} ganan a {cpu.name}")
    elif rel == -1:
        resultado.set("Has perdido")
        jugada.set(f"{cpu.name} ganan a {opcion.name}")
    else:
        resultado.set("Empate")
        jugada.set(f"{opcion.name} y {cpu.name} es ")


raiz = Tk()
raiz.resizable(width=False, height=False)

raiz.geometry('1000x600')

frame1 = Frame(raiz,width=1000,height=600,bg="#ffb0c8",borderwidth=10,relief="ridge")
frame1.place(x=0,y=0)

#botones para jugar
Piedra = Button(frame1, width=12, bg="blue", text="Piedra", command=lambda : juego(simbolo.Simbolo.Piedra))
Piedra.place(x=15, y= 400)
Papel = Button(frame1, width=12,bg="blue",text="Papel" ,command=lambda : juego(simbolo.Simbolo.Papel))
Papel.place(x=214, y= 400)
Tijeras = Button(frame1, width=12,bg="blue",text="Tijeras" ,command=lambda : juego(simbolo.Simbolo.Tijeras))
Tijeras.place(x=432, y= 400)
Lagarto = Button(frame1, width=12,bg="blue",text="Lagarto" ,command=lambda : juego(simbolo.Simbolo.Lagarto))
Lagarto.place(x=650, y= 400)
Spock = Button(frame1, width=12, bg="blue", text="Spok", command=lambda: juego(simbolo.Simbolo.Spock))
Spock.place(x=858, y= 400)
#labels para dar resultados
resultado = tkinter.StringVar()
resultado.set("inicio")
label1 = Label(frame1,textvariable=resultado, font=("Arial",30))

jugada = tkinter.StringVar()
jugada.set("-------------")
ljugada = Label(frame1,textvariable=jugada, font=("Arial",20))

label1.place(x=300,y=200,width=400)
ljugada.place(x=300,y=170,width=400)

raiz.mainloop()

