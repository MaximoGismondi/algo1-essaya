# ejercicios parcial 2
def contar_respuestas_a(msgs, usuario_destino):
    ids_msg_roman = []
    rtas_usr = {}
    for id, msg in msgs.items():
        if msg['de'] == usuario_destino:
            ids_msg_roman.append(id)

    for msg in msgs.values():
        if msg['respuesta_a_id'] in ids_msg_roman:
            rtas_usr[msg['de']] = rtas_usr.get(msg['de'], 0) + 1

    return rtas_usr


msgs = {
    1: {
        'de': 'roman',
        'texto': 'hola como estan',
        'respuesta_a_id': 0
    },
    2: {
        'de': 'ale',
        'texto': 'todo tranqui',
        'respuesta_a_id': 1
    },
    3: {
        'de': 'julio',
        'texto': 'todo bien y vos?',
        'respuesta_a_id': 1
    },
    4: {
        'de': 'roman',
        'texto': 'un lujo',
        'respuesta_a_id': 2
    },
    5: {
        'de': 'lucas',
        'texto': 'chill',
        'respuesta_a_id': 1
    },
    6: {
        'de': 'julio',
        'texto': 'god',
        'respuesta_a_id': 4
    }
}

# print(contar_respuestas_a(msgs, 'roman'))


def traducir_a_ingles(texto, dic):
    return " ".join([dic_es_en.get(palabra, palabra) for palabra in texto.split()])


dic_es_en = {
    "hola": 'hi',
    'como': 'how',
    'estas': 'are',
    'vos': 'you',
}

# print(traducir_a_ingles('hola como estas vos ?', dic_es_en))


def ventas_por_local(vendedores, locales):
    ventas_locales = {}
    for local, vendedores_local in locales.items():
        for vendedor in vendedores_local:
            ventas_locales[local] = ventas_locales.get(
                local, 0) + vendedores[vendedor]

    return ventas_locales


vendedores = {'delportro': 2,
              'juan': 4,
              'martin': 0,
              }
locales = {'waltmart': ['delportro', 'martin', 'juan'],
           'mc': ['martin', 'juan'],
           'burguer': ['delportro', 'martin']}

# print(ventas_por_local(vendedores, locales))


class Angulo:
    def __init__(self, grado, minuto, segundo):

        if segundo < 0 or minuto < 0 or grado < 0:
            raise ValueError("Angulo invalido")

        self.grado = grado
        self.minuto = minuto
        self.segundo = segundo

        while self.segundo >= 60:
            self.segundo -= 60
            self.minuto += 1

        while self.minuto >= 60:
            self.minuto -= 60
            self.grado += 1

    def sumar_segundos(self, segundos):

        if segundos < 0:
            raise ValueError("No se pueden restar segundos")

        nuevo_angulo = self + Angulo(0, 0, segundos)
        self.grado = nuevo_angulo.grado
        self.minuto = nuevo_angulo.minuto
        self.segundo = nuevo_angulo.segundo

    def diferencia_en_segundos(self, otro):
        diferencia = 0
        diferencia += (self.grado - otro.grado) * 3600
        diferencia += (self.minuto - otro.minuto) * 60
        diferencia += self.segundo - otro.segundo
        return abs(diferencia)
        # return diferencia

    def __add__(self, otro):
        segundo = self.segundo + otro.segundo
        minuto = self.minuto + otro.minuto
        angulo = self.grado + otro.grado

        return Angulo(angulo, minuto, segundo)

    def __str__(self):
        return f"{self.grado}° {self.minuto}' {self.segundo}''"


a1 = Angulo(365, 61, 1)
# a1.sumar_segundos(-3)
a1 = Angulo(365, 7, 43)
a2 = Angulo(367, 9, 20)
print(a1)
print(a1.diferencia_en_segundos(a2))
a1.sumar_segundos(3630)
print(a2.diferencia_en_segundos(a1))
print(a1)
