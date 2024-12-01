#Todo el tema de las interfaces viene en otro script para no sobrecargar el otro
from tkinter import *#Este es un paquete para interfaz grafica de python, si no viene instalado en linux se hace con "sudo apt-get install python3-tk", recomendado ver su documentacion
from tkinter import messagebox#Esto es para los cuadros emergentes
from tkinter import filedialog#Esto es para la ventana de usar archivos, combina bien con el io
from tkinter import ttk#Esto es para el combobox, el notebook(pestanas), progressbar
corriendo = True
raiz = Tk()#Con eso y con el .mainloop() al final se crea la variable de la ventana a crear. si el script es .pyw al abrirlo saldra como la ventana. se pueden crear tantas como sean necesarias
raiz.title("prueba")#Cambiar el titulo
raiz.resizable(True,True)#Cada uno es x o y, si es redimensionable o no
#raiz.iconbitmap("x.ico")#Para poner un icono en la ventana, el .ico debe estar en la misma carpeta
#raiz.geometry("800x300")#Para cambiar el tamano de la ventana, puede no ser necesario ponerlo porque se adapta al tamano de su frame interno
raiz.config(bg="yellow")#Cambiar el color de fondo
frame=Frame(raiz)#El frame contiene los elementos graficos, se encuentra dentro de la raiz
frame.pack(fill="both", expand="True")#Opciones de empaquetado dentro de la ventana (side es donde sale y anchor va por n,s,w,e. fill=y con expandable="True" es para que sea autoestirable)
frame.config(bg="gray")
frame.config(width="1000", height="1000")#Para configurarlo y establecer su tamano, el frame estara por defectoclavado  arriba en el centro de la ventana en caso de que se redimensione
#frame.config(bd=10,relief="groove")#Opciones feas para el borde
frame.config(cursor="hand2")#Para cambiar el cursor dentro del frame

def codigoBoton(texto):#Ejemplo de funcion para el boton, tambien puede recibir argumentos pero no devolverlos
    frame.config(bg="yellow")
    mlabel.config(text=texto)
#widgets: (mirar la documentacion para encontrar mas propiedades)(pack()pone y ignora tamano de ventana, place(x,y) pone y respeta tamano de ventana
#place(x=,y=,height=,width=) #Ponerlo libremente
#pack() #Lo pone donde quede automaticamente
#grid(row,column) #pone unos al lado de otros y ignora tamano de ventana) y se le puede poner una propiedad sticky="(punto cardinal)" para que se pegue hacia un lado en caso de que haga falta, o el pady/padx=(num)que hace de margen para otros widgets
#x.config() #Tiene un monton de propiedades utiles para los widgets que convendria mirar en la documentacion
Label(frame, text="quieto parao").grid(row=0,column=0)#Esta es una manera de poner widgets rapidamente, pero no los puedes usar luego, mejor usar la manera de abajo para tenerlos en variables
mlabel=Label(frame, text="hla", fg="red", font=("Comic Sans MS",16))#Esto es un label, un texto (tambien puede contener imagenes), la fuente debe venir instalada
mlabel.grid(row=0,column=1, sticky="n")#Para poner el widget se usa el place con las coordenadas (00 es arriba izquierda) o fila y columna en caso de grid
mimagen=PhotoImage(file="img.png")#Pone una imagen png o un gif, el archivo se mira desde la carpeta del script
Label(frame, image=mimagen, cursor="hand1").grid(row=0,column=2)#La imagen se pone dentro de un label

delacaja=StringVar(raiz)#Declarando una variable stringvar para sacar el texto de la caja de texto
texto = delacaja.get()#Asi se sacaria, pero hay que poner como textvariable el stringvar en la caja
delacaja.set("hola")#Asi se cambia un stringvar
mcuadrotexto=Entry(frame)#Es un cuadro para introducir texto
mcuadrotexto.focus_set()#Para focusear al usuario desde el principio
mcuadrotexto.grid(row=1,column=0)#Otra manera de colocarlo
mcuadrotexto.config(show="*", textvariable=delacaja, justify="center")#Ejemplo de propiedad que cambia la visivilidad de los caracteres por esto. textvariable asigna el texto del cuadro a una variable del tipo stringvar, si le pones state="readonly" no puedes escribir

mtextogrande=Text(frame, width=16, height=20)#Como el cuadro de texto pero mucho mas grande
mtextogrande.grid(row=2,column=0, columnspan=3)#Columnspan y rowspan hace que ocupe varias filas/columnas
mscroll = Scrollbar(frame, command=mtextogrande.yview)
mscroll.grid(row=2,column=1, sticky="nsew")#A los widgets se les anade un scroll cuando son muy grandes, se especifica a que widget y si es yview/xview
mtextogrande.config(yscrollcommand=mscroll.set)

mboton = Button(frame, text="accion", command=lambda:codigoBoton("ai"))#Un boton que ejecuta codigo, command es el nombre de una funcion
mboton.grid(row=3,column=0)

varRadio=IntVar()#Necesario para saber sobre el radiobutton
def CambioRadio():#Funcion para el cambio de los radio
    print(varRadio.get())#El .get() tambien esta para los intvar
    #varOpcion.set(1)#Para cambiar el estado de un radio se cambia su variable asignada
mradio1=Radiobutton(frame, text="opcion unica 1", variable=varRadio, value=1, command=CambioRadio)#Los radiobutton son casillas que solo una puede ser activada dentro de su frame, para saber que llevan es necesario un intvar en variable y asignar a cada uno un value distinto
mradio1.grid(row=4,column=0)
mradio2=Radiobutton(frame, text="opcion unica 2", variable=varRadio, value=2, command=CambioRadio)
mradio2.grid(row=4,column=2)

