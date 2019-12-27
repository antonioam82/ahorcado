from tkinter import *

def probar_letra_funcion():
    print(letraObtenida.get())

raiz = Tk()
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
raiz.mainloop()
