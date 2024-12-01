#Para hacer que un paquete del proyecto sea distribuible hay que hacer en la carpeta raiz un archivo con este nombre que contenga lo siguiente:
from setuptools import setup
setup(
    name="paquete_super_epico",#Nombre
    version="1.0",#Version
    description="paquete muy importante e inprenscindible",#Descripcion
    author="yo",#Autor
    author_email="jambo123@pymail.ch",#Correo opcional
    url="www.paquetespytonchulos.br",#Pagina opcional
    packages=["unpaquete","unpaquete"]#Aqui primero se pone la carpeta del paquete y luego la "ruta" del script sin el archivo
    #Hay mas cosas que se pueden poner
)
#Para crear el distribuible hay que ir a la ruta del archivo desde la consola de comandos normal y escribir "python setup.py sdist"
#Luego creara una carpeta llamada x.egg-info y otra importante llamada dist, dentro esta el .tar.gz para distribuir
#Para instalarlo hay que ir desde una consola normal a la carpeta dist y ejecutar el comando "pip3 install "archivo".tar.gz" y se puede importar desde cualquier lado porque se adhiere a la carpeta de instalacion de python
#Para desinstalarlo hay que poner en una consola normal "pip3 uninstall "nombre""
