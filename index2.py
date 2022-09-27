from tkinter import *

import sqlite3

class rollpay:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Nómina')

        # creamos un contenedor
        frame = LabelFrame(self.wind, text='Reditre un Nuevo Empleado')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Nombre del input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        # Documento imput
        Label(frame, text='Document: ').grid(row=2, column=0)
        self.days = Entry(frame)
        self.days.grid(row=2, column=1)

        # Dias Trabajados imput
        Label(frame, text='Days Workeds: ').grid(row=3, column=0)
        self.days = Entry(frame)
        self.days.grid(row=3, column=1)

        # Pago del empleado imput
        Label(frame, text='Peyment: ').grid(row=4, column=0)
        self.days = Entry(frame)
        self.days.grid(row=4, column=1)

        #BUTTON AGREGAR A UN EMPLEADO
        ttk.Button(frame,text = 'Enviar Datos').grid(row = 3, columnspan =2, sticky = W +E)

        #Table
        this.tree = ttk. Treeview(height = 10, columns = 2)
        this.tree.grid (row = 5,column = 0, columnspan = 2)

if __name__ == '__main__':
    window = Tk()
    rollpay(window)
    window.mainloop()