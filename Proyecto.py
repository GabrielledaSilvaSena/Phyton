# PROYECTO LOGICA: Katas de Python
# ============================================
from functools import reduce
import math  # Lo necesito para el ejercicio 40 del circulo

# ============================================
# EJERCICIO 1
# Escribe una funcion que reciba una cadena de texto como parametro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
# ============================================

def frecuencia_letras(texto):
    # Creamos un diccionario vacio
    frecuencias = {}
    
    # Recorremos cada letra del texto
    for letra in texto:
        # Si NO es un espacio, la contamos
        if letra != ' ':
            # Si la letra ya esta en el diccionario, le sumamos 1
            if letra in frecuencias:
                frecuencias[letra] = frecuencias[letra] + 1
            # Si no esta, la agregamos con valor 1
            else:
                frecuencias[letra] = 1
    
    return frecuencias

# Prueba del ejercicio 1
print("EJERCICIO 1: Frecuencia de letras")
print("-" * 40)
resultado1 = frecuencia_letras("ROSAS ROJAS")
print("Texto: ROSAS ROJAS")
print("Resultado:", resultado1)
print("")


# ============================================
# EJERCICIO 2
# Dada una lista de numeros, obten una nueva lista con el doble de cada valor.
# Usa la funcion map()
# ============================================

def doblar_numero(numero):
    return numero * 2

def obtener_dobles(lista_numeros):
    lista_dobles = list(map(doblar_numero, lista_numeros))
    return lista_dobles

# Prueba del ejercicio 2
print("EJERCICIO 2: Duplicar numeros con map()")
print("-" * 40)
numeros = [2, 0, 1, 9, 58]
resultado2 = obtener_dobles(numeros)
print("Lista original:", numeros)
print("Lista duplicada:", resultado2)
print("")


# ============================================
# EJERCICIO 3
# Escribe una funcion que tome una lista de palabras y una palabra objetivo
# como parametros. La funcion debe devolver una lista con todas las palabras
# de la lista original que contengan la palabra objetivo.
# ============================================

def filtrar_palabras(lista_palabras, palabra_objetivo):
    palabras_encontradas = []
    
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            palabras_encontradas.append(palabra)
    
    return palabras_encontradas

# Prueba del ejercicio 3
print("EJERCICIO 3: Filtrar palabras")
print("-" * 40)
palabras = ["manzana", "pera", "mango", "banana", "mandarina"]
buscar = "man"
resultado3 = filtrar_palabras(palabras, buscar)
print("Lista completa:", palabras)
print("Buscamos:", buscar)
print("Encontradas:", resultado3)
print("")


# ============================================
# EJERCICIO 4
# Genera una funcion que calcule la diferencia entre los valores de dos listas.
# Usa la funcion map()
# ============================================

def calcular_diferencia(num1, num2):
    return num1 - num2

def diferencia_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")
    return list(map(calcular_diferencia, lista1, lista2))

# Prueba del ejercicio 4
print("EJERCICIO 4: Diferencia entre dos listas")
print("-" * 40)
lista_a = [10, 20, 30, 40]
lista_b = [5, 10, 15, 20]
resultado4 = diferencia_listas(lista_a, lista_b)
print("Lista 1:", lista_a)
print("Lista 2:", lista_b)
print("Diferencias:", resultado4)
print("")


# ============================================
# EJERCICIO 5
# Escribe una funcion que tome una lista de numeros como parametro y un valor
# opcional nota_aprobado, que por defecto es 5. La funcion debe calcular la
# media de los numeros en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es asi, el estado sera "aprobado", de lo contrario,
# sera "suspenso". La funcion debe devolver una tupla que contenga la media
# y el estado.
# ============================================

def calcular_media_estado(lista_notas, nota_aprobado=5):
    # Sumamos todas las notas
    suma_notas = 0
    for nota in lista_notas:
        suma_notas = suma_notas + nota
    
    # Calculamos el promedio
    media = suma_notas / len(lista_notas)
    
    # Verificamos si aprueba o no
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

# Prueba del ejercicio 5
print("EJERCICIO 5: Calcular media y estado")
print("-" * 40)
notas = [6, 9, 8, 5, 2]
resultado5 = calcular_media_estado(notas)
print("Notas:", notas)
print("Promedio:", resultado5[0])
print("Estado:", resultado5[1])
print("")

# ============================================
# EJERCICIO 6
# Escribe una funcion que calcule el factorial de un numero de manera recursiva.

def calcular_factorial(numero):
    # Si el numero es 0 o 1, el factorial es 1 (caso base)
    if numero == 0 or numero == 1:
        return 1
    else:
        # Si no, multiplicamos el numero por el factorial del numero anterior
        # Esto se llama recursion porque la funcion se llama a si misma
        return numero * calcular_factorial(numero - 1)

# Prueba del ejercicio 6
print("=== EJERCICIO 6: Factorial ===")
resultado = calcular_factorial(5)
print(f"El factorial de 5 es: {resultado}")  # 5! = 5 x 4 x 3 x 2 x 1 = 120
print()


# ============================================
# EJERCICIO 7
# Genera una funcion que convierta una lista de tuplas a una lista de strings. Usa la funcion map()
# ============================================

def tuplas_a_strings(lista_tuplas):
    # Usamos map() para convertir cada tupla en un string
    # str() convierte cualquier cosa en texto
    resultado = list(map(str, lista_tuplas))
    return resultado

# Prueba del ejercicio 7
print("=== EJERCICIO 7: Tuplas a Strings ===")
tuplas = [(1, 2), (3, 4), (5, 6)]
print(f"Lista original de tuplas: {tuplas}")
strings = tuplas_a_strings(tuplas)
print(f"Lista convertida a strings: {strings}")
print()


# ============================================
# EJERCICIO 8
# Escribe un programa que pida al usuario dos numeros e intente dividirlos.
# Si el usuario ingresa un valor no numerico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada.
# ============================================

