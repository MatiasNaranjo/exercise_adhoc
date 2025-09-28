lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas):
    """El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""

    # Creo la lista de edades
    lista_edad = [persona[3] for persona in lista_personas]
    # Cantidad de elementos en la lista
    n = len(lista_edad)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparo elementos cpsecutivos
            if lista_edad[j] > lista_edad[j + 1]:
                # Si el primero es mayor, los intercambio
                lista_edad[j], lista_edad[j + 1] = lista_edad[j + 1], lista_edad[j]
    return lista_edad

    # Se crea una lista que contiene el elemento de la edad (índice 3) de cada tupla en lista_personas
    # Luego, se utiliza la función sorted() para ordenar la lista de edades de menor a mayor y se devuelve el resultado.
    # return sorted([persona[3] for persona in lista_personas])


def convertir_a_diccionario(lista_personas):
    """Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad"""

    # Creo un diccionario vacío
    personas_dict = {}

    for persona in lista_personas:
        # Se toma el primer elemento de la tupla (dni) como clave
        dni = persona[0]

        # El resto de los elementos (nombre, apellido, edad) como valor en forma de tupla.
        nombre = persona[1]
        apellido = persona[2]
        edad = persona[3]

        # Se almacena una tupla con (nombre, apellido, edad) en el diccionario
        personas_dict[dni] = (nombre, apellido, edad)

    return personas_dict
    # Se toma el primer elemento de cada tupla (dni) como clave
    # el resto de los elementos (nombre, apellido, edad) como valor en forma de tupla.
    # return {persona[0]: persona[1:] for persona in lista_personas}


def devolver_edad(lista_personas, dni):
    """Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    # Utiliza el método convertir_a_diccionario para obtener un diccionario de personas
    lista_personas_dict = convertir_a_diccionario(lista_personas)

    # Verifica si el dni existe en el diccionario y se devuelve la edad (índice 2 del valor tupla)
    if dni in lista_personas_dict:
        # Devuelve la edad de la persona con el dni especificado
        return lista_personas_dict[dni][2]


def eliminar_repetidos(lista_personas):
    """El metodo debe devolver los elementos unicos"""

    # Creamos un conjunto vacío para llevar registro de las personas ya vistas
    set_vistos = set()

    # Lista donde vamos a guardar solo personas únicas (sin duplicados)
    lista_unicos = []

    # Recorremos la lista original
    for persona in lista_personas:
        # Si esta persona aún no fue agregada (no está en el conjunto)
        if persona not in set_vistos:
            # La agregamos a la lista de únicos
            lista_unicos.append(persona)
            # Y marcamos que ya fue vista agregándola al conjunto
            set_vistos.add(persona)

    # Devolvemos la lista sin duplicados y en el mismo orden original
    return lista_unicos

    # Convierte la lista a un conjunto para eliminar duplicados
    # return list(set(lista_personas))


def separar_por_edad(lista_personas):
    """Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    # Se inician dos listas vacías
    lista_mayores = []
    lista_menores = []

    for persona in lista_personas:
        # Accede al cuarto elemento de la tupla (índice 3), que representa la edad
        if persona[3] >= 25:
            # Si la edad es mayor o igual a 25, se agrega la persona a la lista de mayores
            lista_mayores.append(persona)
        else:
            # Si la edad es menor a 25, se agrega la persona a la lista de menores
            lista_menores.append(persona)
    return lista_mayores, lista_menores


def obtener_promedio(lista):
    """Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    try:
        # Intenta hacer la división para calcular el promedio
        lista_prom = sum(lista) / len(lista)
        return lista_prom

    except ZeroDivisionError:
        # Si ocurre una división por cero, se ejecuta la excepción de división por cero
        return 0


def main():
    """Este metodo no debe modificarse y es solo a fines de probar el codigo"""
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))


if __name__ == "__main__":
    main()
