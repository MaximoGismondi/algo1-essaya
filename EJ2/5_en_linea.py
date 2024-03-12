import gamelib

OFFSET_TITULO = 40

ANCHO_VENTANA = 300
ALTO_VENTANA = 300

FILAS = 10
COLUMNAS = 10

VACIO = ' '
JUGADORES = ['O', 'X']


def juego_crear():
    """Inicializar el estado del juego"""
    juego = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]

    return juego


# Lógica

def corresponde_a_celda(x, y):
    return x > 0 and x < ANCHO_VENTANA and y < ALTO_VENTANA + OFFSET_TITULO and y > OFFSET_TITULO


def posicion_celda_por_coordenadas(x, y):
    return x // (ANCHO_VENTANA//FILAS), (y - OFFSET_TITULO) // (ALTO_VENTANA//COLUMNAS)


def validar_click(juego, x, y):
    '''Valida que el click este en el rango y que no sea sobre una celda ya usada
    '''
    if not corresponde_a_celda(x, y):
        print("Fuera de rango")
        return False

    f_cursor, c_cursor = posicion_celda_por_coordenadas(x, y)

    if juego[f_cursor][c_cursor] != VACIO:
        print("Celda ya ocupada")
        return False

    return True


def cambiar_turno(turno):
    '''Cambia el turno de 1 a 0 y viceversa'''

    if turno == 1:
        return 0
    return 1


def juego_actualizar(juego, x, y, turno):
    '''Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve junto con el nuevo turno turno.
    '''

    juego_actualizado = [fila for fila in juego[:]]
    f_cursor, c_cursor = posicion_celda_por_coordenadas(x, y)

    juego_actualizado[f_cursor][c_cursor] = JUGADORES[turno]

    return juego_actualizado


# Interfaz

def juego_mostrar(juego, turno):
    '''Actualizar la ventana'''

    gamelib.draw_text(f'5 en línea - Turno: {JUGADORES[turno]}', 150, 20)

    for f in range(1, FILAS):
        x = f * (ANCHO_VENTANA/FILAS)
        gamelib.draw_line(x, OFFSET_TITULO, x, ALTO_VENTANA + OFFSET_TITULO)

    for c in range(1, COLUMNAS):
        y = c * (ALTO_VENTANA/COLUMNAS) + OFFSET_TITULO
        gamelib.draw_line(0, y, ANCHO_VENTANA, y)

    for f in range(FILAS):
        for c in range(COLUMNAS):
            x = (f + 0.5) * (ANCHO_VENTANA/FILAS)
            y = (c + 0.5) * (ALTO_VENTANA/COLUMNAS) + OFFSET_TITULO
            gamelib.draw_text(juego[f][c], x, y)


def main():
    juego = juego_crear()
    turno = 0

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA + OFFSET_TITULO)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():

        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego, turno)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click

            if validar_click(juego, x, y):
                juego = juego_actualizar(juego, x, y, turno)
                turno = cambiar_turno(turno)


gamelib.init(main)
