# UIDE
## Lógica de Programación

# Atari Pong en Python

Este es un juego básico de Pong hecho en Python usando la biblioteca **Pygame**. El juego tiene dos plataformas que los jugadores pueden mover para hacer rebotar la pelota. El objetivo es evitar que la pelota salga de la pantalla.

## Requisitos

- Python **3.6 o superior**.
- Pygame (versión compatible con la instalación de Python).

## Instalación

### 1. Instalar Python

Para instalar Python, visita el sitio oficial de Python y descarga la versión más reciente compatible con tu sistema operativo:

🔗 [Descargar Python](https://www.python.org/downloads/)

Asegúrate de marcar la opción **"Add Python to PATH"** durante la instalación.

### 2. Instalar Pygame

Una vez instalado Python, abre una terminal o consola de comandos y ejecuta:

```
python -m pip install pygame
```

Si tienes varias versiones de Python instaladas, usa:

```
py -3 -m pip install pygame
```

Para verificar que la instalación fue exitosa, ejecuta:

```
python -m pygame.examples.aliens
```

Si ves una ventana de juego, significa que **Pygame** está instalado correctamente.

### 3. Ejecutar el juego

Para correr el juego, abre una terminal en la carpeta donde está el archivo del juego y ejecuta:

```
Juego atari pong.py
```


## Mejoras implementadas

✅ **Menú principal**: Ahora el juego cuenta con un menú inicial con las siguientes opciones:
   - **Jugar**: Inicia el juego directamente.
   - **Instrucciones**: Muestra los controles y reglas del juego.
   - **Salir**: Permite cerrar el juego desde el menú.

   Para seleccionar una opción, el usuario debe presionar la tecla correspondiente al número de la opción deseada.

✅ **Instrucciones dentro del juego**: Se añadió una opción en el menú principal donde se explican los controles y reglas del juego, incluyendo cómo mover las paletas y el objetivo del juego.

✅ **Cuenta regresiva al inicio**: Antes de que la pelota comience a moverse, hay una cuenta regresiva de 3 segundos, permitiendo que los jugadores se preparen antes de comenzar.

✅ **Sistema de vidas**: Cada jugador tiene 3 vidas. Si la pelota cruza su lado de la pantalla, pierde una vida. El juego termina cuando un jugador se queda sin vidas y el otro se declara ganador.

✅ **Optimización del movimiento de las paletas**: Ahora los jugadores pueden mover sus paletas usando las siguientes teclas:
   - **Jugador 1**: Usa las teclas **W** (subir) y **S** (bajar) para mover la paleta.
   - **Jugador 2**: Usa las teclas de las flechas **Arriba** y **Abajo** para mover la paleta.

✅ **Reinicio del juego después de una partida**: Cuando un jugador pierde todas sus vidas, se muestra un mensaje indicando al ganador y el juego regresa automáticamente al menú principal para jugar nuevamente o salir.

## Funcionalidades generales

- **Rebotes**: La pelota rebota al tocar los bordes superior e inferior de la ventana.
- **Colisiones con las paletas**: Si la pelota toca alguna de las paletas, rebota en dirección contraria.
- **Reinicio de la pelota**: Si la pelota sale por el lado izquierdo o derecho de la pantalla, la pelota se reinicia en el centro.
- **Flujo continuo del juego**: El juego nunca se cierra abruptamente, siempre regresa al menú principal tras finalizar una partida.

## Créditos

Desarrollado por **Christian Escalante** como un proyecto de aprendizaje de **Pygame y Python** para la universidad **UIDE**.

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - Mira el archivo [LICENSE](LICENSE) para más detalles.