def dividir_numeros_con_ejemplos(num1, num2):
    # Version con parametros para poder probarla facilmente
    try:
        # Intentamos convertir a numeros
        numero1 = float(num1)
        numero2 = float(num2)
        
        # Intentamos hacer la division
        return numero1 / numero2
        
    except ValueError:
        # Si el valor no es un numero
        raise ValueError("Debes ingresar valores numericos")
        
    except ZeroDivisionError:
        # Si intento dividir por cero
        raise ZeroDivisionError("No se puede dividir por cero")

# Prueba del ejercicio 8
print("=== EJERCICIO 8: Division con manejo de errores ===")

# Caso 1: Division normal (funciona bien)
print("Caso 1: Dividir 10 entre 2")
try:
    resultado = dividir_numeros_con_ejemplos(10, 2)
    print(f"OK - La division fue exitosa: {resultado}")
except (ValueError, ZeroDivisionError) as e:
    print(f"ERROR: {e}")

# Caso 2: Division por cero (error controlado)
print("\nCaso 2: Dividir 10 entre 0")
try:
    resultado = dividir_numeros_con_ejemplos(10, 0)
    print(f"OK - La division fue exitosa: {resultado}")
except (ValueError, ZeroDivisionError) as e:
    print(f"ERROR: {e}")

# Caso 3: Valor no numerico (error controlado)
print("\nCaso 3: Dividir 10 entre 'abc'")
try:
    resultado = dividir_numeros_con_ejemplos(10, "abc")
    print(f"OK - La division fue exitosa: {resultado}")
except (ValueError, ZeroDivisionError) as e:
    print(f"ERROR: {e}")

print()

# ============================================
# ============================================
# EJERCICIO 9
# Escribe una funcion que tome una lista de nombres de mascotas como parametro
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en EspaÃ±a.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]
# Usa la funcion filter()

def filtrar_mascotas_permitidas(lista_mascotas):
    # Lista de mascotas prohibidas en EspaÃ±a
    prohibidas = ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]
    
    # Usamos filter() para quedarnos solo con las mascotas que NO estan prohibidas
    # lambda es una funcion pequeÃ±a que revisa si la mascota NO esta en la lista de prohibidas
    mascotas_permitidas = list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))
    
    return mascotas_permitidas

# Prueba del ejercicio 9
print("=== EJERCICIO 9: Filtrar mascotas prohibidas ===")
todas_las_mascotas = ["Perro", "Gato", "Tigre", "Conejo", "Serpiente Piton", "Hamster", "Oso"]
print(f"Lista original: {todas_las_mascotas}")
permitidas = filtrar_mascotas_permitidas(todas_las_mascotas)
print(f"Mascotas permitidas: {permitidas}")
print()


# ============================================
# EJERCICIO 10
# ============================================
# Escribe una funcion que reciba una lista de numeros y calcule su promedio.
# Si la lista esta vacia, lanza una excepcion personalizada y maneja el error adecuadamente.

# Primero creamos nuestra propia excepcion personalizada
class ListaVaciaError(Exception):
    # Esta es una clase que representa un error personalizado
    pass

def calcular_promedio(lista_numeros):
    # Verificamos si la lista esta vacia
    if len(lista_numeros) == 0:
        # Si esta vacia, lanzamos nuestro error personalizado
        raise ListaVaciaError("Error: La lista esta vacia, no se puede calcular el promedio")
    
    # Si no esta vacia, calculamos el promedio
    suma = sum(lista_numeros)  # Sumamos todos los numeros
    promedio = suma / len(lista_numeros)  # Dividimos entre la cantidad de numeros
    
    return promedio

# Prueba del ejercicio 10
print("=== EJERCICIO 10: Promedio con excepcion personalizada ===")

# Caso 1: Lista con numeros (funciona bien)
numeros = [8, 7, 9, 6, 10]
try:
    resultado = calcular_promedio(numeros)
    print(f"El promedio de {numeros} es: {resultado}")
except ListaVaciaError as error:
    print(error)

# Caso 2: Lista vacia (lanza el error)
lista_vacia = []
try:
    resultado = calcular_promedio(lista_vacia)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as error:
    print(error)

print()

# ============================================
# EJERCICIO 11: Escribe un programa que pida al usuario que introduzca su edad. Si el usuario 
# ingresa un valor no numerico o un valor fuera del rango esperado (por ejemplo, menor que 0 o 
# mayor que 120), maneja las excepciones adecuadamente.
# ============================================

def validar_edad():
    # Esta funcion le pide al usuario su edad y verifica que sea valida
    try:
        # Pedimos al usuario que escriba su edad
        edad = input("Por favor, introduce tu edad: ")
        
        # Intentamos convertir lo que escribio el usuario a un numero entero
        edad_numerica = int(edad)
        
        # Verificamos que la edad este en un rango razonable (0 a 120 aÃ±os)
        if edad_numerica < 0:
            print("Error: La edad no puede ser negativa")
        elif edad_numerica > 120:
            print("Error: La edad no puede ser mayor a 120 aÃ±os")
        else:
            # Si todo esta bien, mostramos la edad
            print(f"Tu edad es: {edad_numerica} aÃ±os")
    
    except ValueError:
        # Si el usuario escribio algo que no es un numero, mostramos este error
        print("Error: Debes introducir un numero valido")

# Probamos la funcion
print("=== Ejercicio 11: Validar edad ===")
validar_edad()
print()


# ============================================
# EJERCICIO 12: Genera una funcion que al recibir una frase devuelva una lista con la longitud 
# de cada palabra. Usa la funcion map()
# ============================================

def longitud_palabras(frase):
    # Esta funcion cuenta cuantas letras tiene cada palabra de una frase
    
    # Separamos la frase en palabras
    palabras = frase.split()
    
    # Creo una lista vacia para guardar las longitudes
    longitudes = []
    
    # Recorro cada palabra y cuento sus letras
    for palabra in palabras:
        longitudes.append(len(palabra))
    
    return longitudes

