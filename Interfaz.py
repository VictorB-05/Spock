import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import simbolo
from Logica import logica

#Ventana
raiz = Tk()
raiz.resizable(width=False, height=False)
raiz.geometry('1000x600')

def juego(opcion,logica):
    numero_aleatorio = random.randint(1, 5)
    cpu = simbolo.Simbolo(numero_aleatorio)
    print(cpu.name)
    rel = opcion.comparar(cpu)
    if rel == 1:
        resultado.set("Has ganado")
        jugada.set(f"{opcion.name} ganan a {cpu.name}")
        logica.ganaJ()
    elif rel == -1:
        resultado.set("Has perdido")
        jugada.set(f"{cpu.name} ganan a {opcion.name}")
        logica.ganaCpu()
    else:
        resultado.set("Empate")
        jugada.set(f"{opcion.name} y {cpu.name} es ")
    puntuacion.set(logica)
    if logica.fin():
        ganar(logica)

def ganar(logica):
    # Crear una ventana secundaria
    nueva_ventana = tk.Toplevel(raiz)
    nueva_ventana.title("GIF Animado")
    nueva_ventana.geometry("500x400")
    framegif = Frame(nueva_ventana,bg="#00ffff")
    framegif.pack(fill="both", expand=True)
    if logica.ganar():
        gif_path = "resources/win.gif"
        tiempo = 24
    else:
        gif_path = "resources/perder.gif"
        tiempo = 36
    # Cargar el GIF
    gif = Image.open(gif_path)

    # Crear el Label para mostrar el GIF
    label = tk.Label(framegif)

    label = tk.Label(framegif, bg="#00ffff")
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Función para actualizar los frames del GIF
    def actualizar_frame(index):
        try:
            gif.seek(index)
            img_tk = ImageTk.PhotoImage(gif)
            label.config(image=img_tk)
            label.image = img_tk  # Necesario para mantener la referencia
            nueva_ventana.after(tiempo, actualizar_frame, index + 1)  # tiempo a 24 ya que esta a 24 frames por segundo
        except EOFError:
            # Reiniciar la animación cuando se llega al final
            actualizar_frame(0)

    # Iniciar la animación
    actualizar_frame(0)


#frame donde se posicionan las cosas
frame1 = Frame(raiz,width=1000,height=600,bg="#ffb0c8",borderwidth=10,relief="ridge")
frame1.place(x=0,y=0)

#logica del tres en raya
logica = logica()

#botones para jugar
Piedra = Button(frame1, width=12, bg="blue", text="Piedra", command=lambda : juego(simbolo.Simbolo.Piedra,logica))
Piedra.place(x=15, y= 400)
Papel = Button(frame1, width=12,bg="blue",text="Papel" ,command=lambda : juego(simbolo.Simbolo.Papel,logica))
Papel.place(x=214, y= 400)
Tijeras = Button(frame1, width=12,bg="blue",text="Tijeras" ,command=lambda : juego(simbolo.Simbolo.Tijeras, logica))
Tijeras.place(x=432, y= 400)
Lagarto = Button(frame1, width=12,bg="blue",text="Lagarto" ,command=lambda : juego(simbolo.Simbolo.Lagarto, logica))
Lagarto.place(x=650, y= 400)
Spock = Button(frame1, width=12, bg="blue", text="Spok", command=lambda: juego(simbolo.Simbolo.Spock,logica))
Spock.place(x=858, y= 400)
#labels para dar resultados
resultado = tk.StringVar()
resultado.set("inicio")
label1 = Label(frame1,textvariable=resultado, font=("Arial",30))

jugada = tk.StringVar()
jugada.set("-------------")
ljugada = Label(frame1,textvariable=jugada, font=("Arial",20))


puntuacion = tk.StringVar()
puntuacion.set("0-0")
lpuntuacion = Label(frame1,textvariable=puntuacion, font=("Arial",30))

label1.place(x=300,y=200,width=400)
ljugada.place(x=300,y=170,width=400)
lpuntuacion.place(x=300,y=120,width=400)

raiz.mainloop()