varCheck=IntVar()#Necesario para saber sobre cada check
def CambioCheck():#Funcion para el cambio de los check
    print(varCheck.get())
mcheck = Checkbutton(frame, text="activo o no", variable=varCheck, onvalue=1, offvalue=0, command=CambioCheck)#Es como el radio pero no depende de otros, activo o no y ya. usa una variable y onvalue y offvalue es como esta en caso de estar marcado o no
mcheck.grid(row=5, column=0)

varSpin=StringVar()#Necesario para saber sobre el spinbox
mspin=Spinbox(frame, values=("1", "2", "3"), textvariable=varSpin)#Un spinbox es un entry que viene con flechas para elegir textos preestablecidos
mspin.grid(row=6,column=0)

mcuadro=LabelFrame(frame, text="espacio", pady=20, padx=20)#un labelframe es como un marco usado como widget que tiene un titulo y elementos dentro, el pady/x de esta linea es sobre el tamano del widget
mcuadro.grid(row=7, column=1, padx=5, pady=5, columnspan=4)
Label(mcuadro, text="aaaaaaaaaaa").grid(row=0,column=0)#Poniendo un elemento dentro del labelframe

def FuncionSlider(val):#Cuando el slider cambia de valor, llama a esta funcion desde la cual se puede guardar el valor que tiene
    print(val)
    return None
mslider = Scale(frame, from_=0, to=10, length=200, resolution=0.5, orient=HORIZONTAL, command=FuncionSlider)#Es una barra deslizante para elegir un numero, resolution es cuanto sube y length se mide en pixeles
mslider.grid(row=8, column=0)

mcombo = ttk.Combobox(frame, state="readonly")#Combobox es una lista desplegable con textos que viene de la libreria ttk, sigues pudiendo introducir manualmente texto si no pones readonly
mcombo.grid(row=9, column=0)
mcombo["values"]=("a","b","c")#Declarando los textos del combo, se puede cambiar en cualquier momento
mcombo.current(0)#Establecer valor por indice de values
textocombo=mcombo.get()#Conseguir el valor del combo (tambien podria ser algo introducido por el usuario)

mtabControl=ttk.Notebook(frame)#El notebook es un cuadro con pestanas con widgets dentro en cada una
mtab1=ttk.Frame(mtabControl)#Declarando las pestanas, que funcionan como labelframes
mtab2=ttk.Frame(mtabControl)
mtabControl.add(mtab1, text="pestana1")#Agnadiendo las pestanas al notebook
mtabControl.add(mtab2, text="pestana2")
Label(mtab1, text="1111").pack()#Los widgets se empaquetan dentro de las pestanas como si fuesen frames
Label(mtab2, text="2222").pack()
mtabControl.grid(row=10, column=0)#Normalmente el notebook se empaqueta luego

varBarra=DoubleVar()#Variable para establecer o saber el progreso de la barra
varBarra.set(30)#Establecer valor de barra
mbar=ttk.Progressbar(frame, variable=varBarra, maximum=100, orient=HORIZONTAL, length=100)#Una barra de progreso simple
mbar.grid(row=11, column=0)



def AbrirArchivo():
    marchivo=filedialog.askopenfilename(title="hola elige", initialdir="C:", filetypes=(("imagen", "*.png"),("foto", "*.jpg"),("todo", "*.*")))#Abre una ventana de elegir archivo y devuelve la ruta
    marchivo=filedialog.askdirectory(title="elige carpeta")#Lo mismo pero con esto eliges una carpeta y no un archivo
    print(marchivo)

def PulsarSubopcion11():#Funcion para una subopcion
    messagebox.showinfo("titulo", "informacion interior to epica chaval")#Con messagebox importado de tkinter se pueden mostrar ventanas de mensajes, primero el titulo y luego la informacion, el codigo se pausa hasta que le des a un boton
    eleccion = messagebox.askyesno("titulo", "si o no decide")#Te deja elegir si si o si no y lo vuelca en un bool. .askokcancel seria lo mismo pero devuelve true o false. .askretrycancel devuelve tambien True o False
    if eleccion=="yes":#Devolvera "yes" o "no", los nombres de los botones en el caso de .askyesno
        print("si")
def PulsarSubopcion12():
    messagebox.showwarning("titulo aviso", "asdfasdñflkjlasf")#Como showinfo pero como si fuese un aviso
    messagebox.showerror("titulo error", "algo mal")#Y este es un error
    
mmenu=Menu(frame)#Menu superior como archivo, editar, etc
raiz.config(menu=mmenu)#Se le especifica a la raiz que tiene como menu, hay que tener en cuenta de que quepan dentro de la ventana
mopcion1=Menu(mmenu, tearoff=0)#Esto por cada opcion principal, se meten en el menu mas superior. el tearoff 0 o 1 es una subopcion de ejemplo
mopcion2=Menu(mmenu, tearoff=0)
mmenu.add_cascade(label="opcion1", menu=mopcion1)#Se le anaden las opciones al menu mas superior
mmenu.add_cascade(label="opcion2", menu=mopcion2)
mopcion1.add_command(label="subopcion1.1", command=PulsarSubopcion11)#Se anaden las subopciones dentro de las opciones con texto y una funcion
mopcion1.add_separator()#Separador entre opciones
mopcion1.add_command(label="subopcion1.2", command=PulsarSubopcion12)
mopcion2.add_command(label="subopcion2.1", command=AbrirArchivo)
mopcion2.add_command(label="subopcion2.2")



if corriendo:
    raiz.mainloop()#Esto siempre al final o se cerrara
else:
    raiz.destroy()#Esto cierra la interfaz, en este caso tambien cerraria el programa porque aqui acaba el codigo