# Probamos la funcion
print("=== Ejercicio 12: Longitud de palabras ===")
frase_ejemplo = "Hola me llamo Gabi y estudio analisis de datos"
resultado = longitud_palabras(frase_ejemplo)
print(f"Frase: {frase_ejemplo}")
print(f"Longitudes: {resultado}")
print()


# ============================================
# EJERCICIO 13: Genera una funcion la cual, para un conjunto de caracteres, devuelva una lista 
# de tuplas con cada letra en mayusculas y minusculas. Las letras no pueden estar repetidas.
# Usa la funcion map()
# ============================================

def mayusculas_minusculas(caracteres):
    # Esta funcion toma letras y devuelve tuplas con version mayuscula y minuscula
    
    # Primero eliminamos las letras repetidas usando set()
    # set() crea un conjunto sin duplicados
    letras_unicas = set(caracteres)
    
    # Usamos map() para crear una tupla (mayuscula, minuscula) para cada letra
    # lambda es una funcion pequeÃ±a que se escribe en una linea
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))
    
    return resultado

# Probamos la funcion
print("=== Ejercicio 13: Mayusculas y minusculas ===")
caracteres_ejemplo = "aabbccdefgh"
resultado = mayusculas_minusculas(caracteres_ejemplo)
print(f"Caracteres originales: {caracteres_ejemplo}")
print(f"Tuplas (mayuscula, minuscula): {resultado}")
print()


# ============================================
# EJERCICIO 14: Crea una funcion que retorne las palabras de una lista de palabras que comience 
# con una letra en especifico. Usa la funcion filter()
# ============================================

def palabras_con_letra(lista_palabras, letra_inicial):
    # Esta funcion filtra palabras que empiezan con una letra especifica
    
    # Usamos filter() para quedarnos solo con las palabras que empiezan con la letra que queremos
    # lambda verifica si la primera letra de cada palabra coincide con la letra_inicial
    palabras_filtradas = list(filter(lambda palabra: palabra[0].lower() == letra_inicial.lower(), lista_palabras))
    
    return palabras_filtradas

# Probamos la funcion
print("=== Ejercicio 14: Palabras que empiezan con letra especifica ===")
lista_palabras = ["Manzana", "Pera", "Platano", "Mango", "Naranja", "Melon"]
letra = "M"
resultado = palabras_con_letra(lista_palabras, letra)
print(f"Lista de palabras: {lista_palabras}")
print(f"Palabras que empiezan con '{letra}': {resultado}")
print()


# ============================================
# EJERCICIO 15: Crea una funcion lambda que sume 3 a cada numero de una lista dada.
# ============================================

# Una funcion lambda es una funcion pequeÃ±a y anonima que se escribe en una linea
# En este caso, tomamos un numero y le sumamos 3
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Probamos la funcion lambda
print("=== Ejercicio 15: Sumar 3 a cada numero ===")
numeros = [1, 5, 10, 15, 20]
resultado = sumar_tres(numeros)
print(f"Lista original: {numeros}")
print(f"Sumando 3 a cada numero: {resultado}")
print()


# ============================================
# EJERCICIO 16: Escribe una funcion que tome una cadena de texto y un numero entero n como 
# parametros y devuelva una lista de todas las palabras que sean mas largas que n. 
# Usa la funcion filter()
# ============================================

def palabras_mas_largas(texto, n):
    # Esta funcion encuentra palabras que tienen mas letras que el numero n
    
    # Separamos el texto en palabras individuales
    palabras = texto.split()
    
    # Usamos filter() para quedarnos solo con palabras que tienen mas de n letras
    # len(palabra) > n verifica si la palabra es mas larga que n
    palabras_largas = list(filter(lambda palabra: len(palabra) > n, palabras))
    
    return palabras_largas

# Probamos la funcion
print("=== Ejercicio 16: Palabras mas largas que n ===")
texto_ejemplo = "Python es un lenguaje de programacion increible"
n = 5
resultado = palabras_mas_largas(texto_ejemplo, n)
print(f"Texto: {texto_ejemplo}")
print(f"Palabras con mas de {n} letras: {resultado}")
print()


# ============================================
# EJERCICIO 17: Crea una funcion que tome una lista de digitos y devuelva el numero 
# correspondiente. Por ejemplo, [5,7,2] corresponde al numero quinientos setenta y dos (572). 
# Usa la funcion reduce()
# ============================================

def digitos_a_numero(digitos):
    # Esta funcion convierte una lista de digitos en un numero completo
    # Por ejemplo: [5, 7, 2] se convierte en 572
    
    # Convierto cada digito a string y luego los junto
    numero_texto = ""
    for digito in digitos:
        numero_texto = numero_texto + str(digito)
    
    # Convierto el texto final a numero
    numero = int(numero_texto)
    
    return numero

# Probamos la funcion
print("=== Ejercicio 17: Convertir digitos a numero ===")
digitos = [5, 7, 2]
resultado = digitos_a_numero(digitos)
print(f"Lista de digitos: {digitos}")
print(f"Numero formado: {resultado}")
print()


# ============================================
# EJERCICIO 18: Escribe un programa en Python que cree una lista de diccionarios que contenga 
# informacion de estudiantes (nombre, edad, calificacion) y use la funcion filter para extraer 
# a los estudiantes con una calificacion mayor o igual a 90. Usa la funcion filter()
# ============================================

def estudiantes_excelentes(lista_estudiantes):
    # Esta funcion filtra estudiantes que tienen calificacion de 90 o mas
    
    # Usamos filter() para quedarnos solo con estudiantes que tienen calificacion >= 90
    estudiantes_filtrados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))
    
    return estudiantes_filtrados

