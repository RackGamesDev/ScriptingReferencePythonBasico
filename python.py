#python.py
import math#Importar librerias para usarlas mas adelante

#Comentarios con este simbolo

#No deberian usarse los ; o los {} pero estan disponibles, ademas no es necesaria una funcion main, todo va de arriba a abajo

#Para imprimir, aparte de archivo.py de codigo tambien puede hacerse todo esto desde una consola de comandos ej:sublime text instalando su plugin
print("hola")
pregunta = input("te pregunto:_ ")#Detiene el programa y el string recibe el dato escrito por el usuario al darle a enter, se puede meter texto para que salga junto al prompt
print(pregunta)
print(input())
print("salto es nada", end="")#Eso hace que el caractar de cambio de linea en lugar de ser enter sea otro o nada
#pass #Linea nula usada para rellenar sin nada


#Las variables son de cualquier tipo
variable1 = 1
variable2 = 1.2
variable3 = "hola"
variable4 = True

#Pueden cambiar su tipo dinamicamente
variable1 = "adios"

#Para saber el tipo de una variable
print(type(variable1))
int(pregunta)#Intenta convertir a numero otra cosa, y si no da error
float(pregunta)#Intenta convertir a decimal otra cosa y si no da error
bool(pregunta)#Si no es un dato por defecto como 0 o "" devuelve false, y si no true
str(variable1)#Convierte otros tipo de dato en string


#string (hay muchas mas funciones y demas en la documentacion de python, esto es un poco de lo mas usado)
variable3 = "¿{}? ¡{}!".format(1,4)#Esta es una forma interesante de concatenar 
variable3 = variable3.lower()#Todo a minusculas
variable3 = variable3.upper()#Todo a mayusculas
variable3 = variable3.capitalize()#La primera en mayusculas y el resto en minusculasa
variable1 = variable3.count("ta")#Devuelve el numero de veces que aparece un texto/caracter en un string
variable1 = variable3.find("hola",0,15)#Devuelve el numero de caracter en el que empieza este caracter/secuencia por primera vez (el indice), los numeros son opcionales para especificar donde buscar, como con el resto de funciones
variable1 = variable3.rfind("hola")#Devuelve el numero de caracter en el que empieza este caracter/secuencia por primera vez (el indice) pero este lo hace desde el final
print(variable3.isdigit())#Devuelve true si eso es un digito (numeros y .)
print(variable3.isalnum())#Devuelve true si son todos caracteres numericos
print(variable3.isalpha())#Devuelve true si son todos caracteres alfanumericos
variable3 = variable3.split()#Se convierte en una lista de strings usando los espacios como separador

variable1 = len(variable3)#Al ser de string esto devuelve el numero de caracteres
print("ho\nla")#Eso hace un salto de linea


#Operadores
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2)#Division entera
print(1%2)#Resto de division
print(1**2)#Elevar a
print(math.sqrt(25))#Raiz cuadrada de (usando la libreria math)
print(round(5.3))#Redondea para quitar los decimales
import random
print(random.randint(0,10))#Con esta libreria


#Estructura ifs y operadores, nivelar con el tabulador y no con corchetes
if variable2==2:
    print("igual")
if variable2!=2:
    print("no igual")
if variable2>2:
    print("mayor")
if variable2<2:
    print("menor")
if variable2>=2:
    print("mayor o igual")
if variable2<=2:
    print("menor o igual")
if variable2==2:
    print("igual")
else:
    print("pues no")
if variable2==2:#elif (se pueden poner varios y se puede hacer que el ultimo sea un else)
    print("igual")
elif variable2<2:
    print("menor")
if 0<variable2<100:#Se pueden anidar asi las condiciones, otro ejemplo es texto1=texto2=texto3="a":
    print("dentro del rango")
if variable2>0 and variable4==False:#Se deberian cumplir las 2 condiciones
    print("si")
if variable2>0 or variable4==False:#Solo deberia cumplirse una, se podria hacer un sistema de parentesis
    print("si")
if variable3 in ("a","b","c"):#Entra solo si ese dato se encuentra en ese grupo
    print("esta dentro")
#Tambien estan los operadores booleanos (! || &&) para juntar combinaciones o operar con bools

    
#Bucles (no vienen con un contador, hay que poner una variable que se incremente cada vez manualmente)
for i in [0,2,3,4]:#Usando la variable i, repite el codigo tantas veces como elementos tenga ese rango
    print(i)#La variable i sera cada vez la posicion en el rango equivalente a la vuelta del bucle
