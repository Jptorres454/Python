from tkinter import *
from tkinter import ttk

import sqlite3

class rollpay:
    db_name = 'nomina.db'
    
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
        ttk.Button(frame,text = 'Enviar Datos').grid(row = 5, columnspan =2, sticky = W +E)
       
       #Table
        self.tree = ttk. Treeview(height = 10, columns = 2)
        self.tree.grid (row = 5,column = 0, columnspan = 2)  
        self.tree.heading('#0', text = 'Name', anchor = CENTER )
        self.tree.heading('#1', text = 'Document', anchor = CENTER )
        
        self.get_empleado()
        
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_empleado(self):
        query = 'SELECT * FROM empleados ORDER BY Name DESC'
        db_rows = self.run_query(query)
        print(db_rows)
    
if __name__ == '__main__':
    window = Tk()
    rollpay(window)
    window.mainloop()
    