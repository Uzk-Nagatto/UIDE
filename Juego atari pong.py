import pygame

# Inicializamos pygame
pygame.init()

# Definimos el tamaño de la ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

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

# Bucle del juego
running = True
clock = pygame.time.Clock()

while running:
    pantalla.fill(NEGRO)

    # Dibujamos las paletas y la pelota
    pygame.draw.rect(pantalla, BLANCO, paleta1)
    pygame.draw.rect(pantalla, BLANCO, paleta2)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de la pelota
    pelota.x += vel_x
    pelota.y += vel_y

    # Rebote en los bordes
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        vel_y = -vel_y
    if pelota.colliderect(paleta1) or pelota.colliderect(paleta2):
        vel_x = -vel_x
    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.x = ANCHO // 2
        pelota.y = ALTO // 2
        vel_x = 5
        vel_y = 5

    # Control de las paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paleta1.top > 0:
        paleta1.y -= 10
    if keys[pygame.K_s] and paleta1.bottom < ALTO:
        paleta1.y += 10
    if keys[pygame.K_UP] and paleta2.top > 0:
        paleta2.y -= 10
    if keys[pygame.K_DOWN] and paleta2.bottom < ALTO:
        paleta2.y += 10

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla los FPS
    clock.tick(60)

pygame.quit()