for i in "hola":#El rango usado es cada letra por separado
    print(i)
for i in range(12):#Range inventa un rango del tamano que le digas, el bucle se hara esas veces y tendra i en incremento
    print(f"fase {i}")#La f hace que lo que haya entre corchetes se omita y se reemplace por una variable
for i in range(5,10,1):#El rango es de un numero a otro, en este caso 5 a 9, el tercer numero indica el incremento
    if i==7:
        continue#Cuando esta dentro de un bucle se salta esa vuelta y la empieza a empezar si deberia
    print(i)
variable2 = -1
while variable2>0:#El bucle while se ejecuta en bucle hasta que la condicion sea falsa
    if variable2<-5:
        break
    variable2+=1
    

#Estructura funcion normal
def Funcion1():
    global variable2#Usando global se puede usar la variable externa dentro de la funcion, aunque esto ya se puede de normal
    print("funcion1" + str(variable2))
#Estructura funcion con entradas
def Funcion2(texto):
    print("funcion1 con "+texto)
#Estructura funcion con entradas y salidas
def Funcion3(num1,num2):
    return num1+num2
#Llamar a funcion
print(Funcion3(3,6))
Funcion2("hola")
Funcion1()
#Podria ser recomendable comprobar en las funciones que tipo de dato se le inserta usanto type()

area=lambda base,altura:(base*altura)/2#Si es una funcion de una operacion que requiere parametros se puede simplificar su return con una funcion lambda sin usar un def
print(area(2,5))#Luego a la funcion lambda se la llama asi
nums=[1,2,3,4]
print(list(filter(lambda num: num%2==0, nums)))#La opcion filter pide una funcion que tenga return y una variable o lista, y devuelve solo los que cumplen con el mismo valor que esa funcion return, util con lambda
def espar(num):
    if num%2==0:
        return True
print(list(map(espar, nums)))#Mismo ejemplo pero con la funcion map que se suele usar con funciones def, la funcion filter devuelve o no el valor si su funcion devuelve true o false, la funcion map devuelve en si lo que salga del return

def fundecorador(funparametro):#Las funciones decoradoras son codigo adicional que se le agnaden a funciones normales antes y despues, se hacen con esta estructura
    def funinterior(*args, **kwargs):#Si las funciones normales reciben parametros se escribe *args. si quieres llamar a la funcion poniendo cada entrada con su nombre tambien se escribe **kwargs
        print("sumare")#Aqui el codigo antes de hacer la funcion normal
        funparametro(*args, **kwargs)#Aqui indica cuando se haria la funcion normal. si las funciones normales reciben parametros se escribe *args. si quieres llamar a la funcion poniendo cada entrada con su nombre tambien se escribe **kwargs
        print("sume")#Aqui el codigo despeus de hacer la funcion normal
    return funinterior
@fundecorador#Antes de declarar el def, se le especifica el nombre de la funcion decoraroda
def Sumica(a,b):
    print(a+b)
Sumica(1,4)
Sumica(a=2,b=3)

#Los generadores son funciones que devuelven una parte de una lista y cada vez que la llamas devuelve un elemento concreto. una vez la llamas se queda descansando para que cuando la vuelvas a llamar te mande el siguiente
def generarPar(limite):
    num=1
    while num<limite:
        yield num*2#Se usa el yield cada vez que devuelva algo
        num+=1
print(next(generarPar(9999)))#Se usa next para recibir solo el siguiente dato, si no se usa funcionaria como una funcion normal
def devolver(*tex):#Al poner un asterisco aqui se indica que recibe un grupo de elementos/tupla en lugar de uno
    for elemento in tex:
        yield from elemento#Devuelve con un nivel de abstraccion menor, al pasar texto pasaria segun caracteres
print(next(devolver("hola","adios","skadfsa")))

def Decir(que):
    """aqui se puede poner informacion sobre la funcion de mas abajo
    >>> Decir("aa")
    "bb"
    y incluso se pueden usar saltos de linea"""#Documentar funciones y clases, la 2º y 3º linea son sobre el testmod de abajo
    print(que)
    return que
print(Decir.__doc__)#Esto devuelve la informacion puesta con las triples comillas, o puedes usar help(nombrefuncion) pero si esta dentro de una clase seria help(clase.funcion)
import doctest
doctest.testmod()#Si haces la estructura con >>>(se pueden poner mas con mas lineas y usar ... para la identaicion) y la funcion con parametros, y luego eso no devuelve lo de la linea de abajo o da error el testmod lo hara saber, se pueden hacer varios test y se comprueban todos a la vez con el testmod


