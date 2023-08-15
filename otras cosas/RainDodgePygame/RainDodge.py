velocidad = 3
gravedad = 2
viento = 1
factorSum = 60
gotasInicial = 12







import pygame, sys, random, math
pygame.init()
size = (512, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RainDodge por RackGames/Yester")
clock = pygame.time.Clock()
cblanco = (255,255,255)
cnegro = (0,0,0)

class Gota(pygame.sprite.Sprite):
    def __init__(self, x, y, img, alpha):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image.set_alpha(alpha)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.scale(self.image, (64,64))
    def Actualizar(self):
        self.rect.y+=gravedad
        self.rect.x+=viento
        if self.rect.x > 512:
            self.rect.x=-17
        if self.rect.y > 512:
            self.rect.y=-17
            self.rect.x=random.randint(1, 511)

tetiempo=0
tiempo=0
tiempoGota=0
escena="menu"
gotasListaObj=pygame.sprite.Group()#lista con todas las gotas
spritesListaObj=pygame.sprite.Group()
fuente1=pygame.font.SysFont("monospace", 50)#fuente grande
textoTitulo=fuente1.render("RainDodge", 1, cblanco,cnegro)#texto titulo
fuente2=pygame.font.SysFont("monospace", 20)#fuente mediana
textoEmpieza=fuente2.render("Haz click para jugar", 1, cblanco,cnegro)#texto empezar
textoInfo1=fuente2.render("Te mueves con las flechas, ", 1, cblanco,cnegro)
textoInfo2=fuente2.render("evita tocar las gotas", 1, cblanco,cnegro)
textoMuere1=fuente1.render("FIN", 1, cblanco, cnegro)#texto perder
textoMuere2=fuente2.render("Hac click para reiniciar", 1, cblanco, cnegro)
fondo=pygame.image.load("fondo.png").convert()
jugador=Gota(256,256,"jugador.png", 255)
spritesListaObj.add(jugador)
#jugador=pygame.image.load("jugador.png").convert()
#jugador.set_colorkey((0,0,0))
sonido = pygame.mixer.Sound("snd.ogg")
posJugadorX = 256
posJugadorY = 256


def Update():
    global tiempo
    global tiempoGota
    global escena
    global fondo
    global gotasListaObj
    global posJugadorY
    global posJugadorX
    global tetiempo
    screen.blit(fondo, [0,0])
    
    if escena=="menu":
        screen.blit(textoTitulo, (32,64))
        screen.blit(textoEmpieza, (40,150))
        screen.blit(textoInfo1, (40, 180))
        screen.blit(textoInfo2, (40, 200))
        
    if escena=="juego":
        tiempo+=0.0166
        tiempoGota+=1
        textoTiempo=fuente2.render(str(tiempo), 1, cblanco, cnegro)
        screen.blit(textoTiempo, (10,10))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jugador.rect.y-=velocidad
            if event.key == pygame.K_DOWN:
                jugador.rect.y+=velocidad
            if event.key == pygame.K_LEFT:
                jugador.rect.x-=velocidad
            if event.key == pygame.K_RIGHT:
                jugador.rect.x+=velocidad
        if posJugadorX < 0:
            posJugadorX=511
        if posJugadorX >512:
            posJugadorX=1
        if posJugadorY < 0:
            posJugadorY=511
        if posJugadorY >512:
            posJugadorY=1
        #screen.blit(jugador, [posJugadorX, posJugadorY])
        
        if tiempoGota % factorSum == 0:
            gota=Gota(random.randint(1, 511), random.randint(-529, -17), "gota.png", 200)
            gotasListaObj.add(gota)
            spritesListaObj.add(gota)
            print("aumentando dificultad")
        for i in gotasListaObj:
            i.Actualizar()
        spritesListaObj.draw(screen)
        listahit=pygame.sprite.spritecollide(jugador, gotasListaObj, True)
        for obj in listahit:
            escena="perder"
            tetiempo=tiempo
            sonido.play()
                
    if escena=="perder":
        screen.blit(textoMuere1, (10,10))
        screen.blit(textoMuere2, (10,70))
        textoScore=fuente2.render("Aguantaste "+str(tetiempo), 1, cblanco, cnegro)
        screen.blit(textoScore, (10, 200))
        spritesListaObj.add(jugador)
        tiempo=0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if escena=="menu" or escena=="perder":
                escena="juego"
                sonido.play()
                for i in range(gotasInicial):
                    gota=Gota(random.randint(1, 511), random.randint(-529, -17), "gota.png", 200)
                    gotasListaObj.add(gota)
                    spritesListaObj.add(gota)
    screen.fill(cblanco)#esto establece un color de fondo a la pantalla mediante rgb
    Update()
    pygame.display.flip()#esto va dentro del bucle para que se actualice la pantalla
    clock.tick(60)#establece cuantas veces se actualiza graficamente en un segundo
pygame.quit()