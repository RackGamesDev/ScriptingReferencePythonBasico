from tkinter import *
from tkinter import messagebox
raiz=Tk()
raiz.title("calculadora")
raiz.resizable(True, True)
frame=Frame(raiz)
frame.pack(fill="both", expand="True")
corriendo=True
decimal=0
parentesisabi=0
parentesiscer=0
textoCaja=StringVar()
operacion=Entry(frame, state="readonly", width=40)
operacion.grid(row=0, column=0, pady=10, columnspan=4, sticky="nsew")
operacion.config(readonlybackground="white", textvariable=textoCaja, justify="right")
textoCaja.set("0")


class Nomio():
    def __init__(self, numero_, operacion_, nivelPrioridad_):
        numero=numero_
        operacion=operacion_
        nivelPrioridad=nivelPrioridad_


def PulsarNumero(cifra):
    if textoCaja.get() == "0" or textoCaja.get() == "":
        textoCaja.set(cifra)
    else:
        ult = textoCaja.get()[len(textoCaja.get()) - 1]
        if ult!=")":
            textoCaja.set(textoCaja.get()+cifra)
                
def PonerComilla():
    global decimal
    if textoCaja.get() != "":
        ult = textoCaja.get()[len(textoCaja.get()) - 1]
        if decimal==0 and ult!="." and ult!="+" and ult!="-" and ult!="x" and ult!="/" and ult!="(" and ult!=")":
            textoCaja.set(textoCaja.get()+".")
            decimal=1

def PulsarOperacion(caracter):
    global decimal
    if textoCaja.get() != "0" and textoCaja.get() != "":
        ult = textoCaja.get()[len(textoCaja.get()) - 1]
        if ult=="+" or ult=="-" or ult=="x" or ult=="/" or ult==".":
            pass
        else:
             textoCaja.set(textoCaja.get()+caracter) 
             decimal=0          
    if caracter=="-":
        if textoCaja.get() == "0":
            textoCaja.set("-") 
            decimal=0
        else:
            ult = textoCaja.get()[len(textoCaja.get()) - 1]
            if ult!="+" and ult!="-" and ult!="+.":
                textoCaja.set(textoCaja.get()+"-") 
                decimal=0
                
            
  
def AbrirParentesis():
    global parentesisabi
    ult = textoCaja.get()[len(textoCaja.get()) - 1]
    if textoCaja.get()=="0":
        parentesisabi=1
        textoCaja.set("(")
    else:
        if ult!="." and ult!="0" and ult!="1" and ult!="2" and ult!="3" and ult!="4" and ult!="5" and ult!="6" and ult!="7" and ult!="8" and ult!="9":
            parentesisabi+=1
            textoCaja.set(textoCaja.get()+"(")

def CerrarParentesis():
    global parentesisabi
    global parentesiscer
    ult = textoCaja.get()[len(textoCaja.get()) - 1]
    if parentesiscer<parentesisabi and ult!="." and ult!="+" and ult!="-" and ult!="x" and ult!="/" and ult!="(":
        parentesiscer+=1
        textoCaja.set(textoCaja.get()+")")
            

def BorrarUno():
    global decimal
    global parentesises
    if len(textoCaja.get())>1:
        ult = textoCaja.get()[len(textoCaja.get()) - 1]
        if ult==".":
            decimal=0
        i=0
        nom = textoCaja.get()
        l=""
        for c in nom:
            i+=1
            if i < len(textoCaja.get()):
                l+=c
        textoCaja.set(l)
    else:
        textoCaja.set("0")


def PulsarIgual():
    puede=1
    ult = textoCaja.get()[len(textoCaja.get()) - 1]
    if parentesiscer<parentesisabi:
        messagebox.showerror("Error", "Tienes algún paréntesis sin cerrar")
        puede=0
    if ult==".":
        messagebox.showerror("Error", "Termina de escribir el número")
        puede=0
    if ult=="+" or ult=="-" or ult=="/" or ult=="x":
        messagebox.showerror("Error", "Esa operación del final no hace nada")
        puede=0
    
    if puede==1:
        textoCaja.set(Calcular(textoCaja.get()))
    
    
def BorrarTodo():
    global parentesisabi
    global parentesiscer
    global decimal
    textoCaja.set("0")
    decimal=0
    parentesiscer=0
    parentesisabi=0
   

def cal(tod):
    print(tod)






































def Calcular(opert):
    resultado=0
    try:
        cal(opert)
    except:
        messagebox.showerror("Error", "Error desconocido, lo siento")
        resultado=textoCaja.get()
    return resultado

decimal=0
Button(frame, text="7", command=lambda:PulsarNumero("7")).grid(row=1, column=0, sticky="we")
Button(frame, text="8", command=lambda:PulsarNumero("8")).grid(row=1, column=1, sticky="we")
Button(frame, text="9", command=lambda:PulsarNumero("9")).grid(row=1, column=2, sticky="we")
Button(frame, text="4", command=lambda:PulsarNumero("4")).grid(row=2, column=0, sticky="we")
Button(frame, text="5", command=lambda:PulsarNumero("5")).grid(row=2, column=1, sticky="we")
Button(frame, text="6", command=lambda:PulsarNumero("6")).grid(row=2, column=2, sticky="we")
Button(frame, text="1", command=lambda:PulsarNumero("1")).grid(row=3, column=0, sticky="we")
Button(frame, text="2", command=lambda:PulsarNumero("2")).grid(row=3, column=1, sticky="we")
Button(frame, text="3", command=lambda:PulsarNumero("3")).grid(row=3, column=2, sticky="we")
Button(frame, text="0", command=lambda:PulsarNumero("0")).grid(row=4, column=0, sticky="we")
Button(frame, text="/", command=lambda:PulsarOperacion("/")).grid(row=1, column=3, sticky="we")
Button(frame, text="x", command=lambda:PulsarOperacion("x")).grid(row=2, column=3, sticky="we")
Button(frame, text="-", command=lambda:PulsarOperacion("-")).grid(row=3, column=3, sticky="we")
Button(frame, text="+", command=lambda:PulsarOperacion("+")).grid(row=4, column=3, sticky="we")
Button(frame, text=".", command=PonerComilla).grid(row=4, column=1, sticky="we")
Button(frame, text="=", command=PulsarIgual).grid(row=4, column=2, sticky="we")
Button(frame, text="C", command=BorrarTodo).grid(row=5, column=0, sticky="we")
Button(frame, text="c", command=BorrarUno).grid(row=5, column=1, sticky="we")
Button(frame, text="(", command=AbrirParentesis).grid(row=5, column=2, sticky="we")
Button(frame, text=")", command=CerrarParentesis).grid(row=5, column=3, sticky="we")
if corriendo:
    raiz.mainloop()
else:
    raiz.destroy()
