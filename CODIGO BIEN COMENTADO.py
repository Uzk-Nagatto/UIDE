import pygame
import time
import random

# =============================================================================
# INICIALIZACIÓN Y CONFIGURACIÓN DE LA VENTANA
# =============================================================================
pygame.init()  # Inicializamos Pygame para poder usar sus funcionalidades

# Definimos las dimensiones de la ventana. En esta versión, se ha aumentado la resolución
# a 1000x700 para dar más espacio al marcador y a la cancha.
ANCHO, ALTO = 1000, 700
SCOREBOARD_HEIGHT = 100  # Reservamos 100 píxeles en la parte superior para el marcador
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong Mejorado")

# =============================================================================
# DEFINICIÓN DE COLORES Y FUENTES
# =============================================================================
# Colores en formato RGB que utilizamos en todo el juego
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)

# Se definen varias fuentes para distintos propósitos:
# - menu_font: para el menú principal
# - game_font: para mostrar el puntaje y mensajes importantes
# - instrucciones_font: para las instrucciones (tamaño reducido para que todo entre)
# - time_font: para mostrar el contador de tiempo
menu_font = pygame.font.SysFont("Courier New", 36, bold=True)
game_font = pygame.font.SysFont("Courier New", 50, bold=True)
instrucciones_font = pygame.font.SysFont("Courier New", 20, bold=True)
time_font = pygame.font.SysFont("Courier New", 28, bold=True)

# =============================================================================
# CONFIGURACIÓN DE LOS ELEMENTOS DEL JUEGO
# =============================================================================
# Establecemos las dimensiones de las paletas y la pelota
PALA_ANCHO, PALA_ALTO = 10, 100
PELOTA_TAMANO = 10

# Definimos la zona de juego: el campo de juego empieza justo debajo del marcador.
game_field_top = SCOREBOARD_HEIGHT
game_field_height = ALTO - SCOREBOARD_HEIGHT

