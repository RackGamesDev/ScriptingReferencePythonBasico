from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from io import open
import pickle
raiz = Tk()
raiz.title("TexTill - Vacío")
raiz.geometry("1280x750")
raiz.resizable(False,False)
raiz.iconbitmap("icono.ico")
frame=Frame(raiz)
frame.pack(fill="both", expand="True")
corriendo=True
rutaarchivo=""
infotexto=StringVar(frame)
buscalo=StringVar(frame)

class Archivo:
    def __init__(self):
        self.textoTotal=""
        self.nombre=""

def Reset():
    print(cajabase.get("1.0",END))
    opcion=messagebox.askyesno("Reset", "Esto eliminará todo lo escrito hasta ahora. ¿Estás seguro?")
    if opcion==True:
        cajabase.delete(1.0, END)
        cajabase.insert(END, "")
    Actualizar(0)

def EscribirNormal(ruta):
    arc=open(ruta,"w")
    arc.write(cajabase.get("1.0",'end-1c'))
    arc.close()
    print(ruta)

def EscribirSerial(ruta):
    arc=open(ruta,"wb")
    pickle.dump(str(cajabase.get("1.0",'end-1c')), arc)
    arc.close()
    print(ruta)

def LeerNormal(ruta):
    Reset()
    try:
        arc=open(ruta, "r")
        cajabase.insert(END, arc.read())
        arc.close()
    except:
        messagebox.showerror("ERROR", "No se ha podido abrir el archivo.")
    arc=open()
    print(ruta)

def LeerSerial(ruta):
    Reset()
    try:
        arc=open(ruta, "rb")
        cajabase.insert(END, pickle.load(arc))
        arc.close()
    except:
        messagebox.showerror("ERROR", "No se ha podido abrir el archivo.")
    arc=open()
    print(ruta)




def Guardar():
    global rutaarchivo
    if rutaarchivo == "":
        GuardarComo()
    else:
        EscribirNormal(rutaarchivo)
    Actualizar(0)

def GuardarComo():
    global rutaarchivo
    #rutaarchivo=filedialog.askdirectory(title="Guardar en:")
    rutaarchivo=filedialog.asksaveasfilename(title="Guardar en:", filetypes=(("Texto plano", "*.txt"),("Ver todo","*.*")))
    if rutaarchivo!="": 
        EscribirNormal(rutaarchivo)
    Actualizar(0)

def GuardarComoSerializado():
    global rutaarchivo
    rutaarchivo=filedialog.asksaveasfilename(title="Guardar en:", filetypes=(("Información serializada", "*.bin"),("Ver todo","*.*")))
    if rutaarchivo == "":
        GuardarComoSerializado()
    else:
        EscribirSerial(rutaarchivo)
        pass
    Actualizar(0)
    
def GuardarSerializado():
    global rutaarchivo
    if rutaarchivo == "":
        GuardarComoSerializado()
    else:
        EscribirSerial(rutaarchivo)
    Actualizar(0)
    
def Abrir():
    global rutaarchivo
    cual=filedialog.askopenfilename(title="Abrir texto plano", filetypes=(("Texto plano", "*.txt"),("Ver todo","*.*")))
    if cual!="":
        rutaarchivo=cual
        LeerNormal(cual)
    Actualizar(0)

def AbrirSerializado():
    global rutaarchivo
    cual=filedialog.askopenfilename(title="Abrir archivo binario", filetypes=(("Información serializada", "*.bin"),("Ver todo","*.*")))
    if cual!="":
        rutaarchivo=cual
        LeerSerial(cual)
    Actualizar(0)

def Cerrar():
    global corriendo
    opcion=messagebox.askyesno("Cerrar", "Si cierras el programa perderás todo tu progreso que no hayas guardado. ¿Estás seguro?")
    if opcion==True:
        corriendo=False
        raiz.destroy()

def SeleccionarTodo():
    messagebox.showinfo("Info", "Para seleccionar todo puedes pulsar Ctrl+A")
    Actualizar(0)

def SeleccionarNada():
    messagebox.showinfo("Info", "Para no seleccionar nada puedes pulsar Ctrl+D o hacer click en algún lado")
    Actualizar(0)

def Deshacer():
    messagebox.showinfo("Info", "Para deshacer tus cambios puedes pulsar Ctrl+Z")
    Actualizar(0)

def Rehacer():
    messagebox.showinfo("Info", "Para rehacer tus cambios puedes pulsar Ctrl+Y")
    Actualizar(0)

