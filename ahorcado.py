from tkinter import *
from random import randint

letrasUsadas = []

def probar_letra_funcion():
    letrasUsadas.append(letraObtenida.get())
    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get())>1:
            for i in range(len(palabra)):
                if palabra[i]==letraObtenida.get():
                    guiones[i].config(text=""+letraObtenida.get())
        else:
            guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get())
    #print(letrasUsadas)

raiz = Tk()
archivo = open("palabras.txt","r")
conjuntoPalabras = list(archivo.read().split("\n"))
palabra = conjuntoPalabras[randint(0,len(conjuntoPalabras)-1)].lower()
letraObtenida = StringVar()
raiz.config(width = 1000, height = 600, bg = "blue", relief = "groove", bd = 10)
juegoFrame = Frame(raiz)
juegoFrame.config(width = 1000, height = 600, relief = "sunken", bd = 15)
juegoFrame.grid_propagate(False)
juegoFrame.pack()

Label(juegoFrame, text = "Introduce una letra", font = ("Verdana",24)
      ).grid(row = 0, column = 0, padx = 10, pady = 10)

letra = Entry(juegoFrame, width = 2, font = ("Verdana", 24), textvariable = letraObtenida
              ).grid(row = 0, column = 1, padx = 10, pady = 10)

probar_letra = Button(juegoFrame,text="Probar",bg="orange", command = probar_letra_funcion
                      ).grid(row = 1, column = 0, pady = 10)

guiones = [Label(juegoFrame,text="_",font=("verdana",30)) for _ in palabra]
inicialx=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialx,y=400)
    inicialx+=50
    
raiz.mainloop()
