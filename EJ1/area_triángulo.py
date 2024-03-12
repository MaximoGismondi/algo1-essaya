from norma import norma
from prodvectorial import producto_vectorial
from diferencia import diferencia


def area_triangulo(punto1, punto2, punto3):
    """Recibe las coordenadas de los 3 puntos que forman el triangulo
        en forma de 3 tuplas de cordenadas de R3 y devuelve el 
        area del triángulo formado por estos 3 puntos."""

    punto1_x, punto1_y, punto1_z = punto1
    punto2_x, punto2_y, punto2_z = punto2
    punto3_x, punto3_y, punto3_z = punto3

    vector_punto1_punto2 = diferencia(
        punto1_x, punto1_y, punto1_z, punto2_x, punto2_y, punto2_z)
    vector_punto1_punto3 = diferencia(
        punto1_x, punto1_y, punto1_z, punto3_x, punto3_y, punto3_z)

    vector_punto1_punto2_x, vector_punto1_punto2_y, vector_punto1_punto2_z = vector_punto1_punto2
    vector_punto1_punto3_x, vector_punto1_punto3_y, vector_punto1_punto3_z = vector_punto1_punto3

    vector_resultante = producto_vectorial(
        vector_punto1_punto2_x, vector_punto1_punto2_y, vector_punto1_punto2_z,
        vector_punto1_punto3_x, vector_punto1_punto3_y, vector_punto1_punto3_z)

    vector_resultante_x, vector_resultante_y, vector_resultante_z = vector_resultante

    area_triangulo = norma(vector_resultante_x,
                           vector_resultante_y, vector_resultante_z) / 2

    return area_triangulo

# Pruebas


assert area_triangulo((0, 0, 0), (0, 0, 1), (0, 1, 0)) == 0.5
assert area_triangulo((-2, 0, 0), (0, 0, 1), (0, 1, 0)) == 1.5
assert area_triangulo((0, 0, -10), (0, 0, 0), (0, -10, 0)) == 50
assert area_triangulo((10, 22, 10), (10, 10, 10), (-22, 10, 10)) == 72