def Copiar():
    messagebox.showinfo("Info", "Para copiar texto puedes pulsar Ctrl+C")
    Actualizar(0)

def Pegar():
    messagebox.showinfo("Info", "Para pegar texto puedes pulsar Ctrl+V")
    Actualizar(0)

def Cortar():
    messagebox.showinfo("Info", "Para cortar texto puedes pulsar Ctrl+X")
    Actualizar(0)

def Ajustes():
    messagebox.showwarning("Ajustes", "No hay nada que ajustar xd")
    Actualizar(0)

def PonerTodoMinusculas():
    tx=cajabase.get("1.0",'end-1c').lower()
    cajabase.delete("1.0", END)
    cajabase.insert(END, tx)#asdfasdfsadfas dinsertttttttttttttt
    Actualizar(0)

def PonerSeleccionMinusculas():
    tx=cajabase.get(SEL_FIRST, SEL_LAST).lower()
    cajabase.delete(SEL_FIRST, SEL_LAST)
    cajabase.insert(INSERT, tx)
    Actualizar(0)

def PonerTodoMayusculas():
    tx=cajabase.get("1.0",'end-1c').upper()
    cajabase.delete("1.0", END)
    cajabase.insert(END, tx)
    Actualizar(0)

def PonerSeleccionMayusculas():
    tx=cajabase.get(SEL_FIRST, SEL_LAST).upper()
    cajabase.delete(SEL_FIRST, SEL_LAST)
    cajabase.insert(INSERT, tx)
    Actualizar(0)

def CapitalizarTodo():
    tx=cajabase.get("1.0",'end-1c').capitalize()
    cajabase.delete("1.0", END)
    cajabase.insert(END, tx)
    Actualizar(0)

def CapitalizarSeleccion():
    tx=cajabase.get(SEL_FIRST, SEL_LAST).capitalize()
    cajabase.delete(SEL_FIRST, SEL_LAST)
    cajabase.insert(INSERT, tx)
    Actualizar(0)

def ContarSecuencia():
    messagebox.showwarning("Aviso", "La secuencia de carácteres que se contará en el texto será la del texto introducido abajo, y se contará en todo el documento")
    messagebox.showinfo("Resultado:", "La secuencia <" + str(buscalo.get()) + "> apareció en el texto " + str(cajabase.get("1.0",'end-1c').count(buscalo.get())) + " veces.")
    Actualizar(0)

def EncontrarIndice():
    messagebox.showwarning("Aviso", "La secuencia de carácteres que se buscará en el texto será la del texto introducido abajo, y se buscará en todo el documento")
    messagebox.showinfo("Resultado:", "La secuencia de carácteres <" + str(buscalo.get()) + "> apareció por primera vez en el carácter número " + str(cajabase.get("1.0",'end-1c').find(buscalo.get())) + ".")
    Actualizar(0)

def CombprobarDigitos():
    if cajabase.get("1.0",'end-1c').isdigit():
        messagebox.showinfo("Sí", "Lo introducido en el texto son dígitos y puede ser computado")
    else:
        messagebox.showinfo("No", "El texto también contiene carácteres no computables")
    Actualizar(0)

def Info():
    messagebox.showinfo("Info", "Un mierdiprogramilla de editor de texto con alguna que otra opción interesante como buscar")
    Actualizar(0)

def Ayuda():
    messagebox.showinfo("Ayuda", "Ninguna te jodes")
    Actualizar(0)

def Pagina():
    messagebox.showinfo("Ir a la página", "Vamos")
    Actualizar(0)

def Estadisticas():
    messagebox.showinfo("Estadísticas", "Puedes ver las estadísticas del texto más abajo, las cuales son: (" + infotexto.get() + ").")
    Actualizar(0)

def Actualizar(directo):
    print("actualizar")
    if directo==1:
        messagebox.showinfo("Info", "Actualizando...")
    base = cajabase.get("1.0",'end-1c')
    cantcar=len(base)
    cantpall=base.split()
    cantpal=len(cantpall)
    if cajabase.tag_ranges(SEL):
        sbase = cajabase.get(SEL_FIRST, SEL_LAST)
        scantcar=len(sbase)
        scantpall=sbase.split()
        scantpal=len(scantpall)
    else:
        scantpal=0
        scantcar=0
    infotexto.set("| Carácteres={} | Carácteres en selección={} | Palabras={} | Palabras en selección={} |".format(str(cantcar), str(scantcar), str(cantpal), str(scantpal)))
        


