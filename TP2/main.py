import soko
import gamelib
import menu

ANCHO_CELDA = 64
ALTO_CELDA = 64

RUTA_NIVELES = "niveles.txt"
RUTA_TECLAS = "teclas.txt"

LVL_KEYWORD = "Level"
TITLE_KEYWORD = "'"

SALIR = 'SALIR'
REINICIAR = 'REINICIAR'
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
def actualizar_ventana_tablero(tablero):
    '''Recibe el tablero y el numero del nivel y actualiza la ventana donde se muestra'''

    gamelib.draw_begin()
    for i, fila in enumerate(tablero):
        for j, _ in enumerate(fila):
            x = j * ANCHO_CELDA
            y = i * ALTO_CELDA

            gamelib.draw_image(IMG_GROUND, x, y)

            if soko.hay_pared(tablero, j, i):
                gamelib.draw_image(IMG_WALL, x, y)

            if soko.hay_jugador(tablero, j, i):
                gamelib.draw_image(IMG_PLAYER, x, y)

            if soko.hay_caja(tablero, j, i):
                gamelib.draw_image(IMG_BOX, x, y)

            if soko.hay_objetivo(tablero, j, i):
                gamelib.draw_image(IMG_GOAL, x, y)

    gamelib.draw_end()


# Carga de Datos

def matriz_rectangular(matriz):
    '''Recibe una matriz y devuelve la misma matriz rellena con soko.VACIO para que sea rectangular'''
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
    '''Recible la ruta del archivo con niveles y devuelve un mapa del formato <nro_nivel>:<desc_nivel>'''
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


def main():
    '''Ejecuta el juego SokoBan'''

    try:
        # Cargamos los niveles
        niveles = cargar_niveles(RUTA_NIVELES)
    except FileNotFoundError:
        gamelib.say("Error al cargar el archvivo 'niveles.txt'")
        return

    try:
        # Definimos las teclas
        teclas = cargar_teclas(RUTA_TECLAS)
    except FileNotFoundError:
        gamelib.say("Error al cargar el archvivo 'teclas.txt'")
        return

    nivel_actual = None

    while gamelib.is_alive():

        # Actualizar el Nivel actual mediante un menu
        if not nivel_actual:
            seleccion = menu.seleccionar_nivel(niveles)

            if not seleccion:
                return

            nivel_actual = seleccion

            tablero = soko.crear_grilla(niveles[nivel_actual])
            cant_columnas, cant_filas,  = soko.dimensiones(tablero)
            gamelib.resize(ANCHO_CELDA * cant_columnas,
                           ALTO_CELDA * cant_filas)
            gamelib.title(f'Sokoban - Nivel {nivel_actual}')

        actualizar_ventana_tablero(tablero)

        if soko.juego_ganado(tablero):
            gamelib.say(f"Victoria nivel {nivel_actual}")

            if nivel_actual == len(niveles):
                gamelib.say(f"Juego terminado")
                nivel_actual = None
                continue

            nivel_actual += 1
            tablero = soko.crear_grilla(niveles[nivel_actual])
            cant_columnas, cant_filas,  = soko.dimensiones(tablero)
            gamelib.resize(ANCHO_CELDA * cant_columnas,
                           ALTO_CELDA * cant_filas)
            gamelib.title(f'Sokoban - Nivel {nivel_actual}')
            continue

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        # Actualizar el estado del juego, según la `tecla` presionada

        if tecla not in teclas:
            continue

        if teclas[tecla] == SALIR:
            nivel_actual = None
            continue

        if teclas[tecla] in DIRECCIONES_MOVIMIENTO:
            tablero = soko.mover(
                tablero, DIRECCIONES_MOVIMIENTO[teclas[tecla]])

        if teclas[tecla] == REINICIAR:
            tablero = soko.crear_grilla(niveles[nivel_actual])


gamelib.init(main)
