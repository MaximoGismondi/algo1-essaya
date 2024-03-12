def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z


# Agregar pruebas
a1x, a1y, a1z = (16, -72, -52)
b1x, b1y, b1z = (55, 90, -31)

a2x, a2y, a2z = (55, -88, -75)
b2x, b2y, b2z = (38, 62, -12)

assert diferencia(a1x, a1y, a1z, b1x, b1y, b1z) == (-39, -162, -21)
assert diferencia(a2x, a2y, a2z, b2x, b2y, b2z) == (17, -150, -63)

assert diferencia(1, 2, 3, 1, 2, 3) == (0, 0, 0)
