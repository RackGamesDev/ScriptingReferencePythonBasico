import pygame, sys, random, math#Pygame se importa tras instalarse
pygame.init()#Esta linea es para empezarlo, necesario
size = (512, 512)#Tamagno inicial de ventana, las coordenadas se miden en pixeles y arriba izquierda es 0 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("titulo")#Cambia el titulo de la ventana


class ObjConSprite(pygame.sprite.Sprite):#Las variables que se hagan con esta clase seran como objetos con sprites, esta carga la imagen img.png
    def __init__(self, img, alpha, colkey):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(colkey)
        self.rect = self.image.get_rect()
        self.image.set_alpha(alpha)
        
class Game(object):#Estructura recomendada para hacer pantallas, cada variable que se crea seria como una escena
    def __init__(self):
        #Crear variables y objetos y etc: self.x=... tambien se suelen configurar las escenas
        pass
    def process_events(self):
        pass
    def run_logic(self):
        pass
    def display_frame(self):
        pass
    #Crear tantas funciones como uieras
def main():#Aqui se pondria la pantalla principal, mas tarde iria el bucle
    game=Game()

#Aqui se suele poner el codigo start, normalmente para cargar cosas
cblanco=(255,255,255)#Se suelen declarar tuplas de 3 numeros para colores
cnegro=(0,0,0)
crojo=(255,0,0)
cverde=(0,255,0)
cazul=(0,0,255)
tipoclick="no"#Variable para el click que se configura en el bucle de abajo
fuente1=pygame.font.SysFont("monospace", 20)#Establece una fuente, que debe estar instalada
texto=fuente1.render("hola", 1, cblanco,cnegro)#Con la fuente establecida escribe algo, (texto, antialias1/0, colortexto, colorfondo)
clock = pygame.time.Clock()#Variable usada para el tiempo
tiempo=0
imagen=pygame.image.load("bg.png").convert()#Carga una imagen en memoria apartir de un archivo
imagen.set_colorkey(cblanco)#Si la imagen aparece con un fondo aun siendo png, se usa esto especificando que color se va a quitar
imagen.set_alpha(200)#De 0 a 255 establece la opacidad, mayor el numero mayor opacidad
imagen = pygame.transform.scale(imagen, (400,400))#Escala la imagen por pixeles en x y y
imagen = pygame.transform.rotate(imagen, 45)#Rota la imagen alrededor de si misma x grados
#Crear objetos con la clase de antes creada
sprListaObj=pygame.sprite.Group()#Se suelen crear 2 listas, una que almacene todos los objetos de ese tipo
todSprLista=pygame.sprite.Group()#Y otra que almacene todos los sprites en pantalla
for i in range(8):
    unobjeto=ObjConSprite(img="img.png", alpha=255, colkey=(255,255,255))
    unobjeto.rect.x=random.randrange(512)#Establecer coordenadas
    unobjeto.rect.y=random.randrange(512)
    sprListaObj.add(unobjeto)#Agregar los objetos en ambas listas
    todSprLista.add(unobjeto)
otroobjeto=ObjConSprite(img="img.png", alpha=255, colkey=(255,255,255))
otroobjeto.rect.x=random.randrange(512)
otroobjeto.rect.y=random.randrange(512)
sonido = pygame.mixer.Sound("snd.ogg")#Carga un sonido en memoria para usarlo luego

def Update():#Variable update en el juego, conviene ver la documentacion para ver mas funciones, para borrar un objeto dibujado simplemente no hay que renderizarlo en el proximo frame
    global todSprLista
    global tiempo
    global imagen
    global otroobjeto
    global tipoclick
    global sonido
    tiempo+=1
    screen.blit(imagen, [0,0])#Renderiza la imagen donde le digas, la imagen sale tal cual esta sin antialias o redimensionar
    pygame.draw.line(screen, cnegro, [0,0], [50,50], 2)#Dibujar linea (pantalla, color, xyinicio, xyfinal, grosor) medido en pixeles
    pygame.draw.rect(screen, cverde, (50,50,100,100), 3)#Dibujar rectangulo (pantalla, color, (x,y,ancho,alto), ancho de linea(0 es relleno))
    pygame.draw.circle(screen, crojo, (200,100), 30, 0)#Dibujar circulo (pantalla, color, (x,y), radio, ancho de linea(0 es relleno))
    pygame.draw.polygon(screen, cazul, ((100,100),(100,200),(200,300)), 0)#Dibujar poligono (pantalla, color, ((x,y),(x,y),etc.)), ancho de linea(0 es relleno))
    pygame.draw.line(screen, cnegro, [0,0], [tiempo,50], 2)#Ejemplo de animacion, una vez puesto el clock la variable tiempo se suma 60 veces por segundo
    xymouse = pygame.mouse.get_pos()#Devuelve una tupla con las coordenadas x y y del raton dentro de la pantalla
    pygame.mouse.set_visible(0)#Esconde el cursor, 1 es activo
    if event.type == pygame.KEYDOWN:#Devuelve true si se empieza a presionar una tecla
        if event.key == pygame.K_LEFT:#Luego se puede especificar que tecla, se ven con K_tecla
            print("presionar izquierda")
        print("presionar tecla")
    if event.type == pygame.KEYUP:#Lo mismo pero cuando no se pulsa, igual a el if de antes si le pones un else
        if event.key == pygame.K_LEFT:
            print("soltar izquierda")
        print("soltar tecla")
    obj1=pygame.draw.circle(screen, crojo, (200,100), 30, 0)#Normalmente los dibujos se guardan en variables
    obj2=pygame.draw.circle(screen, crojo, (350,100), 30, 0)
    if obj1.colliderect(obj2) or obj2.colliderect(obj1):#Para detectar colisiones entre dibujos, hay que poner los dibujos en variables
        #print("choca")
        pass
    todSprLista.draw(screen)#Con la lista de todos los sprites se pueden dibujar todos a la vez con esta linea
    todSprLista.remove(1)#Otra forma de eliminar un dibujo si esta en una lista es quitarlo de la lista y ya
    #print(otroobjeto.rect.x)#Para conseguir una coordenada de un objeto creado mediante esa clase de sprite
    listaHit=pygame.sprite.spritecollide(otroobjeto, sprListaObj, True)#Esto hace una lista de las colisiones entre la variable otroobjeto y cualquiera de la lista sprlistaobj, el true del final indica que el objeto de la lista que toque desaparece
    for unobjeto in sprListaObj:#Esto seria para ejecutar un evento por cada vez que choca
        #print("choca")
        pass
    screen.blit(texto, (100,100))#Con la fuente declarada y tambien el texto, se vuelca el la pantalla poniendo las coordenadas
    if tipoclick=="izq":
        sonido.play()#Reproduce el sonido previamente cargado



while True:#Bucle central del juego
    for event in pygame.event.get():#Esto de event devuelve todo lo que ocurra dentro de la ventana
        if event.type == pygame.QUIT:#Esto es para que se pueda cerrar
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:#Deteccion de clicks que luego se vuelca en una variable, aparte del click es recomendable hacer una variable por cada tecla que se usara
            if event.button==1:
                tipoclick="izq"
            if event.button==2:
                tipoclick="cen"
            if event.button==3:
                tipoclick="der"
            if event.button==4:
                tipoclick="scrsube"
            if event.button==5:
                tipoclick="scrbaja"
        
    screen.fill(cblanco)#Esto establece un color de fondo a la pantalla mediante rgb
    Update()
    pygame.display.flip()#Esto va dentro del bucle para que se actualice la pantalla
    clock.tick(60)#Establece cuantas veces se actualiza graficamente en un segundo
pygame.quit()