# Inicializamos las paletas y la pelota en sus posiciones iniciales.
# La paleta izquierda se coloca a 50 píxeles del borde izquierdo,
# y la paleta derecha a 60 píxeles del borde derecho.
pala_izq = pygame.Rect(50, game_field_top + (game_field_height // 2) - (PALA_ALTO // 2), PALA_ANCHO, PALA_ALTO)
pala_der = pygame.Rect(ANCHO - 60, game_field_top + (game_field_height // 2) - (PALA_ALTO // 2), PALA_ANCHO, PALA_ALTO)
pelota = pygame.Rect((ANCHO // 2) - (PELOTA_TAMANO // 2), 
                      game_field_top + (game_field_height // 2) - (PELOTA_TAMANO // 2), 
                      PELOTA_TAMANO, PELOTA_TAMANO)

# =============================================================================
# VARIABLES DE VELOCIDAD, PUNTOS Y CONTROL DEL TIEMPO
# =============================================================================
# Estas variables controlan el movimiento de las paletas y la pelota.
# Se han ajustado para mejorar la jugabilidad y que la velocidad de la pelota
# nunca supere la de las paletas.
pala_velocidad = 9
pelota_vel_x = 4
pelota_vel_y = 4
incremento_velocidad = 0.1  # Incremento de velocidad tras colisión, pero se limita a la velocidad de las paletas

# Marcador: cada jugador inicia con 0 puntos y se define el puntaje máximo (5) para determinar el ganador.
puntos_izq = 0
puntos_der = 0
max_puntos = 5

# Usamos un reloj para controlar los FPS (60 en este caso) y un contador de tiempo para la partida.
clock = pygame.time.Clock()
segundos = 0

# Variable para gestionar el estado de pausa del juego.
pausado = False

# =============================================================================
# FUNCIONES DE UTILIDAD Y DE INTERFAZ
# =============================================================================

def mostrar_texto(texto, x, y, fuente, color=BLANCO):
    """
    Renderiza y dibuja un texto en la pantalla.
    Parámetros:
      - texto: el contenido que queremos mostrar.
      - x, y: coordenadas donde se ubicará el texto.
      - fuente: objeto fuente para definir el estilo.
      - color: color del texto (por defecto, BLANCO).
    """
    render = fuente.render(texto, True, color)
    VENTANA.blit(render, (x, y))

def dibujar_linea_central():
    """
    Dibuja una línea discontinua en el centro de la cancha para separar las dos mitades.
    Esta función recorre la zona de juego (por debajo del marcador) y dibuja pequeñas líneas.
    """
    for i in range(game_field_top + 40, ALTO - 40, 20):
        if (i - game_field_top) % 40 == 0:
            pygame.draw.line(VENTANA, GRIS, (ANCHO // 2, i), (ANCHO // 2, i + 10), 2)

def dibujar_scoreboard():
    """
    Dibuja el área del marcador en la parte superior de la pantalla.
    Muestra el tiempo transcurrido (etiqueta "TIEMPO") y los puntos de cada jugador.
    Además, separa visualmente el marcador del campo de juego mediante una línea horizontal gruesa.
    """
    pygame.draw.rect(VENTANA, NEGRO, (0, 0, ANCHO, SCOREBOARD_HEIGHT))
    # Mostramos el tiempo en dos líneas: etiqueta y número
    time_label = "TIEMPO"
    time_count = str(int(segundos))
    time_label_surface = time_font.render(time_label, True, BLANCO)
    time_count_surface = time_font.render(time_count, True, BLANCO)
    VENTANA.blit(time_label_surface, (ANCHO // 2 - time_label_surface.get_width() // 2, 10))
    VENTANA.blit(time_count_surface, (ANCHO // 2 - time_count_surface.get_width() // 2, 10 + time_label_surface.get_height()))
    # Mostramos los puntajes en las esquinas
    jugador1_surface = game_font.render(str(puntos_izq), True, BLANCO)
    jugador2_surface = game_font.render(str(puntos_der), True, BLANCO)
    VENTANA.blit(jugador1_surface, (20, 20))
    VENTANA.blit(jugador2_surface, (ANCHO - jugador2_surface.get_width() - 20, 20))
    # Dibujamos la línea divisoria entre el marcador y el campo de juego (4 píxeles de grosor)
    pygame.draw.line(VENTANA, BLANCO, (0, SCOREBOARD_HEIGHT), (ANCHO, SCOREBOARD_HEIGHT), 4)

def cuenta_regresiva():
    """
    Muestra una cuenta regresiva (de 3 a 1) centrada en la ventana.
    A diferencia de versiones anteriores, ahora el número se centra perfectamente en pantalla,
    lo que mejora la estética y la preparación del jugador.
    """
    for i in range(3, 0, -1):
        VENTANA.fill(NEGRO)
        dibujar_scoreboard()
        dibujar_linea_central()
        # Se dibujan las paletas para mantener el contexto visual
        pygame.draw.rect(VENTANA, BLANCO, pala_izq)
        pygame.draw.rect(VENTANA, BLANCO, pala_der)
        # Renderizamos el número de la cuenta regresiva y lo centramos
        count_surface = game_font.render(str(i), True, BLANCO)
        x = (ANCHO - count_surface.get_width()) // 2
        y = (ALTO - count_surface.get_height()) // 2
        VENTANA.blit(count_surface, (x, y))
        pygame.display.update()
        time.sleep(1)

def instrucciones():
    """
    Muestra las instrucciones del juego de forma paginada y amigable.
    El texto se divide en páginas (14 líneas por página) para que toda la información sea visible,
    y se espera la pulsación de una tecla para avanzar a la siguiente página.
    """
    instrucciones_text = [
        "¡Bienvenido a Pong Mejorado!",
        "",
        "Objetivo:",
        "Evita que la pelota se salga de tu lado.",
        "Cada vez que la pelota pase tu paleta, el contrincante anota un punto.",
        "El primer jugador en llegar a 5 puntos gana el partido.",
        "",
        "Controles:",
        "JUGADOR 1 (lado izquierdo): usa 'W' para subir y 'S' para bajar.",
        "JUGADOR 2 (modo MULTIJUGADOR): usa las flechas ARRIBA y ABAJO.",
        "En VS IA, la paleta derecha es controlada por la IA (JUGADOR IA).",
        "¡La IA tiene fallos para que puedas ganarle!",
        "",
        "Durante el juego, presiona 'P' para pausar o reanudar.",
        "",
        "Al finalizar el partido, verás un mensaje de victoria.",
        "Presiona cualquier tecla para volver al menú principal.",
        "",
        "¡Diviértete y buena suerte!"
    ]
    lines_per_page = 14  # Se muestran 14 líneas por página para aprovechar el espacio
    total_lines = len(instrucciones_text)
    current_line = 0
    # Se recorre el contenido y se muestra página por página
    while current_line < total_lines:
        VENTANA.fill(NEGRO)
        for i in range(lines_per_page):
            if current_line + i >= total_lines:
                break
            mostrar_texto(instrucciones_text[current_line + i], 20, 30 + i * 30, instrucciones_font)
        pygame.display.update()
        espera_tecla()  # Avanza a la siguiente página tras pulsar una tecla
        current_line += lines_per_page
    # Se espera una pulsación final para salir de la pantalla de instrucciones
    espera_tecla()

def espera_tecla():
    """
    Función que espera hasta que el usuario presione cualquier tecla.
    Se utiliza en instrucciones, cuenta regresiva y pausa, asegurando que el usuario
    lea el contenido antes de avanzar.
    """
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                esperando = False

def pausar_juego():
    """
    Pausa el juego mostrando el mensaje 'PAUSA' en el centro del área de juego.
    Al presionar una tecla, el juego se reanuda y se muestra una cuenta regresiva
    para preparar a los jugadores para continuar.
    """
    global pausado
    pausado = True
    mostrar_texto("PAUSA", ANCHO // 2 - 60, game_field_top + (game_field_height // 2) - 30, game_font)
    pygame.display.update()
    espera_tecla()
    pausado = False
    cuenta_regresiva()

def menu_principal():
    """
    Muestra el menú principal del juego con las opciones:
      1. JUGAR VS IA
      2. MULTIJUGADOR
      3. INSTRUCCIONES
      4. SALIR
    El menú ha sido rediseñado para facilitar la navegación y la selección del modo de juego.
    Retorna "IA" o "MULTIJUGADOR" según la opción seleccionada.
    """
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
    """
    Controla el movimiento de la paleta controlada por la IA.
    Se calcula un "objetivo" basado en la posición de la pelota, se añade un pequeño error
    (entre -5 y 5) y se mueve la paleta gradualmente hacia ese objetivo, de manera que el movimiento sea suave.
    Esta mejora permite que la IA no sea infalible, aumentando la posibilidad de que el jugador le gane.
    """
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
    """
    Reinicia la posición de las paletas y la pelota tras que se anote un punto.
    Se muestra la cuenta regresiva para que los jugadores se preparen para el siguiente lanzamiento.
    """
    global pelota_vel_x, pelota_vel_y
    # Se posicionan las paletas en el centro vertical del área de juego
    pala_izq.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pala_der.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    # La pelota se centra en la pantalla
    pelota.center = (ANCHO // 2, game_field_top + (game_field_height // 2))
    # Se asigna una dirección aleatoria a la pelota
    pelota_vel_x = 4 * random.choice([-1, 1])
    pelota_vel_y = 4 * random.choice([-1, 1])
    cuenta_regresiva()

def reiniciar_posiciones_sin_countdown():
    """
    Reinicia la posición de las paletas y la pelota sin mostrar la cuenta regresiva.
    Esta función se utiliza al terminar el juego (cuando se muestra el mensaje de victoria),
    para que al iniciar un nuevo juego el tiempo se reinicie inmediatamente.
    """
    global pelota_vel_x, pelota_vel_y
    pala_izq.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pala_der.y = game_field_top + (game_field_height // 2) - (PALA_ALTO // 2)
    pelota.center = (ANCHO // 2, game_field_top + (game_field_height // 2))
    pelota_vel_x = 4 * random.choice([-1, 1])
    pelota_vel_y = 4 * random.choice([-1, 1])

# =============================================================================
# BUCLE PRINCIPAL DEL JUEGO
# =============================================================================

# Se muestra el menú principal y se inicia la cuenta regresiva antes de la partida.
modo_juego = menu_principal()
cuenta_regresiva()

# Reiniciamos el contador de tiempo y el marcador al iniciar el juego.
running = True
segundos = 0
puntos_izq = 0
puntos_der = 0

while running:
    clock.tick(60)  # Se fija el framerate a 60 FPS
    segundos += 1 / 60  # Se actualiza el contador de tiempo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Permite pausar el juego presionando la tecla 'P'
            if event.key == pygame.K_p:
                pausar_juego()

    keys = pygame.key.get_pressed()
    # Movimiento del Jugador 1 (lado izquierdo), limitado al área de juego
    if keys[pygame.K_w] and pala_izq.top > game_field_top:
        pala_izq.y -= pala_velocidad
    if keys[pygame.K_s] and pala_izq.bottom < ALTO:
        pala_izq.y += pala_velocidad

    # Movimiento de la paleta derecha:
    # - En MULTIJUGADOR, el jugador usa las flechas.
    # - En VS IA, se llama a la función mover_ia() para que la computadora controle la paleta.
    if modo_juego == "MULTIJUGADOR":
        if keys[pygame.K_UP] and pala_der.top > game_field_top:
            pala_der.y -= pala_velocidad
        if keys[pygame.K_DOWN] and pala_der.bottom < ALTO:
            pala_der.y += pala_velocidad
    else:
        mover_ia()

    # Actualiza la posición de la pelota
    pelota.x += pelota_vel_x
    pelota.y += pelota_vel_y

    # Rebote de la pelota en los bordes del campo de juego
    if pelota.top <= game_field_top or pelota.bottom >= ALTO:
        pelota_vel_y *= -1

    # Colisiones con las paletas:
    # Se invierte la dirección de la pelota y se incrementa la velocidad de manera controlada,
    # para que la velocidad no supere la de la paleta.
    if pelota.colliderect(pala_izq) or pelota.colliderect(pala_der):
        pelota_vel_x *= -1
        pelota_vel_x *= (1 + incremento_velocidad)
        if abs(pelota_vel_x) > pala_velocidad:
            pelota_vel_x = pala_velocidad if pelota_vel_x > 0 else -pala_velocidad

    # Actualización del marcador:
    # Si la pelota sale por el borde izquierdo, se reduce una vida del Jugador 1;
    # si sale por el derecho, se reduce una vida del Jugador 2.
    if pelota.left <= 0:
        puntos_der += 1
        reiniciar_posiciones()
    elif pelota.right >= ANCHO:
        puntos_izq += 1
        reiniciar_posiciones()

    # Condición de victoria:
    # Cuando un jugador alcanza el puntaje máximo, se muestra el mensaje de victoria
    # inmediatamente (sin nueva cuenta regresiva) y se reinicia el juego.
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
        espera_tecla()  # Se espera que el usuario presione una tecla para volver al menú
        puntos_izq = 0
        puntos_der = 0
        modo_juego = menu_principal()
        reiniciar_posiciones_sin_countdown()
        segundos = 0  # Reinicia el contador de tiempo

    # Dibuja el marcador y la cancha en cada iteración
    VENTANA.fill(NEGRO)
    dibujar_scoreboard()
    dibujar_linea_central()
    pygame.draw.rect(VENTANA, BLANCO, pala_izq)
    pygame.draw.rect(VENTANA, BLANCO, pala_der)
    pygame.draw.ellipse(VENTANA, BLANCO, pelota)

    pygame.display.update()

pygame.quit()


