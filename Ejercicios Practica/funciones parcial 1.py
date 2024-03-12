def invertir_lista(lista):
    for i in range(len(lista) // 2):
        lista[i], lista[len(lista) - 1 -
                        i] = lista[len(lista) - 1 - i], lista[i]
    return lista


assert invertir_lista([1, 2, 3]) == [3, 2, 1]
assert invertir_lista([1, 2, 3, 4]) == [4, 3, 2, 1]


def pedir_texto():
    t = input()
    l = []

    while t != '':
        l.append(t)
        t = input()

    return "".join(sorted(l))


# print(pedir_texto())

def invertir_palabras_cadena(cadena):
    palabras = cadena.split(" ")

    for i in range(len(palabras)):
        palabras[i] = palabras[i][::-1]

    return " ".join(palabras)


assert invertir_palabras_cadena("Qué día tan bonito") == "éuQ aíd nat otinob"


def diferencia_listas(l1, l2):
    return [x for x in l1 if x not in l2]


assert diferencia_listas([2, 3, 1, 5], [2, 5]) == [3, 1]
assert diferencia_listas([15, 49], [6, 31]) == [15, 49]


def lista_super():
    cant = 0
    lista = input("Ingrese el mensaje: ").split(" ")
    [print(f"{lista[i+1]} - {lista[i]}") for i in range(len(lista))
     if lista[i].isdigit()]
    cant = len([i for i in range(len(lista)) if lista[i].isdigit()])
    while cant == 0:
        print("No se encontraron productos!")
        lista = input("Ingrese el mensaje: ").split(" ")
        [print(f"{lista[i+1]} - {lista[i]}")
         for i in range(len(lista)) if lista[i].isdigit()]
        cant = len([i for i in range(len(lista)) if lista[i].isdigit()])

    print(f"Total de productos: {cant}")


# lista_super()

def obtener_bigramas(frase):
    palabras = frase.split(" ")
    biagramas = []
    for i in range(len(palabras) - 1):
        biagramas.append((palabras[i], palabras[i+1]))
    return biagramas


# print(obtener_bigramas("Hola"))

# frecuencia = int(input("Ingrese una frecuencia: "))
# frase = input("Ingrese una frase: ")
# respuesta = ''

# for i in range(0, len(frase), frecuencia):
#     for j in range(frecuencia):
#         if i + j < len(frase):
#             respuesta += frase[i + j]

#     if i + frecuencia < len(frase):
#         respuesta += '-'

# print(respuesta)

a = ''
b = ''

while not a.isdigit() or int(a) <= 0:
    a = input("Ingrese el número 'a': ")

while not b.isdigit() or int(b) <= 0:
    b = input("Ingrese el número 'b': ")

a = int(a)
b = int(b)

[print(b * (i+1)) for i in range(a)]
