import pygame
import time

# Inicializamos pygame
pygame.init()

# Definimos el tamaño de la ventana
ANCHO = 900
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong Mejorado")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Paletas y pelota
paleta1 = pygame.Rect(20, ALTO // 2 - 50, 10, 100)
paleta2 = pygame.Rect(ANCHO - 30, ALTO // 2 - 50, 10, 100)
pelota = pygame.Rect(ANCHO // 2, ALTO // 2, 10, 10)

# Velocidades
vel_x = 5
vel_y = 5
vel_paleta = 10

# Vidas de los jugadores
vidas_jugador1 = 3
vidas_jugador2 = 3

# Fuente para texto más pequeña y clara
fuente = pygame.font.SysFont("Courier New", 24, bold=True)

def mostrar_texto(texto, x, y):
    superficie_texto = fuente.render(texto, True, BLANCO)
    pantalla.blit(superficie_texto, (x, y))

def cuenta_regresiva():
    for i in range(3, 0, -1):
        pantalla.fill(NEGRO)
        mostrar_texto(f"{i}", ANCHO // 2 - 10, ALTO // 2 - 20)
        pygame.display.flip()
        time.sleep(1)

def mostrar_instrucciones():
    pantalla.fill(NEGRO)
    mostrar_texto("Instrucciones del Juego:", ANCHO // 2 - 200, 150)
    mostrar_texto("- Jugador 1: W para subir, S para bajar", ANCHO // 2 - 250, 200)
    mostrar_texto("- Jugador 2: Flecha arriba para subir, Flecha abajo para bajar", ANCHO // 2 - 250, 230)
    mostrar_texto("- El objetivo es evitar que la pelota salga por tu lado", ANCHO // 2 - 250, 260)
    mostrar_texto("Presiona cualquier tecla para regresar", ANCHO // 2 - 200, 310)
    pygame.display.flip()
    espera_tecla()

def espera_tecla():
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                esperando = False

def menu_principal():
    menu = True
    while menu:
        pantalla.fill(NEGRO)
        mostrar_texto("1. Jugar", ANCHO // 2 - 80, 180)
        mostrar_texto("2. Instrucciones", ANCHO // 2 - 80, 220)
        mostrar_texto("3. Salir", ANCHO // 2 - 80, 260)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return
                if event.key == pygame.K_2:
                    mostrar_instrucciones()
                if event.key == pygame.K_3:
                    pygame.quit()
                    exit()

# Bucle del juego
clock = pygame.time.Clock()
while True:
    menu_principal()
    cuenta_regresiva()
    
    tiempo_inicio = time.time()
    vidas_jugador1 = 3
    vidas_jugador2 = 3
    running = True
    
    while running:
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, BLANCO, paleta1)
        pygame.draw.rect(pantalla, BLANCO, paleta2)
        pygame.draw.ellipse(pantalla, BLANCO, pelota)
        mostrar_texto(f"P1: {vidas_jugador1}", 50, 20)
        mostrar_texto(f"P2: {vidas_jugador2}", ANCHO - 120, 20)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paleta1.top > 0:
            paleta1.y -= vel_paleta
        if keys[pygame.K_s] and paleta1.bottom < ALTO:
            paleta1.y += vel_paleta
        if keys[pygame.K_UP] and paleta2.top > 0:
            paleta2.y -= vel_paleta
        if keys[pygame.K_DOWN] and paleta2.bottom < ALTO:
            paleta2.y += vel_paleta
        
        pelota.x += vel_x
        pelota.y += vel_y
        
        if pelota.top <= 0 or pelota.bottom >= ALTO:
            vel_y = -vel_y
        if pelota.colliderect(paleta1) or pelota.colliderect(paleta2):
            vel_x = -vel_x
        
        if pelota.left <= 0:
            vidas_jugador1 -= 1
            pelota.x = ANCHO // 2
            pelota.y = ALTO // 2
            cuenta_regresiva()
        elif pelota.right >= ANCHO:
            vidas_jugador2 -= 1
            pelota.x = ANCHO // 2
            pelota.y = ALTO // 2
            cuenta_regresiva()
        
        if vidas_jugador1 == 0 or vidas_jugador2 == 0:
            ganador = "Jugador 2" if vidas_jugador1 == 0 else "Jugador 1"
            mostrar_texto(f"{ganador} Gana!", ANCHO // 2 - 80, ALTO // 2 - 20)
            pygame.display.flip()
            time.sleep(3)
            running = False
        
        pygame.display.flip()
        clock.tick(60)
