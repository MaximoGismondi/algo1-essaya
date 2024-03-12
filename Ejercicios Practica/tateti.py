JUGADORES = ['O', 'X']
TAMANO = 3


def crear_tablero():
    tablero = []
    for fila in range(TAMANO):
        tablero.append([])
        for _ in range(TAMANO):
            tablero[fila].append(' ')

    return tablero


def pedir_posicion(jugador):
    print()
    fila = int(input(f"Jugador {jugador + 1} ingrese la fila: "))
    columna = int(input(f"Jugador {jugador + 1} ingrese la columna: "))
    print()

    return (fila-1, columna-1)


def validar_posicion(tablero, posicion):
    if posicion[0] < 0 or posicion[0] >= TAMANO:
        return False

    if posicion[1] < 0 or posicion[1] >= TAMANO:
        return False

    if tablero[posicion[0]][posicion[1]] != ' ':
        return False

    return True


def actualizar_tablero(tablero, jugador, posicion):
    tablero[posicion[0]][posicion[1]] = JUGADORES[jugador]


def cambiar_jugador_actual(jugador_actual):
    if jugador_actual == 0:
        return 1
    return 0


def mostrar_tablero(tablero):
    for fila in range(TAMANO):
        for columna in range(TAMANO):
            if columna < 2:
                print(tablero[fila][columna], end=" | ")
            else:
                print(tablero[fila][columna])
        if fila < 2:
            print('----------')


def comprobar_victoria(tablero, jugador):
    for fila in range(TAMANO):
        for columna in range(TAMANO):
            if tablero[fila][columna] != JUGADORES[jugador]:
                break
        else:
            return True

    for columna in range(TAMANO):
        for fila in range(TAMANO):
            if tablero[fila][columna] != JUGADORES[jugador]:
                break
        else:
            return True

    for diagonal in range(TAMANO):
        if tablero[diagonal][diagonal] != JUGADORES[jugador]:
            break
    else:
        return True

    for diagonal in range(TAMANO):
        if tablero[diagonal][TAMANO - 1 - diagonal] != JUGADORES[jugador]:
            break
    else:
        return True

    return False


def tablero_lleno(tablero):
    for fila in range(TAMANO):
        for columna in range(TAMANO):
            if tablero[fila][columna] == ' ':
                return False

    return True


def main():
    tablero = crear_tablero()
    jugador_actual = 1
    termino = False

    mostrar_tablero(tablero)

    while not termino:  # terminar
        jugador_actual = cambiar_jugador_actual(jugador_actual)
        posicion_a_colocar = pedir_posicion(jugador_actual)

        while validar_posicion(tablero, posicion_a_colocar) == False:
            print('Posicion Invalida')
            posicion_a_colocar = pedir_posicion(jugador_actual)

        actualizar_tablero(tablero, jugador_actual, posicion_a_colocar)
        mostrar_tablero(tablero)

        termino = comprobar_victoria(
            tablero, jugador_actual) or tablero_lleno(tablero)

    if comprobar_victoria(tablero, jugador_actual):
        print()
        print(f"Gano el jugador {jugador_actual + 1}")

    elif tablero_lleno(tablero):
        print()
        print("Tablero lleno")


main()
