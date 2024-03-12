import soko
from pila import Pila
DIRECCIONES_MOVIMIENTO = (0, -1), (-1, 0), (0, 1), (1, 0)


def buscar_solucion(estado_inicial):
    '''Busca una solución a un estado dado, devuelve un booleano si encuentra la solución y una Pila en el orden de las acciones a ejecutar para resolver el problema'''
    visitados = set()
    return _backtrack(estado_inicial, visitados)


def _backtrack(estado, visitados):
    '''
    Recibe un estado y todos los estados visitados hasta el momento, agrega el estado a la lista y devuelve un booleano si se posible una solución desde ese punto y
    una pila con la sucesion de acciones para llegar a la misma.
    '''
    visitados.add(_resumir_estado(estado))
    if soko.juego_ganado(estado):
        return True, Pila()

    for direccion in DIRECCIONES_MOVIMIENTO:
        nuevo_estado = soko.mover(estado, direccion)
        if _resumir_estado(nuevo_estado) in visitados:
            continue
        solucion, acciones = _backtrack(nuevo_estado, visitados)
        if solucion:
            acciones.apilar(direccion)
            return True, acciones

    return False, Pila()


def _resumir_estado(estado):
    '''Recibe un estado y devuelve una tupla con las celdas y posiciones de las cajas y del jugador'''
    resumen = []
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if soko.hay_jugador(estado, j, i):
                resumen.append((estado[i][j], j, i))
            if soko.hay_caja(estado, j, i):
                resumen.append((estado[i][j], j, i))
    return tuple(resumen)