# Creamos una lista de estudiantes con sus datos
print("=== Ejercicio 18: Estudiantes con calificacion >= 90 ===")
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 85},
    {"nombre": "Maria", "edad": 21, "calificacion": 92},
    {"nombre": "Pedro", "edad": 23, "calificacion": 78},
    {"nombre": "Laura", "edad": 20, "calificacion": 98}
]

# Filtramos los estudiantes excelentes
resultado = estudiantes_excelentes(estudiantes)
print("Estudiantes con calificacion >= 90:")
for estudiante in resultado:
    print(f"  - {estudiante['nombre']}: {estudiante['calificacion']} puntos")
print()


# ============================================
# EJERCICIO 19: Crea una funcion lambda que filtre los numeros impares de una lista dada.
# ============================================

# Una funcion lambda que filtra numeros impares
# Un numero es impar cuando al dividirlo entre 2 NO queda resto
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

# Probamos la funcion lambda
print("=== Ejercicio 19: Filtrar numeros impares ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_impares(numeros)
print(f"Lista original: {numeros}")
print(f"Solo numeros impares: {resultado}")
print()


# ============================================
# EJERCICIO 20: Para una lista con elementos tipo integer y string obten una nueva lista solo 
# con los valores int. Usa la funcion filter()
# ============================================

def filtrar_solo_numeros(lista_mixta):
    # Esta funcion filtra solo los numeros enteros de una lista que tiene numeros y textos
    
    # Usamos filter() con isinstance() para verificar si cada elemento es un numero entero
    # isinstance(elemento, int) devuelve True si el elemento es un numero
    solo_numeros = list(filter(lambda elemento: isinstance(elemento, int) and not isinstance(elemento, bool), lista_mixta))
    
    return solo_numeros

# Probamos la funcion
print("=== Ejercicio 20: Filtrar solo numeros enteros ===")
lista_mixta = [1, "hola", 5, "Python", 10, "datos", 15, "analisis", 20]
resultado = filtrar_solo_numeros(lista_mixta)
print(f"Lista mixta: {lista_mixta}")
print(f"Solo numeros: {resultado}")
print()

# ============================================
# EJERCICIO 21
# Crea una funcion que calcule el cubo de un numero dado mediante una funcion lambda
# ============================================

# Funcion lambda que eleva un numero al cubo usando el operador **
cubo = lambda x: x ** 3

# Pruebas del ejercicio
print("=== EJERCICIO 21: Cubo con lambda ===")
print(f"El cubo de 2 es: {cubo(2)}")
print(f"El cubo de 5 es: {cubo(5)}")
print(f"El cubo de 10 es: {cubo(10)}")
print()


# ============================================
# EJERCICIO 22
# Dada una lista numerica, obten el producto total de los valores de dicha lista. Usa la funcion reduce()
# ============================================

def producto_total(lista):
    if not lista:
        return 0
    # Uso de reduce para multiplicar todos los elementos de la lista
    # La funcion lambda va acumulando el producto
    return reduce(lambda a, b: a * b, lista)

# Pruebas del ejercicio
print("=== EJERCICIO 22: Producto total con reduce ===")
numeros = [2, 3, 4, 5]
print(f"Lista: {numeros}")
print(f"Producto total: {producto_total(numeros)}")
print()


# ============================================
# EJERCICIO 23
# Concatena una lista de palabras. Usa la funcion reduce()
# ============================================

def concatenar_palabras(lista):
    # Utilizo reduce para concatenar todas las palabras
    resultado = reduce(lambda a, b: a + " " + b, lista)
    return resultado

# Pruebas del ejercicio
print("=== EJERCICIO 23: Concatenar lista con reduce ===")
palabras = ["Hola", "soy", "estudiante", "de", "Python"]
print(f"Lista de palabras: {palabras}")
print(f"Frase concatenada: {concatenar_palabras(palabras)}")
print()


# ============================================
# EJERCICIO 24
# Calcula la diferencia total en los valores de una lista. Usa la funcion reduce()
# ============================================

def diferencia_total(lista):
    # Reduce aplica la resta de forma acumulativa
    resultado = reduce(lambda a, b: a - b, lista)
    return resultado

# Pruebas del ejercicio
print("=== EJERCICIO 24: Diferencia total con reduce ===")
numeros = [100, 20, 10, 5]
print(f"Lista: {numeros}")
print(f"Diferencia total: {diferencia_total(numeros)}")
print()


# ============================================
# EJERCICIO 25
# Crea una funcion que cuente el numero de caracteres en una cadena de texto dada
# ============================================

def contar_caracteres(texto):
    # Utilizacion de len() para obtener la longitud del string
    cantidad = len(texto)
    return cantidad

# Pruebas del ejercicio
print("=== EJERCICIO 25: Contar caracteres ===")
texto1 = "Hola Mundo"
texto2 = "Python es genial"
print(f"Texto: '{texto1}' tiene {contar_caracteres(texto1)} caracteres")
print(f"Texto: '{texto2}' tiene {contar_caracteres(texto2)} caracteres")
print()


# ============================================
# EJERCICIO 26
# Crea una funcion lambda que calcule el resto de la division entre dos numeros dados
# ============================================

# Lambda que utiliza el operador modulo (%) para calcular el resto
resto_division = lambda a, b: a % b

# Pruebas del ejercicio
print("=== EJERCICIO 26: Resto de division con lambda ===")
print(f"10 dividido 3, resto: {resto_division(10, 3)}")
print(f"17 dividido 5, resto: {resto_division(17, 5)}")
print(f"20 dividido 4, resto: {resto_division(20, 4)}")
print()


# ============================================
# EJERCICIO 27
# Crea una funcion que calcule el promedio de una lista de numeros
# ============================================

def calcular_promedio_simple(lista):
    # Calculo del promedio: suma total dividida entre cantidad de elementos
    suma = sum(lista)
    cantidad = len(lista)
    promedio = suma // cantidad
    return promedio

# Pruebas del ejercicio
print("=== EJERCICIO 27: Calcular promedio ===")
notas = [8, 7, 9, 6, 10]
print(f"Notas: {notas}")
print(f"Promedio: {calcular_promedio_simple(notas):.2f}")
print()


# ============================================
# EJERCICIO 28
# Crea una funcion que busque y devuelva el primer elemento duplicado en una lista dada
# ============================================

def primer_duplicado(lista):
    # Uso un set para almacenar elementos ya vistos
    vistos = set()
    
    # Itero sobre cada elemento
    for elemento in lista:
        # Si el elemento ya esta en vistos, es el primer duplicado
        if elemento in vistos:
            return elemento
        # AÃ±ado el elemento al conjunto de vistos
        vistos.add(elemento)
    
    # Si no hay duplicados, retorno None
    return None

# Pruebas del ejercicio
print("=== EJERCICIO 28: Primer elemento duplicado ===")
lista1 = [1, 2, 3, 4, 2, 5, 6]
lista2 = [10, 20, 30, 40, 30]
lista3 = [1, 2, 3, 4, 5]
print(f"Lista: {lista1}")
print(f"Primer duplicado: {primer_duplicado(lista1)}")
print(f"Lista: {lista2}")
print(f"Primer duplicado: {primer_duplicado(lista2)}")
print(f"Lista: {lista3}")
print(f"Primer duplicado: {primer_duplicado(lista3)}")
print()


# ============================================
# EJERCICIO 29
# Crea una funcion que convierta una variable en una cadena de texto y enmascare 
# todos los caracteres con el caracter '#', excepto los ultimos cuatro
# ============================================

def enmascarar_texto(variable):
    # Conversion a string para trabajar con cualquier tipo de dato
    texto = str(variable)
    
    # Si tiene 4 o menos caracteres, no se enmascara
    if len(texto) <= 4:
        return texto
    
    # Calculo de caracteres a enmascarar
    cantidad_ocultar = len(texto) - 4
    
    # Generacion de la parte enmascarada con #
    parte_oculta = "#" * cantidad_ocultar
    
    # Extraccion de los ultimos 4 caracteres usando slicing
    ultimos_cuatro = texto[-4:]  
    
    # Concatenacion de la parte oculta con los ultimos caracteres
    resultado = parte_oculta + ultimos_cuatro
    return resultado

# Pruebas del ejercicio
print("=== EJERCICIO 29: Enmascarar texto ===")
tarjeta = "1234567890123456"
telefono = "612345678"
palabra = "Python"
print(f"Original: {tarjeta}")
print(f"Enmascarado: {enmascarar_texto(tarjeta)}")
print(f"Original: {telefono}")
print(f"Enmascarado: {enmascarar_texto(telefono)}")
print(f"Original: {palabra}")
print(f"Enmascarado: {enmascarar_texto(palabra)}")
print()


# ============================================
# EJERCICIO 30
# Crea una funcion que determine si dos palabras son anagramas
# Es decir, si estan formadas por las mismas letras pero en diferente orden
# ============================================

def son_anagramas(palabra1, palabra2):
    # Normalizacion a minusculas para comparacion case-insensitive
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Eliminacion de espacios
    palabra1 = palabra1.replace(" ", "")
    palabra2 = palabra2.replace(" ", "")
    
    # Comparacion de las letras ordenadas alfabeticamente
    # Si son anagramas, las letras ordenadas seran identicas
    return sorted(palabra1) == sorted(palabra2)

# Pruebas del ejercicio
print("=== EJERCICIO 30: Detectar anagramas ===")
print(f"'amor' y 'roma' son anagramas: {son_anagramas('amor', 'roma')}")
print(f"'listen' y 'silent' son anagramas: {son_anagramas('listen', 'silent')}")
print(f"'hello' y 'world' son anagramas: {son_anagramas('hello', 'world')}")
print(f"'Enrique' y 'quieren' son anagramas: {son_anagramas('Enrique', 'quieren')}")
print()

# ============================================
# EJERCICIO 31
# Crea una funcion que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre esta en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepcion.
# ============================================

def buscar_nombre_en_lista():
    
    # Aqui creo una funcion para buscar nombres en una lista
    # Me costo entender las excepciones al principio pero creo que ya lo tengo
    
    # Primero le pido al usuario que escriba los nombres
    print("Vamos a crear una lista de nombres")
    print("Escribe los nombres separados por comas")
    
    # Aqui recojo lo que escribe el usuario
    nombres_texto = input("Ingresa los nombres (ej: Juan, Maria, Pedro): ")
    
    # Tuve que investigar como convertir el texto en lista
    # strip() lo uso para quitar espacios que sobran (lo vi en un ejemplo)
    lista_nombres = [nombre.strip() for nombre in nombres_texto.split(',')]
    
    # Ahora le pregunto que nombre quiere buscar
    nombre_buscar = input("\nÂ¿Que nombre quieres buscar?: ").strip()
    
    try:
        # Aqui intento buscar el nombre en la lista
        if nombre_buscar in lista_nombres:
            print(f"OK - Genial! {nombre_buscar} esta en la lista")
        else:
            # Si no lo encuentro, lanzo el error como pide el ejercicio
            raise ValueError(f"El nombre '{nombre_buscar}' no esta en la lista")
    
    except ValueError as error:
        # Aqui capturo el error y lo muestro de forma amigable
        print(f"ERROR: {error}")
        print("Nombres disponibles:", lista_nombres)

# Probamos la funcion
print("=== Ejercicio 31: Buscar nombre en lista ===")
buscar_nombre_en_lista()
print()


# ============================================
# ============================================
# EJERCICIO 32
# Crea una funcion que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si esta en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aqui.
# ============================================

def buscar_empleado(nombre_completo, lista_empleados):
    """
    Esta funcion la hice para buscar empleados en una lista
    Al principio no entendia bien los diccionarios pero ya le cogi el truco
    
    Parametros que necesito:
    - nombre_completo: el nombre que estoy buscando
    - lista_empleados: donde tengo guardados todos los empleados
    """
    # Voy recorriendo uno por uno los empleados
    for empleado in lista_empleados:
        # Compruebo si el nombre es el que busco
        if empleado['nombre'] == nombre_completo:
            # Si lo encuentro, digo su puesto y ya esta
            return f"{nombre_completo} trabaja como {empleado['puesto']}"
    
    # Si llego aqui es que no lo encontre en toda la lista
    return f"{nombre_completo} no trabaja aqui"

# Aqui pongo un ejemplo para probar mi funcion:
print("=== Ejercicio 32: Buscar empleado ===")
empleados = [
    {'nombre': 'Ana Garcia', 'puesto': 'Desarrolladora'},
    {'nombre': 'Carlos Lopez', 'puesto': 'Disenador'},
    {'nombre': 'Maria Rodriguez', 'puesto': 'Project Manager'}
]

# Prueba 1: Buscar empleado que existe
print(buscar_empleado('Ana Garcia', empleados))

# Prueba 2: Buscar empleado que no existe
print(buscar_empleado('Pedro Martinez', empleados))
print()

# ============================================
# ============================================
# EJERCICIO 33
# Crea una funcion lambda que sume elementos correspondientes de dos listas dadas.
# ============================================

# Tuve que buscar que era una lambda, es como una funcion pero mas corta
# zip() lo entendi como que empareja elementos de las listas
sumar_listas = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]

