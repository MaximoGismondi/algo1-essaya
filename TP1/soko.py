PARED = '#'
CAJA = '$'
JUGADOR = '@'
OBJETIVO = '.'
OBJETIVO_CAJA = '*'
OBJETIVO_JUGADOR = '+'
VACIO = ' '


def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador

    Ejemplo:

    >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ])
    '''

    grilla = []

    for i in range(len(desc)):
        grilla.append([])
        for j in range(len(desc[i])):
            grilla[i].append(desc[i][j])

    return grilla


def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    return len(grilla[0]), len(grilla)


def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == PARED


def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    objetivos = OBJETIVO, OBJETIVO_CAJA, OBJETIVO_JUGADOR
    return grilla[f][c] in objetivos


def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    cajas = CAJA, OBJETIVO_CAJA
    return grilla[f][c] in cajas


def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    jugadores = JUGADOR, OBJETIVO_JUGADOR
    return grilla[f][c] in jugadores


def esta_libre(grilla, c, f):
    '''Devuelve True si hay vacio en la columna y fila (c, f).'''
    vacio = VACIO, OBJETIVO
    return grilla[f][c] in vacio


def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''

    objetivo_incumplido = OBJETIVO, OBJETIVO_JUGADOR

    for fila in grilla:
        for celda in fila:
            if celda in objetivo_incumplido:
                return False

    return True


def posicion_jugador(grilla):
    '''Devuelve una tupla con la posicion actual del jugador, en caso de no encontrarlo devuelve la tupla (-1,-1)'''
    for f in range(len(grilla)):
        for c in range(len(grilla[f])):
            if hay_jugador(grilla, c, f):
                return c, f

    return -1, -1


def movimiento_valido(grilla, direccion):
    '''Devuelve True si el movimiento a efectuar es valido'''
    c_jugador, f_jugador = posicion_jugador(grilla)

    c_deseada = c_jugador + direccion[0]
    f_deseada = f_jugador + direccion[1]

    if hay_pared(grilla, c_deseada, f_deseada):
        return False

    if not hay_caja(grilla, c_deseada, f_deseada):
        return True

    c_deseada_caja = c_deseada + direccion[0]
    f_deseada_caja = f_deseada + direccion[1]

    return esta_libre(grilla, c_deseada_caja, f_deseada_caja)


def ejecutar_movimiento(grilla, direccion):
    '''Devuelve una grilla nueva y si el movimiento es valido, ejecuta el movimiento'''

    grilla_movida = [fila[:] for fila in grilla[:]]
    c_jugador, f_jugador = posicion_jugador(grilla)

    if hay_objetivo(grilla, c_jugador, f_jugador):
        grilla_movida[f_jugador][c_jugador] = OBJETIVO
    else:
        grilla_movida[f_jugador][c_jugador] = VACIO

    nueva_c_jugador = c_jugador + direccion[0]
    nueva_f_jugador = f_jugador + direccion[1]

    if hay_objetivo(grilla, nueva_c_jugador, nueva_f_jugador):
        grilla_movida[nueva_f_jugador][nueva_c_jugador] = OBJETIVO_JUGADOR
    else:
        grilla_movida[nueva_f_jugador][nueva_c_jugador] = JUGADOR

    if not hay_caja(grilla, nueva_c_jugador, nueva_f_jugador):
        return grilla_movida

    nueva_c_caja = nueva_c_jugador + direccion[0]
    nueva_f_caja = nueva_f_jugador + direccion[1]

    if hay_objetivo(grilla, nueva_c_caja, nueva_f_caja):
        grilla_movida[nueva_f_caja][nueva_c_caja] = OBJETIVO_CAJA
    else:
        grilla_movida[nueva_f_caja][nueva_c_caja] = CAJA

    return grilla_movida


def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''

    if movimiento_valido(grilla, direccion):
        return ejecutar_movimiento(grilla, direccion)

    return grilla
