import sqlite3#Esto funcinona con el gestor de base de datos sqllite3 crud
conexion=sqlite3.connect("basedatos")#Crea la conexion con la base de datos, si no existe la crea
cursor=conexion.cursor()#Crear el cursor
#cursor.execute("CREATE TABLE PERSONA (NOMBRE VARCHAR(20), EDAD INTEGER)")#Ejecuta una consulta en idioma sql, en este caso crea una tabla, esto no deberia ejecutarse si la tabla ya esta creada
cursor.execute("INSERT INTO PERSONA VALUES('nom',23)")#Ejecuta una consulta sql que agnade un item a la tabla, si la tabla no existe esto no deberia ejecutarse
personas=[("nombrecico",12),("nombrecero",32),("nombrecon", 54)]
cursor.executemany("INSERT INTO PERSONA VALUES (?,?)", personas)#Introduce una lista de cosas en una tabla con el mismo formato, los ? se ponen tantos como atributos tenga la tabla

#Asi se hace la primary key, tambien se le pone el autoincrement en caso de que se quiera o unique para que no se pueda repetir
#cursor.execute('''CREATE TABLE LUGAR (
#   ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#   LETRA VARCHAR(1) UNIQUE)''')#Se suelen usar ''' para introducir texto pudiendo hacer saltos de linea solo visibles en el script
cursor.execute("INSERT INTO LUGAR VALUES(NULL,'a')")#Al tener el autoincremento se pone null en la primary key

cursor.execute("SELECT * FROM PERSONA")#Para conseguir los valores primero hay que seleccionarlos con una consulta sql
personas=cursor.fetchall()#Luego se vuelcan en una tupla o lista de tuplas
print(personas)
personas=cursor.execute("SELECT * FROM PERSONA WHERE EDAD=32")#Asi se pueden devolver filtrados solo los que cumplan con una condicion en ese atributo

cursor.execute("UPDATE PERSONA SET EDAD=33 WHERE NOMBRE='nombrecico'")#Actualiza un valor en algo concreto

cursor.execute("DELETE FROM PERSONA WHERE EDAD=32")#Borrar registros que cumplen algo

conexion.commit()#Confirma todos los cambios hechos anteriormente
conexion.close()#Cierra la conexion para ahorrar ram