# Prueba que hice para ver si funcionaba:
print("=== Ejercicio 33: Sumar listas con lambda ===")
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
resultado = sumar_listas(lista1, lista2)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Suma: {resultado}")
print()

# ============================================
# ============================================
# EJERCICIO 34
# Crea la clase Arbol, define un arbol generico con un tronco y ramas como atributos.
# ============================================

class Arbol:
    """
    Mi primera clase compleja! Me costo entender el concepto de clase
    pero ahora veo que es como crear mi propio tipo de objeto
    """
    
    def __init__(self):
        """
        Aqui inicializo mi arbol con valores basicos
        """
        self.tronco = 1  # El arbol empieza pequeÃ±ito
        self.ramas = []  # Al principio no tiene ramas
    
    def crecer_tronco(self):
        """
        Este metodo lo hice para que el tronco crezca de uno en uno
        """
        self.tronco += 1
        print(f"El tronco crecio! Ahora mide: {self.tronco}")
    
    def nueva_rama(self):
        """
        Con este metodo aÃ±ado ramas nuevas a mi arbol
        Siempre empiezan con tamaÃ±o 1
        """
        self.ramas.append(1)
        print(f"Nueva rama aÃ±adida! Total de ramas: {len(self.ramas)}")
    
    def crecer_ramas(self):
        """
        Aqui hago que todas las ramas crezcan a la vez
        Me costo entender como modificar todos los elementos de la lista
        """
        # Tuve que usar un bucle para cambiar cada rama
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
        print(f"Todas las ramas crecieron! Longitudes: {self.ramas}")
    
    def quitar_rama(self, posicion):
        """
        Este metodo quita una rama segun su posicion
        Tuve que tener cuidado con los indices que empiezan en 0
        """
        if 0 <= posicion < len(self.ramas):
            rama_quitada = self.ramas.pop(posicion)
            print(f"Rama en posicion {posicion} quitada (longitud: {rama_quitada})")
        else:
            print(f"No hay rama en la posicion {posicion}")
    
    def info_arbol(self):
        """
        Aqui devuelvo toda la informacion del arbol en un diccionario
        Me parecio util para ver el estado completo
        """
        info = {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitudes_ramas': self.ramas
        }
        return info