#Declarar listas (se pueden mezclar tipos de valores)
lista=["part0","part1",46,5,True]
print(lista[:])#Referirse a la lista entera
print(lista[1])#Referirse a un elemento concreto empezando por 0
print(lista[-1])#Si usas un indice negativo cuenta desde el ultimo, siendo el ultimo -1
print(lista[2:4])#Referirse a un rango de posiciones
print(lista[3:])#Referirse desde una posicion hasta el final, si hubiese sido [:x] seria desde el principio hasta x
lista.append("nuevo")#Angadir elemento al final porque son dinamicas
lista.insert(2,"inst")#Angadir elemento en una posicion, ese numero sera su nueva posicion y los elementos posteriores se desplazaran
lista.extend(["nu1","nu2","nu3"])#Como insert pero con varios elementos
print(lista.index("part1"))#Busca ese dato y devuelve el numero de indice de la primera vez que lo encuentre
print("part0" in lista)#Si el dato esta en la lista devuelve true
lista.remove("part0")#Busca el dato y lo elimina el primero que encuentre, los elementos posteriores se desplazaran
lista.pop()#Elimina el ultimo elemento
print(lista.count("part0"))#Devuelve cuantas veces aparece el dato
print(len(lista))#Devuelve la cantidad de elementos de la lista
#Concatenar listas
lista2=["a","b"]
lista3 = lista+lista2
lista3 = lista2 * 2#Repite esa lista varias veces
print(list("hola h o l a"))#Devuelve cualquier cosa en formato lista, util en textos

#Las tuplas o listas estaticas no se pueden poner o quitar elementos, el resto es todo igual solo que al imprimirse salen con parentesis (el in y el .count y el len si que funcionan)
listatica=("en1","en2","en3")
print(listatica[1])
lista2=list(listatica)#Una lista dinamica recibe los valores de una lista estatica, terminando exactamente igual
listatica=tuple(lista2)#Una lista estatica recibe los valores de una lista dinamica, la estatica si creara o eliminara valores
elem1, elem2, elem3 = listatica#Varios elementos declarados en orden cogiendo como dato una lista estatica
#Para meter listas en listas
listastatica=("en1",("en2.a","en3.a"),"en3")
listastatica2=((1,3),(5,3))
print(listastatica2[1][0])#Hay que tener cuidado si hay elementos en la lista que no son listas enteras a diferencia del resto
listasta=[[1,4],[6,3]]

#Los diccionarios son como listas pero a cada elemento se le asigna un dato pareja como indice (vale caulquier tipo de dato), nunca pueden haver 2 indices iguales
diccionario={"mas0":"menos0","mas1":"menos1","mas2":"menos2",}
print(diccionario["mas1"])#Para especificar la posicion se usa ese indice (lo de la derecha)
print(diccionario)#Para especificar el diccionario entero
diccionario["mas3"]="menos33"#Si el indice no existe anades un nuevo elemento, si ya existe se sobreescribe
del diccionario["mas3"]#Elimina el elemento segun indice
diccionario2 = {listatica[0]:0,listatica[1]:1,listatica[2]:2}#Se pueden declarar a partir de tuplas
diccionario3 = {1:1,2:2,3:[1,2,3]}#Se pueden meter listas o incluso otros diccionarios como dato
print(diccionario.keys())#Devuelve indices (izquierda)
print(diccionario.values())#Devuelve valores (derecha)


#Se pueden ignorar errores y actuar segun estos
try:#El codigo que intenta ejecutar, se pueden poner con uno o con varios except, si no se especifica el error entrara con cualquier error
    print(10/0)
except ZeroDivisionError:#Si termina dando este error, ejecuta este codigo y el programa continua, otro error comun es ValueError al intentar usar un tipo de dato erroneo y NameError es cuando la variable no existe
    print("error al dividir tontaco")
finally:#Lo del finally se ejecuta si hay error y si no
    print("siempre")
if variable2 > 0:
    raise TypeError("tonto ha fallado jajaja")#raise genera un error especifico con un mensaje especifico


