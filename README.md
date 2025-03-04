UIDE - Pong Mejorado
Proyecto Integrador:
"El impacto de las nuevas tecnologías en la sociedad: visualización del futuro"

Asignatura: Lógica de Programación
Universidad: Universidad Internacional del Ecuador (UIDE)
Desarrollado por: Christian Escalante

Descripción General
Este proyecto es una versión mejorada del clásico juego Atari Pong, desarrollado en Python utilizando la biblioteca Pygame. La aplicación integra mejoras en la jugabilidad, interfaz, inteligencia artificial y estructura del código, basándose en conceptos de programación funcional, manejo de eventos y diseño de interfaces aprendidos en clase. Además, se incluyó la retroalimentación recibida en trabajos previos para optimizar aspectos como el menú principal, las instrucciones, la cuenta regresiva, el sistema de vidas, y el movimiento de la IA.

Como parte del proceso de entrega, además del código fuente (.py), se ha convertido el juego a un archivo ejecutable (.exe) para facilitar su distribución y ejecución en sistemas Windows. Ambos formatos se encuentran en el repositorio.

Características y Mejoras Implementadas
Menú Principal Interactivo:

Opciones: JUGAR VS IA, MULTIJUGADOR, INSTRUCCIONES y SALIR.
Navegación intuitiva mediante pulsación de teclas.
Instrucciones Paginadas y Amigables:

Se presenta la información en varias páginas, permitiendo al usuario avanzar con una pulsación de tecla.
Explicación detallada de controles, reglas del juego y objetivos.
Cuenta Regresiva y Reinicio Inmediato:

Se muestra una cuenta regresiva centrada en la pantalla antes de iniciar cada partida o tras anotar un punto.
Al finalizar el juego (cuando un jugador alcanza 5 puntos), se muestra el mensaje de victoria de inmediato y se reinician las posiciones y el contador de tiempo sin volver a la cuenta regresiva.
Sistema de Vidas:

Cada jugador inicia con 3 vidas.
Se actualiza el marcador en función de las vidas restantes y se reinicia la partida tras la pérdida de una vida.
Movimiento de la Pelota y Colisiones:

La pelota rebota al tocar los bordes superior e inferior de la ventana.
Detecta colisiones con las paletas, rebotando en la dirección contraria y aumentando ligeramente la velocidad (limitada a la velocidad de las paletas).
Inteligencia Artificial Mejorada:

La paleta controlada por la IA se mueve de forma fluida y proporcional hacia la posición de la pelota, incorporando un pequeño margen de error para facilitar la posibilidad de ganarle al sistema.
Zona de Marcador Independiente:

La parte superior de la pantalla se reserva para mostrar el tiempo transcurrido y el puntaje de cada jugador, separada visualmente del área de juego por una línea divisoria gruesa.
Conversión a Archivo Ejecutable (.exe):

Además del código fuente en formato Python (.py), el proyecto se ha convertido a un archivo .exe, el cual se encuentra en el repositorio para facilitar su ejecución en entornos Windows sin necesidad de instalar Python o Pygame.
Requisitos
Python: Versión 3.6 o superior.
Pygame: Versión compatible con Python (se instala vía pip).
Instalación y Ejecución
1. Instalación de Python y Pygame
Instalar Python
Descarga la versión más reciente de Python en python.org.
Durante la instalación, asegúrate de marcar la opción "Add Python to PATH".
Instalar Pygame
Abre una terminal o consola de comandos y ejecuta:

bash
Copiar
python -m pip install pygame
O, si tienes varias versiones instaladas:

bash
Copiar
py -3 -m pip install pygame
Para verificar la instalación, ejecuta:

bash
Copiar
python -m pygame.examples.aliens
Si se abre una ventana de juego, la instalación fue exitosa.

2. Clonar el Repositorio
Clona el repositorio desde GitHub:

bash
Copiar
git clone https://github.com/Uzk-Nagatto/UIDE.git
3. Ejecución del Juego
Desde el Código Fuente (.py)
Navega a la carpeta del proyecto y ejecuta:

bash
Copiar
python "Juego atari pong.py"
Ejecutar el Archivo .exe
En el repositorio encontrarás el archivo PongMejorado.exe.
Simplemente haz doble clic en el archivo para iniciar el juego sin necesidad de tener Python instalado.
Desarrollo y Proceso de Mejoras
El desarrollo del proyecto se realizó en 8 semanas, integrando los siguientes procesos:

Diseño y Diagramas:

Se crearon diagramas de flujo, casos de uso y de arquitectura para definir la estructura del juego.
Se simplificó el flujo eliminando funciones redundantes, optimizando la lógica y mejorando la interacción del usuario.
Implementación del Código:

Se desarrolló la lógica del juego (movimiento, colisiones, sistema de vidas, cuenta regresiva).
Se implementó un menú interactivo e instrucciones paginadas para mejorar la experiencia del usuario.
Se optimizó el movimiento de la IA y se implementó un reinicio sin cuenta regresiva tras finalizar el juego.
Retroalimentación y Autoaprendizaje:

Se aplicaron mejoras basadas en la retroalimentación de la Ing. Estefanía Heredia y en trabajos autónomos previos.
Se consultaron diversas fuentes, como artículos académicos y documentación oficial de Pygame, para optimizar el diseño y la implementación.
Conversión a .exe:

Para facilitar la distribución, se utilizó una herramienta (por ejemplo, PyInstaller) para convertir el código Python en un ejecutable (.exe), el cual se incluye en el repositorio.
Créditos
Desarrollado por: Christian Escalante
Universidad: Universidad Internacional del Ecuador (UIDE)
Asignatura: Lógica de Programación

Licencia
Este proyecto está licenciado bajo la Licencia MIT.
