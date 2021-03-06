from tkinter import *
from random import randint
from tkinter.messagebox import *

letrasUsadas = []

vidas = 7
letrasacertadas = 0

def horca():
    global canvas
    canvas = Canvas(raiz, width=300, height=360)
    canvas.place(x=655,y=100)
    canvas.create_line(0,350,300,350)
    canvas.create_line(300,0,300,350)
    canvas.create_line(300,30,100,10)

def horca_avan(v):
    if v == 6:
        canvas.create_line(100,0,100,80)
    elif v == 5:
        canvas.create_oval(139,80,59,160)
    elif v == 4:
        canvas.create_line(100,160,100,230)
    elif v == 3:
        canvas.create_line(100,210,130,170)
    elif v == 2:
        canvas.create_line(100,210,60,195)
    elif v == 1:
        canvas.create_line(100,230,40,280)
    elif v == 0:
        canvas.create_line(100,230,100,280)
        
        

def colocarLetras():
    x=50
    y=150
    count = 0
    Label(juegoFrame,text="Letras sin usar").place(x=50,y=100)
    for i in range(26):
        count+=1
        letrasLabel[i].place(x=x,y=y)
        x+=30
        if count==5:
            y+=35
            count=0
            x=50

def probar_letra_funcion():
    global vidas, letrasacertadas
    letrasUsadas.append(letraObtenida.get())
    letrasLabel[ord(letraObtenida.get())-97].config(text="")
    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get())>1:
            letrasacertadas+=palabra.count(letraObtenida.get())
            for i in range(len(palabra)):
                if palabra[i]==letraObtenida.get():
                    guiones[i].config(text=""+letraObtenida.get())
        else:
            letrasacertadas+=1
            guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get())
        if letrasacertadas == len(palabra):
            showwarning(title="Victoria",message="Has ganado")
    else:
        vidas-=1
        horca_avan(vidas)
        if vidas == 0:
            showwarning(title="Derrota",message="Juego terminado")
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
letrasLabel = [Label(juegoFrame,text=chr(j+97),font=("Verdana",20)) for j in range(26)]
colocarLetras()
guiones = [Label(juegoFrame,text="_",font=("verdana",30)) for _ in palabra]
inicialx=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialx,y=400)
    inicialx+=50

horca()    
raiz.mainloop()
