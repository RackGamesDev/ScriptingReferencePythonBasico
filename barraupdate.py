from tkinter import *
from tkinter import ttk
raiz=Tk()
varBarra=DoubleVar()
varBarra.set(30)
mbar=ttk.Progressbar(raiz, variable=varBarra, maximum=100, orient=VERTICAL)
mbar.pack()
hecho=False
def baa(m):
    hecho=True
    cont=0
    etapas=m/100
    while cont<etapas:
        cont+=1
        i=0
        while i<1000000:
            i+=i
        varBarra.set(cont)
        raiz.update()#update establece un periodo de tiempo para hacer cosas como esta
if hecho==False:
    baa(100)

raiz.mainloop()