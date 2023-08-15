#esto es un modulo, asi una aplicacion se puede dividir en varios scripts.py
def sumar (o1,o2):
    print("es" + str(o1+o2))
def restar (o1,o2):
    print("es" + str(o1-o2))
    
import pickle  
#ejemplo de guardado permanente con pickle
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):#esto devuelve como string un objeto
        return "{} {}".format(self.nombre, self.edad)#habria que poner tantos corchetes como variables necesitadas para guardar
class ListaPersonas:
    personas=[]
    def __init__(self):
        listdpers = open("archiv","ab+")
        listdpers.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
        except:
            print("no, esta es la primera vez que se abre y el archivo esta vacio")
        finally:
            listdpers.close()
            del(listdpers)
    def Agregar(self,p):
        self.personas.append(p)
listaDePersonas=ListaPersonas()
p=Persona("nom",123)
pp=Persona("nom2",456)
listaDePersonas.Agregar(p)
listaDePersonas.Agregar(pp)