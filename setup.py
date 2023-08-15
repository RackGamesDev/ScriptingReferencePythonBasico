#para hacer que un paquete del proyecto sea distribuible hay que hacer en la carpeta raiz un archivo con este nombre que contenga lo siguiente:
from setuptools import setup
setup(
    name="paquete_super_epico",#nombre
    version="1.0",#version
    description="paquete muy importante e inprenscindible",#descripcion
    author="yo",#autor
    author_email="jambo123@pymail.ch",#correo opcional
    url="www.paquetespytonchulos.br",#pagina opcional
    packages=["unpaquete","unpaquete"]#aqui primero se pone la carpeta del paquete y luego la "ruta" del script sin el archivo
    #hay mas cosas que se pueden poner
)
#para crear el distribuible hay que ir a la ruta del archivo desde la consola de comandos normal y escribir "python setup.py sdist"
#luego creara una carpeta llamada x.egg-info y otra importante llamada dist, dentro esta el .tar.gz para distribuir
#para instalarlo hay que ir desde una consola normal a la carpeta dist y ejecutar el comando "pip3 install "archivo".tar.gz" y se puede importar desde cualquier lado porque se adhiere a la carpeta de instalacion de python
#para desinstalarlo hay que poner en una consola normal "pip3 uninstall "nombre""