class Objeto():#Al haber poo se pueden crear clases y usarlas como variable, asi es la sintaxis
    ancho = 2#Las variables necesitan un estado inicial (en caso de que no haya ningun constructor)
    largo = 3
    nombre = "no"
    def Explotar(self):#Si una funcion no tiene nada debe contener la orden "pass", la funcion debe contener self para referirse a su instancia
        print("boom")
        self.ancho = 0#Para acceder a sus propias variables se usa self.x
        #pass
    def DarNombre(self):
        return self.nombre#El return tambien funciona
    def AgrandarPor(self,cuanto):#Se pueden pedir variables pero debe ser despues del self, al llamarla se especifican todas menos el self
        self.ancho=self.ancho*cuanto  
    def __FuncionEncapsulada(self):#Al igual que las variables las funciones tambien pueden ser encapsuladas/bloqueadas desde fuera
        print("no me puedes ver desde fuera")
    def __str__(self):#Lo que haya en return sera lo que devuelva al intentar usar la variable como texto aunque sea un objeto
        return "se llama {} ancho {} largo {}".format(self.nombre, self.ancho, self.largo)
cosa = Objeto()#Para crear una variable de esa clase se hace asi
cosa2 = Objeto()#Se pueden declarar tantos como sean necesarios y se comportan como variables normales
cosa.Explotar()#Se usan los puntos para acceder a las propiedades y funciones del objeto
cosa.AgrandarPor(3)#Usando funciones que requieren variables, el self se ignora

class ObjetoConConstructor():
    def __init__(self):#Declarar un constructor para que inicie con un estado al declararse, tambien se pueden declarar variables desde una funcion con self.
        self.nombre = "nombre por defecto"
        self.__variableee = 3#Si dentro del constructor la variable empieza por __ aparecera encapsulada y no se podra cambiar desde fuera, y se debe usar luego tambien con eso porque asi es su nombre
cosa3 = ObjetoConConstructor()#Declarando una variable a partir de una clase con constructor
#cosa4 = ObjetoConConstructor("otro nombre", 4)#Se puede declarar con otros valores poniendolos en orden segun se establecen en el constructor
class Heredado(Objeto):#Esta clase tendra sus funciones y variables ademas de las de la clase de la que herede (la del parentesis), el constructor tambien se hereda
    numero = 0
    def __init__(self, numero):
        super().__init__(3,6,"nom")#Con esto se le pueden asignar valores de su clase padre, en este caso objeto, se estaria usando como si se declarase objeto
        self.numero = numero
    def Explotar(self):#Si una clase tiene una funcion o variable que se llama igual que la de la clase padre, la sobreescribe y termina funcionando como la clase con herencia, el unico constructor usado es el de la primera clase
        print("boom pero heredado")
objher = Heredado(120)#Se declararia poniendo segun el constructor
class MasHeredado(Objeto,ObjetoConConstructor):#Se puede heredar de varias clases, la primera siempre tendra prioridad y algunas pueden no ser compatibles por tener coincidencias o hay que ponerlas en otro orden
    nume=3
print(isinstance(objher, Objeto))#Eevuelve true o false si la variable es o hereda de alguna clase, primero la variable y despues la clase
def ExplotarCualquiera(cualquierObjeto):#Aqui hay un ejemplo de polimorfismo, dos clases tienen una funcion/variable con el mismo nombre y al llamar a una variable generica para que haga una cosa no hay conflicto en ninguno de los 2 casos
    cualquierObjeto.Explotar()#Explotar se encuentra en Objeto y en otras clases, le puedes meter un objeto de cualquiera de esas 2 clases
  
    
#Para usar otros scripts el otro archivo tiene que ser .py y estar en la misma carpeta, y luego se importa
import modulo1#Importando el otro archivo (sin escribir la extension)
modulo1.sumar(3,6)#Y se puede llamar a las funciones o variables de ese modulo
from modulo1 import restar#Para no tener que escribir el modulo todo el rato se pueden importrar cosas especificas como funciones
restar(3,1)#Ahora ya no hay que poner modulo1.x
from modulo1 import *#Con el asterisco se importa todo a la vez desde ese script y se puede usar como si fuese de este, tambien podrias imortar varias cosas usando , 
from unpaquete.paquetico import multiplicar#Esto es un paquete, una carpeta en el proyecto con un archivo llamado "__init__.py", python la vera como una carpeta normal en la que hayan scripts
from unpaquete import *#Se puede imoportar todo lo que haya en un paquete/carpeta tambien
multiplicar(3,6)
#import paquetedistribuible#Esto importaria el paquete instalado


