import soko
import backtrack
from pila import Pila


class Juego:
    def __init__(self, nivel_actual=None, grilla=None):
        '''Inicializa una instacia de la clase Juego y opcionalmente recibe actual y grilla'''
        self.nivel_actual = nivel_actual
        self.grilla = grilla
        self.pila_deshacer = Pila()
        self.pila_rehacer = Pila()
        self.pila_pistas = Pila()

    def ejecutar_movimiento(self, direccion):
        '''Ejecuta un movimiento en la direccion recibida por parametro'''
        grilla_anterior = self.grilla
        self.grilla = soko.mover(self.grilla, direccion)

        if self.grilla is grilla_anterior:
            return

        self.pila_deshacer.apilar(grilla_anterior)
        self.pila_rehacer = Pila()

        if self.pila_pistas.esta_vacia():
            return

        pista = self.pila_pistas.desapilar()
        if direccion is pista:
            return

        self.pila_pistas = Pila()

    def deshacer(self):
        '''Deshace el último movimiento si es que lo hay'''
        if not self.pila_deshacer.esta_vacia():
            self.pila_rehacer.apilar(self.grilla)
            self.grilla = self.pila_deshacer.desapilar()
        self.pila_pistas = Pila()

    def rehacer(self):
        '''Rehace el último movimiento si es que deshicimos uno por error'''
        if not self.pila_rehacer.esta_vacia():
            self.pila_deshacer.apilar(self.grilla)
            self.grilla = self.pila_rehacer.desapilar()
        self.pila_pistas = Pila()

    def pista(self):
        '''Calcula y ejecuta una movimiento que permite llegar a la resolución del nivel'''
        if not self.pila_pistas.esta_vacia():
            return self.pila_pistas.ver_tope()

        solucion, self.pila_pistas = backtrack.buscar_solucion(self.grilla)

        if solucion and not self.pila_pistas.esta_vacia():
            return self.pila_pistas.ver_tope()
