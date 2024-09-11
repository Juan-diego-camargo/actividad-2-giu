import tkinter as tk
from tkinter import messagebox
from Clases.Personas import Personas

class FrmPersonas:
    
   
def __init__(self, root):
        self.root = root
        self.root.title(
        self.root = root
        self.root.title

        self.root = root
        self.root

        self.root = root
       

        self.root = root

        self.root =

        self.root

        self

       
"Formulario de Personas")

        

       


# Crear una instancia de la clase Personas
        self.personas = Personas()

        
        self.personas = Personas()

       

        self.personas = Personas()


        self.personas = Personas

        self.personas =

        self.personas

        self.person

       
# Crear los campos de texto y etiquetas
        self.label_nombre = tk.Label(root, text=
        self.label_nombre = tk.Label(root, text

        self.label_nombre = tk

        self.label_nombre =

        self.label_nombre

        self.label

        self
"Nombre:")
        self.label_nombre.grid(row=
        self.label_nombre.grid(row=

        self.label_nombre.grid

        self.label_nombre

        self.label

       
0, column=0)

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=


        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row


        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid


        self.entry_nombre = tk.Entry(root)
        self.entry


        self.entry_nombre = tk.Entry(root)
       


        self.entry_nombre = tk.Entry(root)


        self.entry_nombre = tk.Entry


        self.entry_nombre =


        self.entry_nombre


        self.entry


       
0, column=1)

        self.label_apellido = tk.Label(root, text=

        self.label_apellido = tk.Label(root,


        self.label_apellido = tk.Label(root


        self.label_ap


   


"Apellido:")
        self.label_apellido.grid(row=
        self.label_apellido.grid(row=

        self.label_apellido.grid(row

        self.label_apellido.grid

        self.label_apellido

        self.label_ap

        self.label

        self

       
1, column=0)

        self.entry_apellido = tk.Entry(root)
        self.entry_apellido.grid(row=

        self.entry_apellido = tk.Entry(root)
        self.entry_apellido.grid(row=


        self.entry_apellido = tk.Entry(root)
        self.entry_apellido.grid(row


        self.entry_apellido = tk.Entry(root)
        self.entry_apellido


        self.entry_apellido = tk.Entry(root)
        self.entry_ap


        self.entry_apellido = tk.Entry(root)
        self


        self.entry_apellido = tk.Entry(root)
       


        self.entry_apellido = tk.Entry(root)


        self.entry_apellido = tk.Entry


        self.entry_apellido = tk


        self.entry_apellido


        self.entry_ap


        self.entry


        self


       


1, column=1)

        self.label_direccion = tk.Label(root, text=

        self.label_direccion = tk.Label(root, text


        self.label_direccion = tk.Label(root,


        self.label_direccion = tk.Label


        self.label_direccion = tk


        self.label_direccion


        self.label_d


        self.label


       


"Dirección:")
        self.label_direccion.grid(row=
        self.label_direccion.grid(row

        self.label_direccion.grid

        self.label_d

        self
2, column=0)

        self.entry_direccion = tk.Entry(root)
        self.entry_direccion.grid(row=

        self.entry_direccion = tk.Entry(root)
        self.entry_direccion.grid(row=


        self.entry_direccion = tk.Entry(root)
        self.entry_direccion.grid(row


        self.entry_direccion = tk.Entry(root)
        self.entry_direccion.grid


        self.entry_direccion = tk.Entry(root)
        self.entry_direccion


        self.entry_direccion = tk.Entry(root)
        self.entry_d


        self.entry_direccion = tk.Entry(root)
        self.entry


        self.entry_direccion = tk.Entry(root)
        self


        self.entry_direccion = tk.Entry(root)
       


        self.entry_direccion = tk.Entry(root)


        self.entry_direccion = tk.Entry(root


        self.entry_direccion = tk.Entry


        self.entry_direccion = tk


        self.entry_direccion


        self.entry_d


        self


2, column=1)

        self.label_edad = tk.Label(root, text=

        self.label_edad = tk.Label(root, text


        self.label_edad = tk.Label(root,


        self.label_edad = tk.Label


        self.label_edad = tk


        self.label_edad =


        self.label_edad


        self.label


        self


       


"Edad:")
        self.label_edad.grid(row=
        self.label_edad.grid(row=

        self.label_edad.grid

        self.label_

        self.label

       
3, column=0)

        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid(row=

        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid(row=


        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid(row


        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid


        self.entry_edad = tk.Entry(root)
        self.entry_edad


        self.entry_edad = tk.Entry(root)
        self.entry_


        self.entry_edad = tk.Entry(root)
        self


        self.entry_edad = tk.Entry(root)
       


        self.entry_edad = tk.Entry(root)


        self.entry_edad = tk.Entry(root


        self.entry_edad = tk.Entry


        self.entry_edad = tk


        self.entry_edad =


        self.entry_edad


        self.entry


        self


3, column=1)

        

       


# Botón para guardar los datos
        self.btn_guardar = tk.Button(root, text=
        self.btn_guardar = tk.Button(root

        self.btn_guardar = tk.Button

        self.btn_guardar = tk

        self.btn_guardar =

        self.btn_guardar

        self.btn_guard

        self.btn

       
"Guardar", command=self.guardar_persona)
        self.btn_guardar.grid(row=
        self.btn_guardar.grid(row=

        self.btn_guardar.grid(row

        self.btn_guardar

        self.btn_guard

        self.btn

       
4, column=1)

    

   


# Método para guardar los datos de la persona
    def guardar_persona(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad = self.entry_edad.get()

        
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad = self.entry_edad.get

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad = self.entry_edad

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad = self.entry

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad = self

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad =

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        edad

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
       

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_d

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion =

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
       

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido

        nombre = self.entry_nombre.get()
        apellido = self.entry

        nombre = self.entry_nombre.get()
        apellido =

        nombre = self.entry_nombre.get()
        apellido

        nombre = self.entry_nombre.get()

        nombre = self.entry_nombre.get

        nombre = self.entry_nombre

        nombre = self

        nombre =

        nombre

       
# Validar que todos los campos estén llenos
        
       
if not (nombre and apellido and direccion and edad):
            messagebox.showerror(
            messagebox.showerror

            message

           
"Error", "Todos los campos son obligatorios")
            
           
return

        

       


# Llamar a la función agregar_persona de la clase Personas
        self.personas.agregar_persona(nombre, apellido, direccion, edad)

        
        self.personas.agregar_persona(nombre, apellido, direccion, edad)

       

        self.personas.agregar_persona(nombre, apellido, direccion,

        self.personas.agregar_persona(nombre, apellido,

        self.personas.agregar_persona(nombre, apellido

        self.personas.agregar_persona(nombre,

        self.personas.agregar_persona(nombre

        self.personas.agregar_persona

        self.personas.agregar_person

        self.personas.ag

        self
# Mostrar un mensaje de éxito
        messagebox.showinfo(
        messagebox.showinfo

        messagebox

       
"Éxito", "Persona guardada exitosamente")

        

       


# Limpiar los campos
        self.entry_nombre.delete(
        self.entry_nombre.delete(

        self.entry_nombre.delete

        self.entry
0, tk.END)
        self.entry_apellido.delete(
        self.entry_apellido.delete(

        self.entry_apellido.delete

        self.entry_apellido

        self.entry_ap

        self.entry

        self

       
0, tk.END)
        self.entry_direccion.delete(
        self.entry_direccion.delete

        self.entry_direccion

        self.entry_d

        self.entry

        self

       
0, tk.END)
        self.entry_edad.delete(
        self.entry_edad.delete(

        self.entry_edad.delete

        self.entry_

        self.entry

       
0, tk.END)

        

       


# Puedes imprimir la lista de personas para verificar los datos
        print(self.personas.obtener_lista_personas())

# Código para ejecutar la ventana del formulario
if __name__ == "__main__":
    root = tk.Tk()
    app = FrmPersonas(root)
    root.mainloop()

    root = tk.Tk()
    app = FrmPersonas(root)
    root.mainloop()
``

    root = tk.Tk()
    app = FrmPersonas(root)
    root.mainloop

    root = tk.Tk()
    app = FrmPersonas(root)
   

    root = tk.Tk()
    app = FrmPersonas(root)

    root = tk.Tk()
    app = FrmPersonas(root

    root = tk.Tk()
    app = FrmPersonas

    root = tk.Tk()
    app = Frm

    root = tk.Tk()
    app =

    root = tk.Tk()
    app

    root = tk.Tk()
   

    root = tk.Tk

    root = tk.T

    root = tk

    root =

    root
    