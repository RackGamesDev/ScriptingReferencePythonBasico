import turtle#se importa la libreria para que funcione todo, es una flecha que se mueve por la pantalla dejando un rastro, conviene mirar la documentacion para ver todas las funciones
import math
tu = turtle.Turtle()#se crea la ventana principal y una flecha, se pueden crear varias flechas en una sola ventana con mas variables

turtle.bgcolor("yellow")#cambia el color del fondo, turtle hace referencia a la ventana no a la flecha
turtle.screensize(800,900)#cambia el tamagno del lienzo pero no el de la ventana
turtle.title("hola")#el titulo de la ventana
#se pueden hacer muchas cosas desde turtle.x que tambien se puede desde una flecha

tu.speed(2)#cambia la velocidad de esa flecha
tu.forward(50)#mueve la linea hacia delante
tu.left(90)#gira - grados, right(x) son +
tu.color("#69b00b", "red")#cambia el color de la flecha y de todo lo que dibuje en adelante, el segundo valor se usa con los fill

tu.begin_fill()#al poner esto se empieza a leer su linea para...
for i in range(4):#esto crearia un cuadrado
    tu.forward(50)
    tu.left(90)
tu.end_fill()#... cuando termine se rellena lo que lleve dentro una vez se cruce con su propia cola (si es del mismo color)(y se hara sobre todo lo que haya hecho despues del begin)
tu.penup()#desactiva el dibujado de su cola, moviendo solo la flecha
tu.forward(70)
tu.pendown()#y la vuelve a activar
tu.setheading(0)#pone la flecha hacia ese grado, tambien se pueden usar los puntos cardinales
tu.setx(100)#se mueve hacia esa cordenada, dibujando si eso esta activado
tu.sety(-100)
tu.goto((0,0))#lo mismo pero x y y a la vez
tu.circle(30)#pone un circulo especificando el radio, acabando donde empezo

turtle.done()#esto va al final para que no se cierre
#turtle.bye()#cierra turtle