cajabase=Text(frame, height=42, width=157)
#cajabase.pack(fill="both", expand="True")
cajabase.grid(row=0, column=0, sticky="nsew")#
cajabase.focus_set()
scrolly=Scrollbar(frame, command=cajabase.yview)
#scrolly.pack()
scrolly.grid(row=0, column=1, sticky="nsew")#
cajabase.config(yscrollcommand=scrolly.set, )

infoinferior=Entry(frame, textvariable=infotexto, state="readonly", width=40)
#infoinferior.pack(anchor="w")
infoinferior.grid(row=1, column=0, sticky="nsew")#
botonact=Button(frame, text="Actualizar", command=lambda:Actualizar(1))
botonact.grid(row=2,column=1, sticky="nsew")
infotexto.set("Carácteres=0 | Carácteres en selección=0 | Palabras=0 | Palabras en selección=0 | ")

textobuscar=Entry(frame, textvariable=buscalo, width=40)
textobuscar.grid(row=2, column=0, sticky="nsew")
buscalo.set("Secuencia")

menu=Menu(frame)
raiz.config(menu=menu)
submenuArchivo=Menu(menu, tearoff=0)
submenuEditar=Menu(menu, tearoff=0)
submenuHerramientas=Menu(menu, tearoff=0)
submenuAyuda=Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=submenuArchivo)
menu.add_cascade(label="Editar", menu=submenuEditar)
menu.add_cascade(label="Herramientas", menu=submenuHerramientas)
menu.add_cascade(label="Ayuda", menu=submenuAyuda)
submenuArchivo.add_command(label="Abrir archivo", command=Abrir)
submenuArchivo.add_command(label="Abrir archivo serializado", command=AbrirSerializado)
submenuArchivo.add_command(label="Guardar archivo", command=Guardar)
submenuArchivo.add_command(label="Guardar archivo como", command=GuardarComo)
submenuArchivo.add_command(label="Guardar archivo serializando como", command=GuardarComoSerializado)
submenuArchivo.add_separator()
submenuArchivo.add_command(label="Cerrar", command=Cerrar)
submenuArchivo.add_command(label="Reset", command=Reset)
submenuEditar.add_command(label="Seleccionar todo (ctrl+a)", command=SeleccionarTodo)
submenuEditar.add_command(label="Seleccionar nada (ctrl+d)", command=SeleccionarNada)
submenuEditar.add_separator()
submenuEditar.add_command(label="Deshacer (ctrl+z)", command=Deshacer)
submenuEditar.add_command(label="Rehacer (ctrl+z)", command=Rehacer)
submenuEditar.add_separator()
submenuEditar.add_command(label="Copiar (ctrl+c)", command=Copiar)
submenuEditar.add_command(label="Pegar (ctrl+v)", command=Pegar)
submenuEditar.add_command(label="Cortar (ctrl+x)", command=Cortar)
submenuEditar.add_separator()
submenuEditar.add_command(label="Ajustes", command=Ajustes)
submenuEditar.add_command(label="Actualizar", command=lambda:Actualizar(1))
submenuHerramientas.add_command(label="Poner todo en minúsculas", command=PonerTodoMinusculas)
submenuHerramientas.add_command(label="Poner selección en minúsculas", command=PonerSeleccionMinusculas)
submenuHerramientas.add_command(label="Poner todo en mayúsculas", command=PonerTodoMayusculas)
submenuHerramientas.add_command(label="Poner selección en mayúsculas", command=PonerSeleccionMayusculas)
submenuHerramientas.add_command(label="Poner primera en mayúsculas (todo)", command=CapitalizarTodo)
submenuHerramientas.add_command(label="Poner primera en mayúsculas (selección)", command=CapitalizarSeleccion)
submenuHerramientas.add_separator()
submenuHerramientas.add_command(label="Contar secuencia de carácteres", command=ContarSecuencia)
submenuHerramientas.add_command(label="Encontrar índice de secuencia de carácteres", command=EncontrarIndice)
submenuHerramientas.add_command(label="Comprobar si es computable", command=CombprobarDigitos)
submenuAyuda.add_command(label="Info", command=Info)
submenuAyuda.add_command(label="Ayuda", command=Ayuda)
submenuAyuda.add_command(label="Ir a la página", command=Pagina)
submenuAyuda.add_command(label="Ver estadísticas", command=Estadisticas)

if corriendo:
    raiz.mainloop()
