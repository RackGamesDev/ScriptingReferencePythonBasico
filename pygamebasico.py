import pygame, sys, random, math#pygame se importa tras instalarse
pygame.init()#esta linea es para empezarlo, necesario
size = (512, 512)#tamagno inicial de ventana, las coordenadas se miden en pixeles y arriba izquierda es 0 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("titulo")#cambia el titulo de la ventana


class ObjConSprite(pygame.sprite.Sprite):#las variables que se hagan con esta clase seran como objetos con sprites, esta carga la imagen img.png
    def __init__(self, img, alpha, colkey):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(colkey)
        self.rect = self.image.get_rect()
        self.image.set_alpha(alpha)
        
class Game(object):#estructura recomendada para hacer pantallas, cada variable que se crea seria como una escena
    def __init__(self):
        #crear variables y objetos y etc: self.x=... tambien se suelen configurar las escenas
        pass
        
    def process_events(self):
        pass
    def run_logic(self):
        pass
    def display_frame(self):
        pass
    #crear tantas funciones como uieras
def main():#aqui se pondria la pantalla principal, mas tarde iria el bucle
    game=Game()

#aqui se suele poner el codigo start, normalmente para cargar cosas
cblanco=(255,255,255)#se suelen declarar tuplas de 3 numeros para colores
cnegro=(0,0,0)
crojo=(255,0,0)
cverde=(0,255,0)
cazul=(0,0,255)
tipoclick="no"#variable para el click que se configura en el bucle de abajo
fuente1=pygame.font.SysFont("monospace", 20)#establece una fuente, que debe estar instalada
texto=fuente1.render("hola", 1, cblanco,cnegro)#con la fuente establecida escribe algo, (texto, antialias1/0, colortexto, colorfondo)
clock = pygame.time.Clock()#variable usada para el tiempo
tiempo=0
imagen=pygame.image.load("bg.png").convert()#carga una imagen en memoria apartir de un archivo
imagen.set_colorkey(cblanco)#si la imagen aparece con un fondo aun siendo png, se usa esto especificando que color se va a quitar
imagen.set_alpha(200)#de 0 a 255 establece la opacidad, mayor el numero mayor opacidad
imagen = pygame.transform.scale(imagen, (400,400))#escala la imagen por pixeles en x y y
imagen = pygame.transform.rotate(imagen, 45)#rota la imagen alrededor de si misma x grados
#crear objetos con la clase de antes creada
sprListaObj=pygame.sprite.Group()#se suelen crear 2 listas, una que almacene todos los objetos de ese tipo
todSprLista=pygame.sprite.Group()#y otra que almacene todos los sprites en pantalla
for i in range(8):
    unobjeto=ObjConSprite(img="img.png", alpha=255, colkey=(255,255,255))
    unobjeto.rect.x=random.randrange(512)#establecer coordenadas
    unobjeto.rect.y=random.randrange(512)
    sprListaObj.add(unobjeto)#agregar los objetos en ambas listas
    todSprLista.add(unobjeto)
otroobjeto=ObjConSprite(img="img.png", alpha=255, colkey=(255,255,255))
otroobjeto.rect.x=random.randrange(512)
otroobjeto.rect.y=random.randrange(512)
sonido = pygame.mixer.Sound("snd.ogg")#carga un sonido en memoria para usarlo luego

def Update():#variable update en el juego, conviene ver la documentacion para ver mas funciones, para borrar un objeto dibujado simplemente no hay que renderizarlo en el proximo frame
    global todSprLista
    global tiempo
    global imagen
    global otroobjeto
    global tipoclick
    global sonido
    tiempo+=1
    screen.blit(imagen, [0,0])#renderiza la imagen donde le digas, la imagen sale tal cual esta sin antialias o redimensionar
    pygame.draw.line(screen, cnegro, [0,0], [50,50], 2)#dibujar linea (pantalla, color, xyinicio, xyfinal, grosor) medido en pixeles
    pygame.draw.rect(screen, cverde, (50,50,100,100), 3)#dibujar rectangulo (pantalla, color, (x,y,ancho,alto), ancho de linea(0 es relleno))
    pygame.draw.circle(screen, crojo, (200,100), 30, 0)#dibujar circulo (pantalla, color, (x,y), radio, ancho de linea(0 es relleno))
    pygame.draw.polygon(screen, cazul, ((100,100),(100,200),(200,300)), 0)#dibujar poligono (pantalla, color, ((x,y),(x,y),etc.)), ancho de linea(0 es relleno))
    pygame.draw.line(screen, cnegro, [0,0], [tiempo,50], 2)#ejemplo de animacion, una vez puesto el clock la variable tiempo se suma 60 veces por segundo
    xymouse = pygame.mouse.get_pos()#devuelve una tupla con las coordenadas x y y del raton dentro de la pantalla
    pygame.mouse.set_visible(0)#esconde el cursor, 1 es activo
    if event.type == pygame.KEYDOWN:#devuelve true si se empieza a presionar una tecla
        if event.key == pygame.K_LEFT:#luego se puede especificar que tecla, se ven con K_tecla
            print("presionar izquierda")
        print("presionar tecla")
    if event.type == pygame.KEYUP:#lo mismo pero cuando no se pulsa, igual a el if de antes si le pones un else
        if event.key == pygame.K_LEFT:
            print("soltar izquierda")
        print("soltar tecla")
    obj1=pygame.draw.circle(screen, crojo, (200,100), 30, 0)#normalmente los dibujos se guardan en variables
    obj2=pygame.draw.circle(screen, crojo, (350,100), 30, 0)
    if obj1.colliderect(obj2) or obj2.colliderect(obj1):#para detectar colisiones entre dibujos, hay que poner los dibujos en variables
        #print("choca")
        pass
    todSprLista.draw(screen)#con la lista de todos los sprites se pueden dibujar todos a la vez con esta linea
    todSprLista.remove(1)#otra forma de eliminar un dibujo si esta en una lista es quitarlo de la lista y ya
    #print(otroobjeto.rect.x)#para conseguir una coordenada de un objeto creado mediante esa clase de sprite
    listaHit=pygame.sprite.spritecollide(otroobjeto, sprListaObj, True)#esto hace una lista de las colisiones entre la variable otroobjeto y cualquiera de la lista sprlistaobj, el true del final indica que el objeto de la lista que toque desaparece
    for unobjeto in sprListaObj:#esto seria para ejecutar un evento por cada vez que choca
        #print("choca")
        pass
    screen.blit(texto, (100,100))#con la fuente declarada y tambien el texto, se vuelca el la pantalla poniendo las coordenadas
    if tipoclick=="izq":
        sonido.play()#reproduce el sonido previamente cargado


    








while True:#bucle central del juego
    for event in pygame.event.get():#esto de event devuelve todo lo que ocurra dentro de la ventana
        if event.type == pygame.QUIT:#esto es para que se pueda cerrar
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:#deteccion de clicks que luego se vuelca en una variable, aparte del click es recomendable hacer una variable por cada tecla que se usara
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
        
    screen.fill(cblanco)#esto establece un color de fondo a la pantalla mediante rgb
    Update()
    pygame.display.flip()#esto va dentro del bucle para que se actualice la pantalla
    clock.tick(60)#establece cuantas veces se actualiza graficamente en un segundo
pygame.quit()