# Caso de uso del ejercicio 34
print("=== Ejercicio 34: Clase Arbol ===")
print("Creando un arbol...")
mi_arbol = Arbol()

print("\n1. Hacer crecer el tronco:")
mi_arbol.crecer_tronco()

print("\n2. AÃ±adir una nueva rama:")
mi_arbol.nueva_rama()

print("\n3. Hacer crecer todas las ramas:")
mi_arbol.crecer_ramas()

print("\n4. AÃ±adir dos nuevas ramas:")
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

print("\n5. Retirar la rama en posicion 2:")
mi_arbol.quitar_rama(2)

print("\n6. Informacion del arbol:")
info = mi_arbol.info_arbol()
print(f"Longitud del tronco: {info['longitud_tronco']}")
print(f"Numero de ramas: {info['numero_ramas']}")
print(f"Longitudes de ramas: {info['longitudes_ramas']}")
print()

# ============================================
# EJERCICIO 35 - NO EXISTE EN EL ENUNCIADO
# ============================================
# Nota para el profesor: No encontre el ejercicio 35 en el PDF

# ============================================
# ============================================
# EJERCICIO 36
# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente.
# ============================================

class UsuarioBanco:
    """
    Segunda clase que hago con excepciones incluidas
    Me ayudo mucho el ejemplo anterior del arbol para entender mejor las clases
    """
    
    def __init__(self, nombre, saldo, tiene_cuenta):
        """
        Aqui creo un nuevo usuario del banco con sus datos basicos
        
        Lo que necesito guardar:
        - nombre: como se llama el usuario
        - saldo: cuanto dinero tiene
        - tiene_cuenta: si tiene cuenta corriente (True/False)
        """
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta
    
    def retirar_dinero(self, cantidad):
        """
        Metodo para sacar dinero de la cuenta
        Tuve que aÃ±adir validacion para que no saque mas de lo que tiene
        """
        # Primero compruebo si tiene suficiente dinero
        if cantidad > self.saldo:
            # Si no tiene suficiente, lanzo error como pide el ejercicio
            raise ValueError(f"Saldo insuficiente. Tienes {self.saldo}â‚¬ y quieres retirar {cantidad}â‚¬")
        
        # Si llega aqui es que si tiene suficiente
        self.saldo -= cantidad
        print(f"{self.nombre} retiro {cantidad}â‚¬. Saldo actual: {self.saldo}â‚¬")
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Este metodo transfiere dinero desde otro usuario hacia este
        Al principio lo entendi al reves pero ya lo tengo claro
        """
        # Primero miro si el otro usuario tiene suficiente dinero
        if otro_usuario.saldo < cantidad:
            # Si no tiene, lanzo el error
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir")
        
        # Si tiene suficiente, hago la transferencia
        otro_usuario.saldo -= cantidad  # Le quito al que envia
        self.saldo += cantidad          # Se lo sumo al que recibe (este usuario)
        
        print(f"Transferencia exitosa de {cantidad}â‚¬")
        print(f"  De: {otro_usuario.nombre} (saldo: {otro_usuario.saldo}â‚¬)")
        print(f"  A: {self.nombre} (saldo: {self.saldo}â‚¬)")
    
    def agregar_dinero(self, cantidad):
        """
        Metodo simple para ingresar dinero
        Este fue el mas facil de hacer
        """
        self.saldo += cantidad
        print(f"{self.nombre} ingreso {cantidad}â‚¬. Saldo actual: {self.saldo}â‚¬")

# Caso de uso del ejercicio 36
print("=== Ejercicio 36: Clase UsuarioBanco ===")
print("\n1. Crear dos usuarios:")
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
print(f"- {alicia.nombre} con saldo inicial: {alicia.saldo}â‚¬")
print(f"- {bob.nombre} con saldo inicial: {bob.saldo}â‚¬")

print("\n2. Agregar 20â‚¬ al saldo de Bob:")
bob.agregar_dinero(20)

print("\n3. Transferir 50â‚¬ desde Bob a Alicia:")
alicia.transferir_dinero(bob, 50)

print("\n4. Retirar 30â‚¬ del saldo de Alicia:")
alicia.retirar_dinero(30)
print()

# ============================================
# EJERCICIO 37
"""
37. Crea una funcion llamada procesar_texto que procesa un texto segun la opcion especificada.
"""

def contar_palabras(texto):
    """
    Esta funcion cuenta cuantas veces aparece cada palabra
    Me gusto porque es como hacer estadisticas del texto
    """
    # Primero paso todo a minusculas y separo las palabras
    palabras = texto.lower().split()
    
    # Creo un diccionario vacio para ir contando
    contador = {}
    
    # Voy contando cada palabra que encuentro
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1  # Si ya existe, le sumo 1
        else:
            contador[palabra] = 1   # Si es nueva, empiezo en 1
    
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Esta funcion cambia una palabra por otra en todo el texto
    Es como el buscar y reemplazar de Word que uso mucho
    """
    # Uso replace que lo busque y es perfecto para esto
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    """
    Aqui elimino una palabra especifica del texto
    Tuve que pensar un poco como hacerlo sin replace
    """
    # Separo el texto en palabras individuales
    palabras = texto.split()
    
    # Filtro quitando la palabra que no quiero
    # Esta sintaxis me costo pero es muy util
    palabras_filtradas = [p for p in palabras if p != palabra]
    
    # Vuelvo a juntar todo con espacios
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """
    Esta es la funcion principal que llama a las otras segun la opcion
    Lo de *args me costo mucho entender, son argumentos variables
    """
    if opcion == "contar":
        # Para contar no necesito argumentos extra
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        # Para reemplazar necesito la palabra original y la nueva
        if len(args) >= 2:
            return reemplazar_palabras(texto, args[0], args[1])
        else:
            return "Error: necesito la palabra original y la nueva"
    
    elif opcion == "eliminar":
        # Para eliminar solo necesito que palabra quitar
        if len(args) >= 1:
            return eliminar_palabra(texto, args[0])
        else:
            return "Error: necesito saber que palabra eliminar"
    
    else:
        return "Opcion no valida. Usa: contar, reemplazar o eliminar"

