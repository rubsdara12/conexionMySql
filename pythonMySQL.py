import tkinter as tk

# importar los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from conexion import *

class FormularioClientes:
    #  declaramos las variables globales para que se puedan reutilizar
    
    global base
    base = None
    
    global textBoxId
    textBOxId = None

    global textBoxNombres
    textBoxNombres = None

    global textBoxApellidos
    textBoxApellidos = None

    global groupBox
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    


def Formulario():
        global textBoxId
        global textBoxNombres
        global textBoxApellidos
        global combo
        global base
        global groupBox
        global tree


        try:
            base = Tk()
            base.geometry("1200x300")  # damos el tamaño de la ventana que se va a crear
            base.title("Formulario Python")  # nombre de la ventana del formulario

            groupBox = LabelFrame(base,text="Datos del Personal", padx=5, pady=5)  # crear el primer contenedor
            groupBox.grid(row=0, column=0, padx=10, pady=10)
            # se crear la etiqueta id
            LabelId= Label(groupBox, text="Id", width=13, font=("arial",12)).grid(row=0,column=0)  # con .grid damos la ubicacion de la etiqueta
            # control donde ingresamos datos por teclado del espacio del id
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0, column=1)

            LabelNombres= Label(groupBox, text="Nombres", width=13, font=("arial",12)).grid(row=1,column=0)
            textBoxNombres = Entry(groupBox)
            textBoxNombres.grid(row=1, column=1)

            LabelApellidos= Label(groupBox, text="Apellidos", width=13, font=("arial",12)).grid(row=2,column=0)
            textBoxApellidos = Entry(groupBox)
            textBoxApellidos.grid(row=2, column=1)

            LabelSexo= Label(groupBox, text="Sexo", width=13, font=("arial",12)).grid(row=3,column=0)
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1)
            # queda fijo en el menu desplegable
            seleccionSexo.set("Masculino")  

            Button(groupBox,text="Guardar",width=10, command=guardarRegistros).grid(row=4, column=0)
            Button(groupBox,text="Modificar",width=10, command=modificarRegistros).grid(row=4, column=1)
            Button(groupBox,text="Eliminar",width=10, command=eliminarRegistros).grid(row=4, column=2)

            # creamos otra casilla o otro contenedor
            groupBox = LabelFrame(base,text="Lista del Personal", padx=5, pady=5)
            groupBox.grid(row=0, column=1, padx=5, pady=5)
            # crear un Treeview


            # configurar las columnas

            tree = ttk.Treeview(groupBox, columns=("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5,)
            tree.column("# 1", anchor=CENTER)  #  se le da ubicacion a las columnas con alineacion
            tree.heading("# 1", text="Id")  # columnas y cabeceras
            
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombres")
            
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellidos")
            
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Sexo")
            
            # agregar los datos a la tabla
            # mostrar la tabla

            for row in CClientes.mostrarClientes():
                 tree.insert("", "end", values=row)

            # ejecuctar la funcion de hacer clic y mostrar el resultado en los Entry
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)


            tree.pack()  #permite que funcione y se visualice el tree

            base.mainloop()  #  permite cerrar la ventana de visualizacion


        except ValueError as error:
            print("Error al Mostrar la interfaz, Error: {}".format(error))

def guardarRegistros():
        global textBoxNombres,textBoxApellidos,combo,groupBox

        try: # verificar si los widgets estan inicializados
            if textBoxNombres is None or textBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return
            nombres = textBoxNombres.get()
            apellidos = textBoxApellidos.get()
            sexo = combo.get()

            CClientes.ingresarClientes(nombres, apellidos, sexo)
            messagebox.showinfo("Informacion","Los datos fueron guardados")

            actualizarTreeView()

            # limpiamos los campos

            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          # borrar todos los elementos actuales del treview
          tree.delete(*tree.get_children())
 
          # obtener los nuevos datos deseados a mostrar
          datos = CClientes.mostrarClientes()

          # inssertar los nuevos datos en el treeview
          for row in CClientes.mostrarClientes():
                 tree.insert("", "end", values=row)
     except ValueError as error:
        print("Error al actualizar la tabla {}".format(error))

def seleccionarRegistro(event):
     try: # obtener el id del elemento seleccionado
          itemSeleccionado = tree.focus()
          
          if itemSeleccionado:
               # obtener los valores de las columnas
            values = tree.item(itemSeleccionado) ['values']

            # establecer los valores en los widgets entry

            textBoxId.delete(0,END)
            textBoxId.insert(0,values[0])

            textBoxNombres.delete(0,END)
            textBoxNombres.insert(0,values[1])

            textBoxApellidos.delete(0,END)
            textBoxApellidos.insert(0,values[2])

            combo.set(values[3])

     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
        global textBoxId,textBoxNombres,textBoxApellidos,combo,groupBox

        try: # verificar si los widgets estan inicializados
            if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return
            
            idUsuario = textBoxId.get()
            nombres = textBoxNombres.get()
            apellidos = textBoxApellidos.get()
            sexo = combo.get()

            CClientes.modificarClientes(idUsuario,nombres, apellidos, sexo)
            messagebox.showinfo("Informacion","Los datos fueron actualizados")

            actualizarTreeView()

            # limpiamos los campos
            textBoxId.delete(0,END)
            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al modificar los datos {}".format(error))

def eliminarRegistros():
        global textBoxId,textBoxNombres,textBoxApellidos

        try: # verificar si los widgets estan inicializados
            if textBoxId is None:
                print("Los widgets no estan inicializados")
                return
            
            idUsuario = textBoxId.get()
            

            CClientes.eliminarClientes(idUsuario)
            messagebox.showinfo("Informacion","Los datos fueron Eliminados")

            actualizarTreeView()

            # limpiamos los campos
            textBoxId.delete(0,END)
            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al modificar los datos {}".format(error))

Formulario()