#Manipulacion de archivos
from io import open#Necesario importarlo
archivoTexto=open("archivo.txt","w")#Primero en nombre del archivo y luego el modo (w=write), open crea un archivo y lo carga en memoria
archivoTexto.write("contenido y tal")#.write() hace que el archivo tenga todo lo que le metas por string, quitando lo que ya haya
archivoTexto.close()#Al final se cierra para no malgastar espacio en memoria y para que otros lo puedan editar y mirar
archivoTexto=open("archivo.txt","r")#Ahora la r=read es para leer, de esta manera se abre pero no para escribir sino para leer, el archivo debe existir de antes
texto = archivoTexto.read()#.read() devuelve todo su contenido, se le puede meter un numero para que lea desde del cursor hasta el numero
textoL = archivoTexto.readlines()#Esto devuelve una lista de strings con cada linea separado por saltos de linea
archivoTexto.seek(0)#seek lleva el cursor a x posicion que se usa para leer y escribir, se resetea cada vez que se cierra, el cursor se mueve por cada operacion de lectura/escritura normalmente al final
archivoTexto.close()
print(texto)#Todo listo para usarse
archivoTexto=open("archivo.txt","a")#a=append es como write pero se le anade al final, pero tambien necesita que ya exista el archivo
archivoTexto.write(" nuevo")#Esto aparecera despues del contenido ya almacenado
archivoTexto.close()
archivoTexto=open("archivo.txt","r+")#r+ es para lectura y escritura
archivoTexto.close()

#Archivos serializados (cifrados en binario)
import pickle#Necesario importarlo
guardar=open("cifrado","wb")#Abrirlo como writebinary
variableParaGuardar=["guarda esto","y esto", "esto tambien"]#Un archivo binario guarda una variable, da igual si es un objeto o una lista, lo que sea (ejemplo con una lista)
pickle.dump(variableParaGuardar, guardar)#Para volcar la informacion al binario primero se pone la informacion y luego el archivo
guardar.close()#Cerrarlo
del(guardar)#Normalmente se usa esto para eliminarlo de la memoria pero no es necesario
abrir=open("cifrado","rb")#Para leerlo y descifrarlo hay que abrirlo como readbinary
listaCargada = pickle.load(abrir)#Esto devuelve la informacion de dentro del binario, la variable que reciba la informacion sera del tipo de la informacion guardada
print(listaCargada)#Si se carga un fichero con un objeto de clase, se debe hacer desde un script que conozca esa clase bien


#Los regex buscan dentro de una lista como un string y devuelven un objeto con la info de la coincidencia, si no existe devuelve None, son compatibles con sus wildcards
import re#Esto es para las expresiones regulares normalmente usadas para buscar texto y mas aun con listas de textos
textoinicial="Hola buenas este texto se va a manimular mucho 1234"
print(re.search("buenas", textoinicial))#Devuelve un objeto sobre si aparece el texto y de donde a donde, en caso de que no sera "None"
if re.search("buenas", textoinicial) is not None: print("si")#Asi es como se comprueba con un if
if re.match("Hol", textoinicial, re.IGNORECASE) is not None: print("si")#Comprueba si el texto empieza con eso, el tercer parametro es opcional para ignorar mayusculas/minusculas
objetoencontro=re.search("este", textoinicial)#En este caso se almacena ese objeto en una variable
print(objetoencontro.start())#De ese objeto, .start devuelve en donde empezo a encontrarlo
print(objetoencontro.end())#De ese objeto, .end devuelve en donde dejo de encontrarlo
print(objetoencontro.span())#De ese objeto, .span devuelve una dupla de .start y .end
print(re.findall("te", textoinicial))#Devuelve como lista todos los sitios en los que aparece el texto, pudiendo almacenar el resultado como objeto para saber donde esta cada uno o se podria usar un len()
#Wildcards para expresiones regulares
print(re.findall("^Ho", textoinicial))#Devuelve si empieza por ese texto
print(re.findall("Ho$", textoinicial))#Devuelve si terminapor ese texto
print(re.findall("[tsb]", textoinicial))#Devuelve si el texto contiene esos caracteres en cualquier orden
print(re.findall("^Ho[al]", textoinicial))#Se pueden concatenar de cualquier forma
print(re.findall("[b-dx-z]", textoinicial))#Igual que lo del [] pero todos los caracteres de ese rango en orden ascii, tambien se pueden meter varios rangos en un solo [] como en este caso
print(re.findall("[^b-d]", textoinicial))#Con ese simbolo se invierte y devuelve los que esten fuera del rango
print(re.findall("^Ho.a", textoinicial))#El . cuenta como cualquier caracter ascii
print(re.findall("\n$", textoinicial))#El \n cuenta como cualquier digito