# Caso de uso del ejercicio 37
print("=== Ejercicio 37: Procesar texto ===")
texto_prueba = "Python es genial Python es poderoso Python es facil"

print("\nTexto original:")
print(f'"{texto_prueba}"')

print("\n1. Contar palabras:")
resultado_contar = procesar_texto(texto_prueba, "contar")
print(resultado_contar)

print("\n2. Reemplazar 'Python' por 'JavaScript':")
resultado_reemplazar = procesar_texto(texto_prueba, "reemplazar", "Python", "JavaScript")
print(f'"{resultado_reemplazar}"')

print("\n3. Eliminar la palabra 'es':")
resultado_eliminar = procesar_texto(texto_prueba, "eliminar", "es")
print(f'"{resultado_eliminar}"')
print()

# ============================================
# ============================================
# EJERCICIO 38
# Genera un programa que nos diga si es de noche, de dia o tarde segun la hora proporcionada por el usuario.
# ============================================

def determinar_momento_del_dia():
    """
    Funcion que determina si es dia, tarde o noche
    Este fue facil, solo usar condicionales con las horas
    """
    try:
        # Le pido al usuario que escriba la hora
        hora = int(input("Â¿Que hora es? (0-23): "))
        
        # Verifico que sea una hora valida (entre 0 y 23)
        if hora < 0 or hora > 23:
            print("Error: La hora debe estar entre 0 y 23")
            return
        
        # Aqui determino que momento del dia es segun la hora
        if 6 <= hora < 14:
            momento = "dia"
            print(f"Son las {hora}:00 - Es de {momento}")
        elif 14 <= hora < 20:
            momento = "tarde"
            print(f"Son las {hora}:00 - Es de {momento}")
        else:  # Entre 20-23 o 0-5
            momento = "noche"
            print(f"Son las {hora}:00 - Es de {momento}")
    
    except ValueError:
        # Por si el usuario escribe algo que no es numero
        print("Error: Por favor ingresa un numero entero")

