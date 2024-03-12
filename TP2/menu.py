import gamelib

ANCHO_FONDO = 640
ALTO_FONDO = 320

ANCHO_BOTON = 120
ALTO_BOTON = 60

X_JUGAR, Y_JUGAR = 60, 150
KEY_JUGAR = 'jugar'

X_SEL, Y_SEL = 460, 150
KEY_SELECCIONAR = 'seleccionar'


def mostrar_menu():
    '''Muestra un menu interactivo con el usuario'''
    gamelib.resize(ANCHO_FONDO, ALTO_FONDO)
    gamelib.title(f'Sokoban - Menu')
    gamelib.draw_begin()
    # Fondo
    gamelib.draw_image('img/background.gif', 0, 0)

    # Play
    gamelib.draw_rectangle(X_JUGAR, Y_JUGAR, X_JUGAR +
                           ANCHO_BOTON, Y_JUGAR + ALTO_BOTON, fill='white',  activefill='lightgreen')
    gamelib.draw_text('Jugar', X_JUGAR + ANCHO_BOTON // 2,
                      Y_JUGAR + ALTO_BOTON // 2, fill="black", state='disabled')

    # Seleccionar Nivel
    gamelib.draw_rectangle(X_SEL, Y_SEL, X_SEL + ANCHO_BOTON,
                           Y_SEL + ALTO_BOTON, fill='white',  activefill='lightblue')
    gamelib.draw_text('Seleccionar\nNivel', X_SEL + ANCHO_BOTON // 2,
                      Y_SEL + ALTO_BOTON // 2, fill="black", justify='center', state='disabled')

    gamelib.draw_end()


def mostrar_menu():
    '''Muestra un menu interactivo con el usuario'''
    gamelib.resize(ANCHO_FONDO, ALTO_FONDO)
    gamelib.title(f'Sokoban - Menu')

    gamelib.draw_begin()

    # Fondo
    gamelib.draw_image('img/background.gif', 0, 0)

    # Play
    gamelib.draw_rectangle(X_JUGAR, Y_JUGAR, X_JUGAR +
                           ANCHO_BOTON, Y_JUGAR + ALTO_BOTON, fill='white',  activefill='lightgreen')
    gamelib.draw_text('Jugar', X_JUGAR + ANCHO_BOTON // 2,
                      Y_JUGAR + ALTO_BOTON // 2, fill="black", state='disabled')

    # Seleccionar Nivel
    gamelib.draw_rectangle(X_SEL, Y_SEL, X_SEL + ANCHO_BOTON,
                           Y_SEL + ALTO_BOTON, fill='white',  activefill='lightblue')
    gamelib.draw_text('Seleccionar\nNivel', X_SEL + ANCHO_BOTON // 2,
                      Y_SEL + ALTO_BOTON // 2, fill="black", justify='center', state='disabled')

    gamelib.draw_end()


# Interaccion
def pedir_nivel(niveles):
    '''Recibe la lista de niveles, y devuelve el nivel seleccionado por el usuario o None en caso contrario'''
    while gamelib.is_alive():
        entrada = gamelib.input(
            f'Elija el Nivel ( {min(niveles)} - {max(niveles)} )')

        if not entrada:
            return

        if not entrada.isdigit():
            gamelib.say('Escriba el NUMERO del nivel')
            continue

        if int(entrada) not in niveles:
            gamelib.say('El nivel no esta en la lista')
            continue

        return int(entrada)


def opcion_menu():
    '''Muestra el menu y espera a que una opción sea seleccionada o devuelve None si el menu se cierra'''
    mostrar_menu()
    while gamelib.is_alive():
        ev = gamelib.wait()
        if not ev:
            return

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            return

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click

            if x >= X_JUGAR and x <= X_JUGAR + ANCHO_BOTON and y >= Y_JUGAR and y <= Y_JUGAR + ALTO_BOTON:
                return KEY_JUGAR

            if x >= X_SEL and x <= X_SEL + ANCHO_BOTON and y >= Y_SEL and y <= Y_SEL + ALTO_BOTON:
                return KEY_SELECCIONAR


def seleccionar_nivel(niveles):
    '''Recibe la lista de niveles y devuelve el numero del nivel a jugar o None si ce cierra'''
    nivel_actual = None
    while not nivel_actual:
        opcion = opcion_menu()

        if not opcion:
            return

        if opcion == KEY_JUGAR:
            nivel_actual = min(niveles.keys())

        elif opcion == KEY_SELECCIONAR:
            nivel_actual = pedir_nivel(niveles.keys())

    return nivel_actual
