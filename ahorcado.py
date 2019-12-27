from tkinter import *

raiz = Tk()
raiz.config(width = 1000, height = 600, bg = "blue", relief = "groove", bd = 10)
juegoFrame = Frame(raiz)
juegoFrame.config(width = 1000, height = 600, relief = "sunken", bd = 15)
juegoFrame.grid_propagate(False)
juegoFrame.pack()

Label(juegoFrame, text = "Introduce una letra", font = ("Verdana",24)
      ).grid(row = 0, column = 0, padx = 10, pady = 10)

letra = Entry(juegoFrame, width = 1, font = ("Verdana", 24)
              ).grid(row = 0, column = 1, padx = 10, pady = 10)
raiz.mainloop()
