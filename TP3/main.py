import soko
import gamelib
import menu
from juego import Juego

ANCHO_CELDA = 64
ALTO_CELDA = 64

RUTA_NIVELES = "niveles.txt"
RUTA_TECLAS = "teclas.txt"

LVL_KEYWORD = "Level"
TITLE_KEYWORD = "'"

SALIR = 'SALIR'
REINICIAR = 'REINICIAR'
DESHACER = 'DESHACER'
REHACER = 'REHACER'
PISTA = 'PISTA'
DIRECCIONES_MOVIMIENTO = {
    'NORTE': (0, -1), 'OESTE': (-1, 0), 'SUR': (0, 1), 'ESTE': (1, 0)
}

IMG_FOLDER = "img/"
IMG_PLAYER = IMG_FOLDER + "player.gif"
IMG_GROUND = IMG_FOLDER + "ground.gif"
IMG_GOAL = IMG_FOLDER + "goal.gif"
IMG_WALL = IMG_FOLDER + "wall.gif"
IMG_BOX = IMG_FOLDER + "box.gif"


# GUI
def actualizar_ventana_juego(juego):
    '''Recibe el grilla y el número del nivel y actualiza la ventana donde se muestra'''
    gamelib.draw_begin()
    for i in range(len(juego.grilla)):
        for j in range(len(juego.grilla[i])):
            x = j * ANCHO_CELDA
            y = i * ALTO_CELDA

            gamelib.draw_image(IMG_GROUND, x, y)

            if soko.hay_pared(juego.grilla, j, i):
                gamelib.draw_image(IMG_WALL, x, y)

            if soko.hay_jugador(juego.grilla, j, i):
                gamelib.draw_image(IMG_PLAYER, x, y)

            if soko.hay_caja(juego.grilla, j, i):
                gamelib.draw_image(IMG_BOX, x, y)

            if soko.hay_objetivo(juego.grilla, j, i):
                gamelib.draw_image(IMG_GOAL, x, y)

    gamelib.draw_end()


def actualizar_tamano_ventana_juego(juego):
    ''''Recibe el juego y actualiza la ventana segun el número y las dimensiones del nivel'''
    cant_c, cant_f,  = soko.dimensiones(juego.grilla)
    gamelib.resize(ANCHO_CELDA * cant_c, ALTO_CELDA * cant_f)
    gamelib.title(f'Sokoban - Nivel {juego.nivel_actual}')


# Carga de Datos
def matriz_rectangular(matriz):
    '''Recibe una matriz y devuelve la misma matriz rellena con 'soko.VACIO' para que sea rectangular'''
    ancho_matriz = len(max(matriz, key=len))

    for i, linea in enumerate(matriz):
        matriz[i] += soko.VACIO * (ancho_matriz - len(linea))
    return matriz


def cargar_teclas(ruta):
    '''Recible la ruta del archivo con teclas y devuelve un mapa del formato <tecla>:<accion>'''
    teclas = {}
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            if len(linea.rstrip().split(' = ')) == 2:
                tecla, accion = linea.rstrip().split(' = ')
                teclas[tecla] = accion
    return teclas


def cargar_niveles(ruta):
    '''Recible la ruta del archivo con niveles y devuelve un diccionario del formato <nro_nivel>:<desc_nivel>'''
    niveles = {}
    with open(ruta, 'r') as archivo:
        nro_nivel = 0
        desc_nivel = []
        linea = archivo.readline()

        while linea:
            if LVL_KEYWORD not in linea:
                linea = archivo.readline()
                continue

            nro_nivel = int(linea.rstrip().split()[1])
            linea = archivo.readline()

            if TITLE_KEYWORD in linea:
                linea = archivo.readline()

            while linea and linea.rstrip():
                desc_nivel.append(linea.rstrip())
                linea = archivo.readline()

            desc_nivel = matriz_rectangular(desc_nivel)
            niveles[nro_nivel] = desc_nivel
            desc_nivel = []

    return niveles


# Logica
def main():
    '''Ejecuta el juego SokoBan'''
    # Cargamos los niveles
    try:
        niveles = cargar_niveles(RUTA_NIVELES)
    except FileNotFoundError:
        gamelib.say("Error al cargar el archvivo 'niveles.txt'")
        return

    # Definimos las teclas
    try:
        teclas = cargar_teclas(RUTA_TECLAS)
    except FileNotFoundError:
        gamelib.say("Error al cargar el archvivo 'teclas.txt'")
        return

    # Inicializamos el estado del juego
    juego = Juego()

    while gamelib.is_alive():

        # Actualizar el Nivel actual mediante un menu o termina el juego
        if not juego.nivel_actual:
            nivel = menu.seleccionar_nivel(niveles)

            if not nivel:
                return

            grilla = soko.crear_grilla(niveles[nivel])
            juego = Juego(nivel, grilla)

            actualizar_tamano_ventana_juego(juego)

        actualizar_ventana_juego(juego)

        # Nivel terminado
        if soko.juego_ganado(juego.grilla):
            gamelib.say(f"Victoria nivel { juego.nivel_actual }")

            # Sokoban Ganado
            if juego.nivel_actual == max(niveles):
                gamelib.say(f"Juego terminado")
                juego = Juego()
                continue

            nivel = juego.nivel_actual + 1
            grilla = soko.crear_grilla(niveles[nivel])
            juego = Juego(nivel, grilla)

            actualizar_tamano_ventana_juego(juego)
            continue

        # Actualizar el estado del juego, según la `tecla` presionada
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key

        if tecla not in teclas:
            continue

        if teclas[tecla] == SALIR:
            juego = Juego()

        if teclas[tecla] in DIRECCIONES_MOVIMIENTO:
            juego.ejecutar_movimiento(DIRECCIONES_MOVIMIENTO[teclas[tecla]])

        if teclas[tecla] == REINICIAR:
            nivel = juego.nivel_actual
            grilla = soko.crear_grilla(niveles[juego.nivel_actual])
            juego = Juego(nivel, grilla)

        if teclas[tecla] == DESHACER:
            juego.deshacer()

        if teclas[tecla] == REHACER:
            juego.rehacer()

        if teclas[tecla] == PISTA:
            pista = juego.pista()
            if not pista:
                gamelib.say("No es resoluble, vuelva a intentar")
                continue
            juego.ejecutar_movimiento(pista)


gamelib.init(main)
