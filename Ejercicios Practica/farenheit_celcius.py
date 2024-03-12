def farenheit_a_celcius(farenheit):
    """ Esta funcion recibe grados farenheit y devuelve grados celcius """
    celcius = (farenheit - 32) * (5 / 9)
    return celcius


def mostrar_tabla_farenheit_a_celcius():
    """ 
        Mostrar de 10 en 10 Farenheit a Celcius 
        de 0 a 120
    """
    for farenheit in range(0, 121, 10):
        celcius = farenheit_a_celcius(farenheit)
        print("Farenheit: ", farenheit, " -> Calcius: ", celcius)


mostrar_tabla_farenheit_a_celcius()
