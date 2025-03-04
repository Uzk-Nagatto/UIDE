import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana y zona de marcador
ANCHO, ALTO = 1000, 700
SCOREBOARD_HEIGHT = 100  # Altura reservada para el marcador
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong Mejorado")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)

# Fuentes
menu_font = pygame.font.SysFont("Courier New", 36, bold=True)
game_font = pygame.font.SysFont("Courier New", 50, bold=True)
instrucciones_font = pygame.font.SysFont("Courier New", 20, bold=True)
time_font = pygame.font.SysFont("Courier New", 28, bold=True)

# Dimensiones de las paletas y la pelota
PALA_ANCHO, PALA_ALTO = 10, 100
PELOTA_TAMANO = 10

# Definir la zona de juego (por debajo del marcador)
game_field_top = SCOREBOARD_HEIGHT
game_field_height = ALTO - SCOREBOARD_HEIGHT

# Posiciones iniciales de las paletas y la pelota
pala_izq = pygame.Rect(50, game_field_top + (game_field_height // 2) - (PALA_ALTO // 2), PALA_ANCHO, PALA_ALTO)
pala_der = pygame.Rect(ANCHO - 60, game_field_top + (game_field_height // 2) - (PALA_ALTO // 2), PALA_ANCHO, PALA_ALTO)
pelota = pygame.Rect((ANCHO // 2) - (PELOTA_TAMANO // 2), 
                      game_field_top + (game_field_height // 2) - (PELOTA_TAMANO // 2), 
                      PELOTA_TAMANO, PELOTA_TAMANO)

# Velocidades
pala_velocidad = 9
pelota_vel_x = 4
pelota_vel_y = 4
incremento_velocidad = 0.1

# Marcador y condición de victoria
puntos_izq = 0
puntos_der = 0
max_puntos = 5

# Reloj y control de tiempo
clock = pygame.time.Clock()
segundos = 0

# Estado de pausa
pausado = False

def mostrar_texto(texto, x, y, fuente, color=BLANCO):
    render = fuente.render(texto, True, color)
    VENTANA.blit(render, (x, y))

def dibujar_linea_central():
    # Dibuja la línea central en la zona de juego
    for i in range(game_field_top + 40, ALTO - 40, 20):
        if (i - game_field_top) % 40 == 0:
            pygame.draw.line(VENTANA, GRIS, (ANCHO // 2, i), (ANCHO // 2, i + 10), 2)

def dibujar_scoreboard():
    # Dibuja el área del marcador y la línea horizontal de separación
    pygame.draw.rect(VENTANA, NEGRO, (0, 0, ANCHO, SCOREBOARD_HEIGHT))
    # Contador de tiempo en dos líneas, centrado
    time_label = "TIEMPO"
    time_count = str(int(segundos))
    time_label_surface = time_font.render(time_label, True, BLANCO)
    time_count_surface = time_font.render(time_count, True, BLANCO)
    VENTANA.blit(time_label_surface, (ANCHO // 2 - time_label_surface.get_width() // 2, 10))
    VENTANA.blit(time_count_surface, (ANCHO // 2 - time_count_surface.get_width() // 2, 10 + time_label_surface.get_height()))
    # Puntos cerca de las esquinas
    jugador1_surface = game_font.render(str(puntos_izq), True, BLANCO)
    jugador2_surface = game_font.render(str(puntos_der), True, BLANCO)
    VENTANA.blit(jugador1_surface, (20, 20))
    VENTANA.blit(jugador2_surface, (ANCHO - jugador2_surface.get_width() - 20, 20))
    # Línea horizontal que separa el marcador de la cancha (más gruesa)
    pygame.draw.line(VENTANA, BLANCO, (0, SCOREBOARD_HEIGHT), (ANCHO, SCOREBOARD_HEIGHT), 4)

def cuenta_regresiva():
    # Cuenta regresiva centrada en la ventana completa
    for i in range(3, 0, -1):
        VENTANA.fill(NEGRO)
        dibujar_scoreboard()
        dibujar_linea_central()
        pygame.draw.rect(VENTANA, BLANCO, pala_izq)
        pygame.draw.rect(VENTANA, BLANCO, pala_der)
        count_surface = game_font.render(str(i), True, BLANCO)
        x = (ANCHO - count_surface.get_width()) // 2
        y = (ALTO - count_surface.get_height()) // 2
        VENTANA.blit(count_surface, (x, y))
        pygame.display.update()
        time.sleep(1)

def instrucciones():
    # Instrucciones paginadas con texto amigable
    instrucciones_text = [
        "¡Bienvenido a Pong Mejorado!",
        "",
        "Objetivo:",
        "Evita que la pelota se salga de tu lado.",
        "Cada vez que la pelota pase tu paleta, tu contrincante anota un punto.",
        "El primer jugador en llegar a 5 puntos gana el partido.",
        "",
        "Controles:",
        "JUGADOR 1 (lado izquierdo): usa 'W' para subir y 'S' para bajar.",
        "JUGADOR 2 (lado derecho en modo MULTIJUGADOR): utiliza las flechas ARRIBA y ABAJO.",
        "En el modo VS IA, la paleta derecha es controlada por la IA (JUGADOR IA).",
        "¡No te preocupes, la IA tiene fallos y puedes ganarle!",
        "",
        "Durante el juego, presiona 'P' para pausar o reanudar.",
        "",
        "Cuando termine el partido, verás un mensaje de victoria.",
        "Presiona cualquier tecla para volver al menú principal.",
        "",
        "¡Diviértete y buena suerte!"
    ]
    lines_per_page = 14
    total_lines = len(instrucciones_text)
    current_line = 0
    while current_line < total_lines:
        VENTANA.fill(NEGRO)
        for i in range(lines_per_page):
            if current_line + i >= total_lines:
                break
            mostrar_texto(instrucciones_text[current_line + i], 20, 30 + i * 30, instrucciones_font)
        pygame.display.update()
        espera_tecla()
        current_line += lines_per_page
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

def pausar_juego():
    global pausado
    pausado = True
    mostrar_texto("PAUSA", ANCHO // 2 - 60, game_field_top + (game_field_height // 2) - 30, game_font)
    pygame.display.update()
    espera_tecla()
    pausado = False
    cuenta_regresiva()

def menu_principal():
    while True:
        VENTANA.fill(NEGRO)
        mostrar_texto("1. JUGAR VS IA", ANCHO // 2 - 250, 180, menu_font)
        mostrar_texto("2. MULTIJUGADOR", ANCHO // 2 - 250, 240, menu_font)
        mostrar_texto("3. INSTRUCCIONES", ANCHO // 2 - 250, 300, menu_font)
        mostrar_texto("4. SALIR", ANCHO // 2 - 250, 360, menu_font)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "IA"
                if event.key == pygame.K_2:
                    return "MULTIJUGADOR"
                if event.key == pygame.K_3:
                    instrucciones()
                if event.key == pygame.K_4:
                    pygame.quit()
                    exit()

def mover_ia():
    # Movimiento de la IA más fluido: se calcula un objetivo basado en la posición de la pelota
    # con un pequeño error (entre -5 y 5) y se mueve gradualmente la paleta.
    error = random.randint(-5, 5)
    objetivo = pelota.centery + error
    diferencia = objetivo - pala_der.centery
    if abs(diferencia) < 2:
        movimiento = diferencia
    else:
        movimiento = pala_velocidad if diferencia > 0 else -pala_velocidad
    if (pala_der.top + movimiento) >= game_field_top and (pala_der.bottom + movimiento) <= ALTO:
        pala_der.y += movimiento

def reiniciar_posiciones():
    # Reinicia posiciones con cuenta regresiva (usado al anotar un punto)
    global pelota_vel_x, pelota_vel_y
    pala_izq.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pala_der.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pelota.center = (ANCHO // 2, game_field_top + (game_field_height // 2))
    pelota_vel_x = 4 * random.choice([-1, 1])
    pelota_vel_y = 4 * random.choice([-1, 1])
    cuenta_regresiva()

def reiniciar_posiciones_sin_countdown():
    # Reinicia posiciones sin mostrar cuenta regresiva (usado al terminar el juego)
    global pelota_vel_x, pelota_vel_y
    pala_izq.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pala_der.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pelota.center = (ANCHO // 2, game_field_top + (game_field_height // 2))
    pelota_vel_x = 4 * random.choice([-1, 1])
    pelota_vel_y = 4 * random.choice([-1, 1])

# --- Programa principal ---

modo_juego = menu_principal()
cuenta_regresiva()

running = True
segundos = 0
puntos_izq = 0
puntos_der = 0

while running:
    clock.tick(60)
    segundos += 1 / 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausar_juego()

    keys = pygame.key.get_pressed()
    # Movimiento del JUGADOR 1 (izquierda) sin salir de la zona de juego
    if keys[pygame.K_w] and pala_izq.top > game_field_top:
        pala_izq.y -= pala_velocidad
    if keys[pygame.K_s] and pala_izq.bottom < ALTO:
        pala_izq.y += pala_velocidad

    # Movimiento de la paleta derecha según el modo seleccionado
    if modo_juego == "MULTIJUGADOR":
        if keys[pygame.K_UP] and pala_der.top > game_field_top:
            pala_der.y -= pala_velocidad
        if keys[pygame.K_DOWN] and pala_der.bottom < ALTO:
            pala_der.y += pala_velocidad
    else:
        mover_ia()

    # Movimiento de la pelota
    pelota.x += pelota_vel_x
    pelota.y += pelota_vel_y

    # Rebote en los bordes de la zona de juego
    if pelota.top <= game_field_top or pelota.bottom >= ALTO:
        pelota_vel_y *= -1

    # Colisión con las paletas
    if pelota.colliderect(pala_izq) or pelota.colliderect(pala_der):
        pelota_vel_x *= -1
        pelota_vel_x *= (1 + incremento_velocidad)
        if abs(pelota_vel_x) > pala_velocidad:
            pelota_vel_x = pala_velocidad if pelota_vel_x > 0 else -pala_velocidad

    # Actualización de puntuaciones
    if pelota.left <= 0:
        puntos_der += 1
        reiniciar_posiciones()
    elif pelota.right >= ANCHO:
        puntos_izq += 1
        reiniciar_posiciones()

    # Condición de victoria: se imprime el ganador inmediatamente sin cuenta regresiva
    if puntos_izq >= max_puntos or puntos_der >= max_puntos:
        VENTANA.fill(NEGRO)
        dibujar_scoreboard()
        dibujar_linea_central()
        if puntos_izq >= max_puntos:
            mensaje = "JUGADOR 1 HA GANADO!"
        else:
            mensaje = "JUGADOR IA HA GANADO!" if modo_juego != "MULTIJUGADOR" else "JUGADOR 2 HA GANADO!"
        mensaje_surface = game_font.render(mensaje, True, BLANCO)
        x = (ANCHO - mensaje_surface.get_width()) // 2
        y = (ALTO - mensaje_surface.get_height()) // 2
        VENTANA.blit(mensaje_surface, (x, y))
        pygame.display.update()
        espera_tecla()  # Espera cualquier tecla para volver al menú
        puntos_izq = 0
        puntos_der = 0
        modo_juego = menu_principal()
        reiniciar_posiciones_sin_countdown()
        segundos = 0

    # Dibujo general: primero el marcador, luego la cancha
    VENTANA.fill(NEGRO)
    dibujar_scoreboard()
    dibujar_linea_central()
    pygame.draw.rect(VENTANA, BLANCO, pala_izq)
    pygame.draw.rect(VENTANA, BLANCO, pala_der)
    pygame.draw.ellipse(VENTANA, BLANCO, pelota)

    pygame.display.update()

pygame.quit()