# Prueba del ejercicio 38
print("=== Ejercicio 38: Momento del dia ===")
determinar_momento_del_dia()
print()

# ============================================
# ============================================
# EJERCICIO 39
# Escribe un programa que determine que calificacion en texto tiene un alumno en base a su calificacion numerica.
# Las reglas de calificacion son:
# - 0 - 69 insuficiente
# - 70 - 79 bien  
# - 80 - 89 muy bien
# - 90 - 100 excelente
# ============================================

def obtener_calificacion_texto():
    """
    Convierte una nota numerica en su equivalente en texto
    Me recuerda a cuando recibia las notas en el colegio
    """
    try:
        # Pido la nota al usuario
        nota = float(input("Ingresa la calificacion numerica (0-100): "))
        
        # Verifico que sea una nota valida
        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100")
            return
        
        # Determino la calificacion segun los rangos del ejercicio
        if nota <= 69:
            calificacion = "Insuficiente"
        elif nota <= 79:
            calificacion = "Bien"
        elif nota <= 89:
            calificacion = "Muy bien"
        else:  # 90-100
            calificacion = "Excelente"
        
        print(f"Nota: {nota} - Calificacion: {calificacion}")
    
    except ValueError:
        print("Error: Por favor ingresa un numero valido")

# Prueba del ejercicio 39
print("=== Ejercicio 39: Calificacion en texto ===")
obtener_calificacion_texto()
print()

# ============================================
# EJERCICIO 40 
# ============================================
"""
40. Escribe una funcion que tome dos parametros: figura (una cadena que puede ser "rectangulo", "circulo" o 
"triangulo") y datos (una tupla con los datos necesarios para calcular el area de la figura).
"""

def calcular_area(figura, datos):
    """
    Calcula el area de diferentes figuras geometricas
    Me gusta porque uso las formulas que aprendi en matematicas
    """
    
    if figura == "rectangulo":
        # Para el rectangulo necesito base y altura
        if len(datos) == 2:
            base, altura = datos
            area = base * altura
            return f"Area del rectangulo: {area}"
        else:
            return "Error: El rectangulo necesita base y altura"
    
    elif figura == "circulo":
        # Para el circulo necesito el radio
        if len(datos) == 1:
            radio = datos[0]
            # Ahora si puedo usar math.pi porque lo importe arriba
            area = math.pi * radio ** 2
            return f"Area del circulo: {area:.2f}"
        else:
            return "Error: El circulo necesita solo el radio"
    
    elif figura == "triangulo":
        # Para el triangulo es base por altura dividido entre 2
        if len(datos) == 2:
            base, altura = datos
            area = (base * altura) / 2
            return f"Area del triangulo: {area}"
        else:
            return "Error: El triangulo necesita base y altura"
    
    else:
        return "Figura no reconocida. Usa: rectangulo, circulo o triangulo"

# Prueba del ejercicio 40
print("=== Ejercicio 40: Calcular area de figuras ===")
print("\n1. Rectangulo (base=5, altura=3):")
print(calcular_area("rectangulo", (5, 3)))

print("\n2. Circulo (radio=4):")
print(calcular_area("circulo", (4,)))

print("\n3. Triangulo (base=6, altura=4):")
print(calcular_area("triangulo", (6, 4)))
print()

# ============================================
# ============================================
# EJERCICIO 41
# En este ejercicio, se te pedira que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en linea, despues de aplicar un descuento.
# ============================================

def calcular_precio_final():
    """
    Calcula el precio final de una compra con descuentos
    Me recuerda a cuando compro online y uso cupones
    """
    print("TIENDA ONLINE - Calculadora de Precios")
    print("-" * 40)
    
    valor_cupon = 0
    
    try:
        # Paso 1: Pido el precio original del articulo
        precio_original = float(input("Ingresa el precio original del articulo (â‚¬): "))
        
        # Verifico que el precio sea positivo (no puede ser 0 o negativo)
        if precio_original <= 0:
            print("Error: El precio debe ser mayor que 0")
            return
        
        # Paso 2: Pregunto si tiene cupon de descuento
        tiene_cupon = input("Â¿Tienes un cupon de descuento? (si/no): ").lower()
        
        # Paso 3: Si tiene cupon, pido el valor del descuento
        if tiene_cupon == "si" or tiene_cupon == "sÃ­":
            valor_cupon = float(input("Ingresa el valor del cupon de descuento (â‚¬): "))
            
            # Paso 4: Verifico si el cupon es valido y lo aplico
            if valor_cupon > 0:
                # Me aseguro de que el descuento no sea mayor que el precio
                if valor_cupon > precio_original:
                    print("\nAVISO: El descuento es mayor que el precio. Aplicando descuento maximo.")
                    precio_final = 0
                else:
                    precio_final = precio_original - valor_cupon
                    
                print(f"\nDescuento aplicado: -{valor_cupon}â‚¬")
            else:
                # Si el cupon no es valido (0 o negativo)
                print("\nEl cupon no es valido (debe ser mayor que 0)")
                precio_final = precio_original
        else:
            # Si no tiene cupon
            precio_final = precio_original
            print("\nNo se aplico ningun descuento")
        
        # Paso 5: Muestro el resumen final
        print("-" * 40)
        print(f"Precio original: {precio_original:.2f}â‚¬")
        if tiene_cupon in ["si", "sÃ­"] and valor_cupon > 0:
            print(f"Descuento: -{valor_cupon:.2f}â‚¬")
        print(f"PRECIO FINAL: {precio_final:.2f}â‚¬")
        print("-" * 40)
        
    except ValueError:
        # Por si el usuario escribe texto en vez de numeros
        print("Error: Por favor ingresa un numero valido")

# Prueba del ejercicio 41
print("=== Ejercicio 41: Precio final con descuento ===")
calcular_precio_final()
print()

print("\n" + "="*50)
print("TODOS LOS EJERCICIOS COMPLETADOS")
print("="*50)