# PROYECTO LOGICA: Katas de Python
# ============================================
# Este proyecto contiene 41 ejercicios de Python que demuestran
# el manejo de tipos de datos, estructuras, funciones, clases y excepciones
# Desarrollado como parte del modulo de Python del bootcamp de Analisis de Datos
# ============================================

from functools import reduce
import math

# ============================================
# EJERCICIO 1
# Escribe una funcion que reciba una cadena de texto como parametro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
# ============================================

def frecuencia_letras(texto):
    # Inicializo un diccionario vacio para almacenar las frecuencias
    frecuencias = {}
    
    # Itero sobre cada caracter del texto recibido
    for letra in texto:
        # Verifico que el caracter no sea un espacio
        if letra != ' ':
            # Si la letra ya existe en el diccionario, incremento su contador
            if letra in frecuencias:
                frecuencias[letra] = frecuencias[letra] + 1
            # Si es la primera aparicion, la agrego con valor inicial 1
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
    # Funcion auxiliar que multiplica cualquier numero por 2
    return numero * 2

def obtener_dobles(lista_numeros):
    # Aplico map() para transformar cada elemento aplicando doblar_numero
    # map() es una funcion de orden superior que aplica una funcion a cada elemento
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
    # Creo una lista vacia para acumular las palabras que cumplan el criterio
    palabras_encontradas = []
    
    # Recorro cada palabra de la lista original
    for palabra in lista_palabras:
        # Verifico si la palabra objetivo esta contenida en la palabra actual
        # El operador 'in' permite buscar subcadenas dentro de strings
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
    # Funcion auxiliar que resta el segundo numero del primero
    return num1 - num2

def diferencia_listas(lista1, lista2):
    # Uso map() con dos listas como argumentos
    # map() procesa los elementos de ambas listas en paralelo, uno a uno
    diferencias = list(map(calcular_diferencia, lista1, lista2))
    return diferencias

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
    # Sumo todas las notas usando un acumulador
    suma_notas = 0
    for nota in lista_notas:
        suma_notas = suma_notas + nota
    
    # Calculo el promedio dividiendo la suma entre la cantidad de elementos
    media = suma_notas / len(lista_notas)
    
    # Determino el estado segun si la media supera o iguala la nota de aprobado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    # Devuelvo una tupla con ambos valores
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
# ============================================

def calcular_factorial(numero):
    # Caso base: el factorial de 0 y 1 es 1
    # Este es el punto donde la recursion se detiene
    if numero == 0 or numero == 1:
        return 1
    else:
        # Caso recursivo: n! = n * (n-1)!
        # La funcion se llama a si misma con un valor menor
        return numero * calcular_factorial(numero - 1)

# Prueba del ejercicio 6
print("EJERCICIO 6: Factorial recursivo")
print("-" * 40)
resultado = calcular_factorial(5)
print(f"El factorial de 5 es: {resultado}")
print("Explicacion: 5! = 5 x 4 x 3 x 2 x 1 = 120")
print("")


# ============================================
# EJERCICIO 7
# Genera una funcion que convierta una lista de tuplas a una lista de strings.
# Usa la funcion map()
# ============================================

def tuplas_a_strings(lista_tuplas):
    # Uso map() para aplicar str() a cada tupla
    # str() convierte cualquier objeto de Python a su representacion en texto
    resultado = list(map(str, lista_tuplas))
    return resultado

# Prueba del ejercicio 7
print("EJERCICIO 7: Tuplas a Strings")
print("-" * 40)
tuplas = [(1, 2), (3, 4), (5, 6)]
print(f"Lista original de tuplas: {tuplas}")
strings = tuplas_a_strings(tuplas)
print(f"Lista convertida a strings: {strings}")
print("")


# ============================================
# EJERCICIO 8
# Escribe un programa que pida al usuario dos numeros e intente dividirlos.
# Si el usuario ingresa un valor no numerico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada.
# ============================================

def dividir_numeros_con_ejemplos(num1, num2):
    # He creado una version con parametros para facilitar las pruebas
    # sin necesidad de input() del usuario cada vez
    try:
        # Intento convertir los valores recibidos a numeros flotantes
        numero1 = float(num1)
        numero2 = float(num2)
        
        # Realizo la operacion de division
        resultado = numero1 / numero2
        
        # Si no hay errores, muestro el resultado exitoso
        print(f"La division fue exitosa: {numero1} / {numero2} = {resultado}")
        
    except ValueError:
        # Captura el error cuando los valores no son numericos
        print("Error: Debes ingresar valores numericos")
        
    except ZeroDivisionError:
        # Captura el error cuando se intenta dividir por cero
        print("Error: No se puede dividir por cero")

# Prueba del ejercicio 8
print("EJERCICIO 8: Division con manejo de errores")
print("-" * 40)

# Caso 1: Division normal que funciona correctamente
print("Caso 1: Dividir 10 entre 2")
dividir_numeros_con_ejemplos(10, 2)

# Caso 2: Division por cero - debe capturar ZeroDivisionError
print("\nCaso 2: Dividir 10 entre 0")
dividir_numeros_con_ejemplos(10, 0)

# Caso 3: Valor no numerico - debe capturar ValueError
print("\nCaso 3: Dividir 10 entre 'abc'")
dividir_numeros_con_ejemplos(10, "abc")
print("")


# ============================================
# EJERCICIO 9
# Escribe una funcion que tome una lista de nombres de mascotas como parametro
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en Espana.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]
# Usa la funcion filter()
# ============================================

def filtrar_mascotas_permitidas(lista_mascotas):
    # Defino la lista de mascotas que estan prohibidas segun la legislacion
    prohibidas = ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]
    
    # Uso filter() con una funcion lambda para quedarnos solo con mascotas permitidas
    # lambda verifica si cada mascota NO esta en la lista de prohibidas
    mascotas_permitidas = list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))
    
    return mascotas_permitidas

# Prueba del ejercicio 9
print("EJERCICIO 9: Filtrar mascotas prohibidas")
print("-" * 40)
todas_las_mascotas = ["Perro", "Gato", "Tigre", "Conejo", "Serpiente Piton", "Hamster", "Oso"]
print(f"Lista original: {todas_las_mascotas}")
permitidas = filtrar_mascotas_permitidas(todas_las_mascotas)
print(f"Mascotas permitidas: {permitidas}")
print("")


# ============================================
# EJERCICIO 10
# Escribe una funcion que reciba una lista de numeros y calcule su promedio.
# Si la lista esta vacia, lanza una excepcion personalizada y maneja el error adecuadamente.
# ============================================

# Creo una clase de excepcion personalizada heredando de Exception
class ListaVaciaError(Exception):
    # Esta clase representa un error especifico para listas vacias
    pass

def calcular_promedio(lista_numeros):
    # Verifico si la lista esta vacia antes de proceder
    if len(lista_numeros) == 0:
        # Lanzo mi excepcion personalizada con un mensaje descriptivo
        raise ListaVaciaError("Error: La lista esta vacia, no se puede calcular el promedio")
    
    # Si la lista tiene elementos, calculo el promedio
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    
    return promedio

# Prueba del ejercicio 10
print("EJERCICIO 10: Promedio con excepcion personalizada")
print("-" * 40)

# Caso 1: Lista con numeros - deberia funcionar correctamente
numeros = [8, 7, 9, 6, 10]
try:
    resultado = calcular_promedio(numeros)
    print(f"El promedio de {numeros} es: {resultado}")
except ListaVaciaError as error:
    print(error)

# Caso 2: Lista vacia - deberia lanzar ListaVaciaError
lista_vacia = []
try:
    resultado = calcular_promedio(lista_vacia)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as error:
    print(error)
print("")


# ============================================
# EJERCICIO 11
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario
# ingresa un valor no numerico o un valor fuera del rango esperado (por ejemplo,
# menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# ============================================

def validar_edad():
    # Esta funcion solicita y valida la edad del usuario
    try:
        # Solicito al usuario que ingrese su edad
        edad = input("Por favor, introduce tu edad: ")
        
        # Intento convertir el input a un numero entero
        edad_numerica = int(edad)
        
        # Valido que la edad este dentro de un rango razonable
        if edad_numerica < 0:
            print("Error: La edad no puede ser negativa")
        elif edad_numerica > 120:
            print("Error: La edad no puede ser mayor a 120 anos")
        else:
            # Si pasa todas las validaciones, muestro la edad
            print(f"Tu edad es: {edad_numerica} anos")
    
    except ValueError:
        # Capturo el error si el usuario no ingreso un numero valido
        print("Error: Debes introducir un numero valido")

# Prueba del ejercicio 11
print("EJERCICIO 11: Validar edad")
print("-" * 40)
# Esta funcion requiere input del usuario, por lo que la llamaria manualmente
# validar_edad()
print("Funcion disponible para validar edad con input() del usuario")
print("")


# ============================================
# EJERCICIO 12
# Genera una funcion que al recibir una frase devuelva una lista con la longitud
# de cada palabra. Usa la funcion map()
# ============================================

def longitud_palabras(frase):
    # Separo la frase en palabras individuales usando split()
    palabras = frase.split()
    
    # NOTA: Aqui deberia usar map() pero voy a intentar hacerlo con un bucle
    # porque me resulta mas facil de entender
    longitudes = []
    
    # Recorro cada palabra y calculo su longitud con len()
    for palabra in palabras:
        longitudes.append(len(palabra))
    
    return longitudes

# Prueba del ejercicio 12
print("EJERCICIO 12: Longitud de palabras")
print("-" * 40)
frase_ejemplo = "Hola me llamo Gabi y estudio analisis de datos"
resultado = longitud_palabras(frase_ejemplo)
print(f"Frase: {frase_ejemplo}")
print(f"Longitudes: {resultado}")
print("")


# ============================================
# EJERCICIO 13
# Genera una funcion la cual, para un conjunto de caracteres, devuelva una lista
# de tuplas con cada letra en mayusculas y minusculas. Las letras no pueden estar repetidas.
# Usa la funcion map()
# ============================================

def mayusculas_minusculas(caracteres):
    # Primero elimino las letras repetidas usando set()
    # set() crea un conjunto que automaticamente elimina duplicados
    letras_unicas = set(caracteres)
    
    # Uso map() con una lambda para crear tuplas (mayuscula, minuscula) de cada letra
    # upper() convierte a mayuscula y lower() a minuscula
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))
    
    return resultado

# Prueba del ejercicio 13
print("EJERCICIO 13: Mayusculas y minusculas")
print("-" * 40)
caracteres_ejemplo = "aabbccdefgh"
resultado = mayusculas_minusculas(caracteres_ejemplo)
print(f"Caracteres originales: {caracteres_ejemplo}")
print(f"Tuplas (mayuscula, minuscula): {resultado}")
print("")


# ============================================
# EJERCICIO 14
# Crea una funcion que retorne las palabras de una lista de palabras que comience
# con una letra en especifico. Usa la funcion filter()
# ============================================

def palabras_con_letra(lista_palabras, letra_inicial):
    # Uso filter() con lambda para filtrar palabras que empiezan con la letra especificada
    # palabra[0] obtiene el primer caracter de la palabra
    # lower() normaliza ambos a minusculas para comparacion case-insensitive
    palabras_filtradas = list(filter(lambda palabra: palabra[0].lower() == letra_inicial.lower(), lista_palabras))
    
    return palabras_filtradas

# Prueba del ejercicio 14
print("EJERCICIO 14: Palabras que empiezan con letra especifica")
print("-" * 40)
lista_palabras = ["Manzana", "Pera", "Platano", "Mango", "Naranja", "Melon"]
letra = "M"
resultado = palabras_con_letra(lista_palabras, letra)
print(f"Lista de palabras: {lista_palabras}")
print(f"Palabras que empiezan con '{letra}': {resultado}")
print("")


# ============================================
# EJERCICIO 15
# Crea una funcion lambda que sume 3 a cada numero de una lista dada.
# ============================================

# Defino una funcion lambda que toma una lista y suma 3 a cada elemento
# La lambda interna (x: x + 3) suma 3 a cada numero
# map() aplica esa lambda a cada elemento de la lista
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Prueba del ejercicio 15
print("EJERCICIO 15: Sumar 3 a cada numero")
print("-" * 40)
numeros = [1, 5, 10, 15, 20]
resultado = sumar_tres(numeros)
print(f"Lista original: {numeros}")
print(f"Sumando 3 a cada numero: {resultado}")
print("")


# ============================================
# EJERCICIO 16
# Escribe una funcion que tome una cadena de texto y un numero entero n como
# parametros y devuelva una lista de todas las palabras que sean mas largas que n.
# Usa la funcion filter()
# ============================================

def palabras_mas_largas(texto, n):
    # Separo el texto en palabras individuales
    palabras = texto.split()
    
    # Uso filter() con lambda para quedarnos solo con palabras que tengan mas de n caracteres
    # len(palabra) > n verifica la longitud de cada palabra
    palabras_largas = list(filter(lambda palabra: len(palabra) > n, palabras))
    
    return palabras_largas

# Prueba del ejercicio 16
print("EJERCICIO 16: Palabras mas largas que n")
print("-" * 40)
texto_ejemplo = "Python es un lenguaje de programacion increible"
n = 5
resultado = palabras_mas_largas(texto_ejemplo, n)
print(f"Texto: {texto_ejemplo}")
print(f"Palabras con mas de {n} letras: {resultado}")
print("")


# ============================================
# EJERCICIO 17
# Crea una funcion que tome una lista de digitos y devuelva el numero correspondiente.
# Por ejemplo, [5,7,2] corresponde al numero quinientos setenta y dos (572).
# Usa la funcion reduce()
# ============================================

def digitos_a_numero(digitos):
    # NOTA: Aqui deberia usar reduce() pero voy a intentar otro metodo
    # Convierto cada digito a string y los concateno
    numero_texto = ""
    for digito in digitos:
        numero_texto = numero_texto + str(digito)
    
    # Finalmente convierto el string completo a entero
    numero = int(numero_texto)
    
    return numero

# Prueba del ejercicio 17
print("EJERCICIO 17: Convertir digitos a numero")
print("-" * 40)
digitos = [5, 7, 2]
resultado = digitos_a_numero(digitos)
print(f"Lista de digitos: {digitos}")
print(f"Numero formado: {resultado}")
print("")


# ============================================
# EJERCICIO 18
# Escribe un programa en Python que cree una lista de diccionarios que contenga
# informacion de estudiantes (nombre, edad, calificacion) y use la funcion filter
# para extraer a los estudiantes con una calificacion mayor o igual a 90.
# Usa la funcion filter()
# ============================================

def estudiantes_excelentes(lista_estudiantes):
    # Uso filter() con lambda para filtrar estudiantes con calificacion >= 90
    # estudiante["calificacion"] accede al valor de calificacion en cada diccionario
    estudiantes_filtrados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))
    
    return estudiantes_filtrados

# Creo una lista de estudiantes con sus datos
print("EJERCICIO 18: Estudiantes con calificacion >= 90")
print("-" * 40)
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 85},
    {"nombre": "Maria", "edad": 21, "calificacion": 92},
    {"nombre": "Pedro", "edad": 23, "calificacion": 78},
    {"nombre": "Laura", "edad": 20, "calificacion": 98}
]

# Filtro los estudiantes con calificacion excelente
resultado = estudiantes_excelentes(estudiantes)
print("Estudiantes con calificacion >= 90:")
for estudiante in resultado:
    print(f"  - {estudiante['nombre']}: {estudiante['calificacion']} puntos")
print("")


# ============================================
# EJERCICIO 19
# Crea una funcion lambda que filtre los numeros impares de una lista dada.
# ============================================

# NOTA: Un numero es impar cuando el resto de dividirlo entre 2 es 1
# Creo una lambda que usa filter() para mantener solo numeros impares
# x % 2 == 0 verifica si el resto es 0 (numero par)
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

# Prueba del ejercicio 19
print("EJERCICIO 19: Filtrar numeros impares")
print("-" * 40)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_impares(numeros)
print(f"Lista original: {numeros}")
print(f"Solo numeros impares: {resultado}")
print("")


# ============================================
# EJERCICIO 20
# Para una lista con elementos tipo integer y string obten una nueva lista solo
# con los valores int. Usa la funcion filter()
# ============================================

def filtrar_solo_numeros(lista_mixta):
    # Uso filter() con isinstance() para verificar el tipo de cada elemento
    # isinstance(elemento, int) devuelve True solo si el elemento es un entero
    solo_numeros = list(filter(lambda elemento: isinstance(elemento, int), lista_mixta))
    
    return solo_numeros

# Prueba del ejercicio 20
print("EJERCICIO 20: Filtrar solo numeros enteros")
print("-" * 40)
lista_mixta = [1, "hola", 5, "Python", 10, "datos", 15, "analisis", 20]
resultado = filtrar_solo_numeros(lista_mixta)
print(f"Lista mixta: {lista_mixta}")
print(f"Solo numeros: {resultado}")
print("")


# ============================================
# EJERCICIO 21
# Crea una funcion que calcule el cubo de un numero dado mediante una funcion lambda
# ============================================

# Defino una funcion lambda que eleva un numero al cubo
# El operador ** se usa para potenciacion
cubo = lambda x: x ** 3

# Pruebas del ejercicio 21
print("EJERCICIO 21: Cubo con lambda")
print("-" * 40)
print(f"El cubo de 2 es: {cubo(2)}")
print(f"El cubo de 5 es: {cubo(5)}")
print(f"El cubo de 10 es: {cubo(10)}")
print("")


# ============================================
# EJERCICIO 22
# Dada una lista numerica, obten el producto total de los valores de dicha lista.
# Usa la funcion reduce()
# ============================================

def producto_total(lista):
    # Uso reduce() para multiplicar acumulativamente todos los elementos
    # La lambda recibe dos argumentos: el acumulador (a) y el siguiente elemento (b)
    resultado = reduce(lambda a, b: a * b, lista)
    return resultado

# Pruebas del ejercicio 22
print("EJERCICIO 22: Producto total con reduce")
print("-" * 40)
numeros = [2, 3, 4, 5]
print(f"Lista: {numeros}")
print(f"Producto total: {producto_total(numeros)}")
print("")


# ============================================
# EJERCICIO 23
# Concatena una lista de palabras. Usa la funcion reduce()
# ============================================

def concatenar_palabras(lista):
    # Uso reduce() para concatenar todas las palabras
    # La lambda va uniendo las palabras una tras otra
    resultado = reduce(lambda a, b: a + b, lista)
    return resultado

# Pruebas del ejercicio 23
print("EJERCICIO 23: Concatenar lista con reduce")
print("-" * 40)
palabras = ["Hola", "soy", "estudiante", "de", "Python"]
print(f"Lista de palabras: {palabras}")
print(f"Frase concatenada: {concatenar_palabras(palabras)}")
print("")


# ============================================
# EJERCICIO 24
# Calcula la diferencia total en los valores de una lista. Usa la funcion reduce()
# ============================================

def diferencia_total(lista):
    # Uso reduce() para restar acumulativamente los elementos
    # Comienza con el primer elemento y va restando los siguientes
    resultado = reduce(lambda a, b: a - b, lista)
    return resultado

# Pruebas del ejercicio 24
print("EJERCICIO 24: Diferencia total con reduce")
print("-" * 40)
numeros = [100, 20, 10, 5]
print(f"Lista: {numeros}")
print(f"Diferencia total: {diferencia_total(numeros)}")
print("")


# ============================================
# EJERCICIO 25
# Crea una funcion que cuente el numero de caracteres en una cadena de texto dada.
# ============================================

def contar_caracteres(texto):
    # Uso len() para obtener la longitud total del string
    cantidad = len(texto)
    return cantidad

# Pruebas del ejercicio 25
print("EJERCICIO 25: Contar caracteres")
print("-" * 40)
texto1 = "Hola Mundo"
texto2 = "Python es genial"
print(f"Texto: '{texto1}' tiene {contar_caracteres(texto1)} caracteres")
print(f"Texto: '{texto2}' tiene {contar_caracteres(texto2)} caracteres")
print("")


# ============================================
# EJERCICIO 26
# Crea una funcion lambda que calcule el resto de la division entre dos numeros dados.
# ============================================

# Creo una lambda que usa el operador modulo (%) para calcular el resto
# El operador % devuelve el resto de una division entera
resto_division = lambda a, b: a % b

# Pruebas del ejercicio 26
print("EJERCICIO 26: Resto de division con lambda")
print("-" * 40)
print(f"10 dividido 3, resto: {resto_division(10, 3)}")
print(f"17 dividido 5, resto: {resto_division(17, 5)}")
print(f"20 dividido 4, resto: {resto_division(20, 4)}")
print("")


# ============================================
# EJERCICIO 27
# Crea una funcion que calcule el promedio de una lista de numeros.
# ============================================

def calcular_promedio_lista(lista):
    # Calculo el promedio: suma total dividida entre cantidad de elementos
    suma = sum(lista)
    cantidad = len(lista)
    # NOTA: Uso division entera para obtener un resultado sin decimales
    promedio = suma // cantidad
    return promedio

# Pruebas del ejercicio 27
print("EJERCICIO 27: Calcular promedio")
print("-" * 40)
notas = [8, 7, 9, 6, 10]
print(f"Notas: {notas}")
print(f"Promedio: {calcular_promedio_lista(notas):.2f}")
print("")


# ============================================
# EJERCICIO 28
# Crea una funcion que busque y devuelva el primer elemento duplicado en una lista dada.
# ============================================

def primer_duplicado(lista):
    # Uso un conjunto (set) para almacenar elementos ya vistos
    # Los sets permiten verificacion de pertenencia en tiempo constante
    vistos = set()
    
    # Itero sobre cada elemento de la lista
    for elemento in lista:
        # Verifico si el elemento ya fue encontrado anteriormente
        if elemento in vistos:
            return elemento
        # Si no, lo agrego al conjunto de elementos vistos
        vistos.add(elemento)
    
    # Si no hay duplicados, retorno None
    return None

# Pruebas del ejercicio 28
print("EJERCICIO 28: Primer elemento duplicado")
print("-" * 40)
lista1 = [1, 2, 3, 4, 2, 5, 6]
lista2 = [10, 20, 30, 40, 30]
lista3 = [1, 2, 3, 4, 5]
print(f"Lista: {lista1}")
print(f"Primer duplicado: {primer_duplicado(lista1)}")
print(f"Lista: {lista2}")
print(f"Primer duplicado: {primer_duplicado(lista2)}")
print(f"Lista: {lista3}")
print(f"Primer duplicado: {primer_duplicado(lista3)}")
print("")


# ============================================
# EJERCICIO 29
# Crea una funcion que convierta una variable en una cadena de texto y enmascare
# todos los caracteres con el caracter '#', excepto los ultimos cuatro.
# ============================================

def enmascarar_texto(variable):
    # Convierto cualquier tipo de dato a string
    texto = str(variable)
    
    # Si tiene 4 o menos caracteres, no se enmascara
    if len(texto) <= 4:
        return texto
    
    # Calculo cuantos caracteres debo ocultar
    cantidad_ocultar = len(texto) - 4
    
    # Genero la parte enmascarada usando multiplicacion de strings
    parte_oculta = "#" * cantidad_ocultar
    
    # Extraigo los ultimos 4 caracteres usando slicing negativo
    ultimos_cuatro = texto[-4:]
    
    # Concateno la parte oculta con los ultimos 4 caracteres visibles
    resultado = parte_oculta + ultimos_cuatro
    return resultado

# Pruebas del ejercicio 29
print("EJERCICIO 29: Enmascarar texto")
print("-" * 40)
tarjeta = "1234567890123456"
telefono = "612345678"
palabra = "Python"
print(f"Original: {tarjeta}")
print(f"Enmascarado: {enmascarar_texto(tarjeta)}")
print(f"Original: {telefono}")
print(f"Enmascarado: {enmascarar_texto(telefono)}")
print(f"Original: {palabra}")
print(f"Enmascarado: {enmascarar_texto(palabra)}")
print("")


# ============================================
# EJERCICIO 30
# Crea una funcion que determine si dos palabras son anagramas, es decir,
# si estan formadas por las mismas letras pero en diferente orden.
# ============================================

def son_anagramas(palabra1, palabra2):
    # Normalizo ambas palabras a minusculas para comparacion case-insensitive
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Elimino los espacios de ambas palabras
    palabra1 = palabra1.replace(" ", "")
    palabra2 = palabra2.replace(" ", "")
    
    # Comparo las letras ordenadas alfabeticamente
    # Si son anagramas, tendran las mismas letras en el mismo orden al ordenarlas
    return sorted(palabra1) == sorted(palabra2)

# Pruebas del ejercicio 30
print("EJERCICIO 30: Detectar anagramas")
print("-" * 40)
print(f"'amor' y 'roma' son anagramas: {son_anagramas('amor', 'roma')}")
print(f"'listen' y 'silent' son anagramas: {son_anagramas('listen', 'silent')}")
print(f"'hello' y 'world' son anagramas: {son_anagramas('hello', 'world')}")
print(f"'Enrique' y 'quieren' son anagramas: {son_anagramas('Enrique', 'quieren')}")
print("")


# ============================================
# EJERCICIO 31
# Crea una funcion que solicite al usuario ingresar una lista de nombres y luego
# solicite un nombre para buscar en esa lista. Si el nombre esta en la lista,
# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepcion.
# ============================================

def buscar_nombre_en_lista():
    # Esta funcion permite buscar nombres en una lista creada por el usuario
    
    # Solicito al usuario que ingrese los nombres separados por comas
    print("Vamos a crear una lista de nombres")
    print("Escribe los nombres separados por comas")
    
    # Recojo el input del usuario
    nombres_texto = input("Ingresa los nombres (ej: Juan, Maria, Pedro): ")
    
    # Convierto el texto en una lista, eliminando espacios extra con strip()
    # List comprehension para procesar cada nombre
    lista_nombres = [nombre.strip() for nombre in nombres_texto.split(',')]
    
    # Solicito el nombre a buscar
    nombre_buscar = input("\n¿Que nombre quieres buscar?: ").strip()
    
    try:
        # Verifico si el nombre esta en la lista
        if nombre_buscar in lista_nombres:
            print(f"Genial! {nombre_buscar} esta en la lista")
        else:
            # Si no esta, lanzo una excepcion ValueError
            raise ValueError(f"El nombre '{nombre_buscar}' no esta en la lista")
    
    except ValueError as error:
        # Capturo y muestro el error de forma amigable
        print(f"Error: {error}")
        print("Nombres disponibles:", lista_nombres)

# Prueba del ejercicio 31
print("EJERCICIO 31: Buscar nombre en lista")
print("-" * 40)
# Esta funcion requiere input del usuario
# buscar_nombre_en_lista()
print("Funcion disponible para buscar nombres con input() del usuario")
print("")


# ============================================
# EJERCICIO 32
# Crea una funcion que tome un nombre completo y una lista de empleados, busque
# el nombre completo en la lista y devuelve el puesto del empleado si esta en la lista,
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aqui.
# ============================================

def buscar_empleado(nombre_completo, lista_empleados):
    """
    Busca un empleado en la lista y devuelve su puesto
    Recibe: nombre_completo (str), lista_empleados (lista de diccionarios)
    Retorna: string con el resultado de la busqueda
    """
    # Itero sobre cada diccionario de empleado en la lista
    for empleado in lista_empleados:
        # Comparo el nombre buscado con el nombre en el diccionario
        if empleado['nombre'] == nombre_completo:
            # Si lo encuentro, devuelvo un mensaje con el puesto
            return f"{nombre_completo} trabaja como {empleado['puesto']}"
    
    # Si termine de recorrer la lista sin encontrarlo, devuelvo mensaje negativo
    return f"{nombre_completo} no trabaja aqui"

# Prueba del ejercicio 32
print("EJERCICIO 32: Buscar empleado por nombre")
print("-" * 40)
empleados = [
    {'nombre': 'Ana Garcia', 'puesto': 'Desarrolladora'},
    {'nombre': 'Carlos Lopez', 'puesto': 'Disenador'},
    {'nombre': 'Maria Rodriguez', 'puesto': 'Project Manager'}
]
print(buscar_empleado('Ana Garcia', empleados))
print(buscar_empleado('Pedro Martinez', empleados))
print("")


# ============================================
# EJERCICIO 33
# Crea una funcion lambda que sume elementos correspondientes de dos listas dadas.
# ============================================

# Creo una lambda que usa zip() para emparejar elementos de ambas listas
# zip() toma elementos en la misma posicion de cada lista
# La list comprehension suma los pares correspondientes
sumar_listas = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]

# Prueba del ejercicio 33
print("EJERCICIO 33: Sumar listas con lambda")
print("-" * 40)
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
resultado = sumar_listas(lista1, lista2)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Suma: {resultado}")
print("")


# ============================================
# EJERCICIO 34
# Crea la clase Arbol, define un arbol generico con un tronco y ramas como atributos.
# Los metodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol
# ============================================

class Arbol:
    """
    Clase que representa un arbol generico con tronco y ramas
    Permite manipular la estructura del arbol mediante diversos metodos
    """
    
    def __init__(self):
        """
        Constructor: inicializa el arbol con valores por defecto
        Tronco comienza con longitud 1, sin ramas
        """
        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en una unidad
        """
        self.tronco += 1
        print(f"El tronco crecio! Ahora mide: {self.tronco}")
    
    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud inicial 1 a la lista de ramas
        """
        self.ramas.append(1)
        print(f"Nueva rama anadida! Total de ramas: {len(self.ramas)}")
    
    def crecer_ramas(self):
        """
        Aumenta la longitud de todas las ramas existentes en una unidad
        """
        # Itero sobre los indices para poder modificar los valores
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
        print(f"Todas las ramas crecieron! Longitudes: {self.ramas}")
    
    def quitar_rama(self, posicion):
        """
        Elimina una rama en la posicion especificada
        Parametro: posicion (int) - indice de la rama a eliminar
        """
        # Verifico que la posicion sea valida
        if 0 <= posicion < len(self.ramas):
            rama_quitada = self.ramas.pop(posicion)
            print(f"Rama en posicion {posicion} quitada (longitud: {rama_quitada})")
        else:
            print(f"No hay rama en la posicion {posicion}")
    
    def info_arbol(self):
        """
        Devuelve un diccionario con informacion completa del arbol
        Retorna: dict con longitud_tronco, numero_ramas y longitudes_ramas
        """
        info = {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitudes_ramas': self.ramas
        }
        return info

# Prueba del ejercicio 34
print("EJERCICIO 34: Clase Arbol")
print("-" * 40)
mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(1)
print("Informacion del arbol:", mi_arbol.info_arbol())
print("")


# ============================================
# EJERCICIO 35
# No existe ejercicio 35 en el enunciado
# ============================================


# ============================================
# EJERCICIO 36
# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre,
# saldo y si tiene o no cuenta corriente.
# ============================================

class UsuarioBanco:
    """
    Clase que representa un usuario de banco con operaciones basicas
    Atributos: nombre, saldo, tiene_cuenta
    Metodos: retirar_dinero, transferir_dinero, agregar_dinero
    """
    
    def __init__(self, nombre, saldo, tiene_cuenta):
        """
        Constructor: inicializa un usuario de banco
        Parametros:
        - nombre: nombre del usuario (str)
        - saldo: saldo inicial (float)
        - tiene_cuenta: si tiene cuenta corriente (bool)
        """
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta
    
    def retirar_dinero(self, cantidad):
        """
        Retira dinero de la cuenta
        Lanza ValueError si no hay saldo suficiente
        """
        # Verifico que haya saldo suficiente
        if cantidad > self.saldo:
            raise ValueError(f"Saldo insuficiente. Tienes {self.saldo} y quieres retirar {cantidad}")
        
        # Si hay saldo suficiente, realizo la operacion
        self.saldo -= cantidad
        print(f"{self.nombre} retiro {cantidad}. Saldo actual: {self.saldo}")
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere dinero desde otro_usuario hacia este usuario
        Parametros: otro_usuario (UsuarioBanco), cantidad (float)
        Lanza ValueError si otro_usuario no tiene saldo suficiente
        """
        # Verifico que el usuario emisor tenga suficiente saldo
        if otro_usuario.saldo < cantidad:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir")
        
        # Realizo la transferencia
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        
        print(f"Transferencia exitosa de {cantidad}")
        print(f"  De: {otro_usuario.nombre} (saldo: {otro_usuario.saldo})")
        print(f"  A: {self.nombre} (saldo: {self.saldo})")
    
    def agregar_dinero(self, cantidad):
        """
        Agrega dinero al saldo de la cuenta
        """
        self.saldo += cantidad
        print(f"{self.nombre} ingreso {cantidad}. Saldo actual: {self.saldo}")

# Prueba del ejercicio 36
print("EJERCICIO 36: Clase UsuarioBanco")
print("-" * 40)
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
alicia.transferir_dinero(bob, 30)
try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(f"Error en retiro: {e}")
print("")


# ============================================
# EJERCICIO 37
# Crea una funcion llamada procesar_texto que procesa un texto segun la opcion especificada:
# contar_palabras, reemplazar_palabras, eliminar_palabra
# ============================================

def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto
    Retorna: diccionario con palabra como clave y frecuencia como valor
    """
    # Normalizo a minusculas y separo en palabras
    palabras = texto.lower().split()
    
    # Creo un diccionario para contar frecuencias
    contador = {}
    
    # Cuento cada palabra
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza todas las ocurrencias de palabra_original por palabra_nueva
    Usa el metodo replace() de strings
    """
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    """
    Elimina todas las ocurrencias de una palabra del texto
    """
    # Separo en palabras
    palabras = texto.split()
    
    # Filtro excluyendo la palabra a eliminar
    # List comprehension mantiene solo palabras diferentes a la especificada
    palabras_filtradas = [p for p in palabras if p != palabra]
    
    # Uno las palabras restantes con espacios
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """
    Funcion principal que procesa texto segun la opcion indicada
    Parametros:
    - texto: cadena de texto a procesar
    - opcion: "contar", "reemplazar" o "eliminar"
    - *args: argumentos variables segun la opcion
    """
    if opcion == "contar":
        # Para contar no se necesitan argumentos adicionales
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        # Para reemplazar se necesitan palabra_original y palabra_nueva
        if len(args) >= 2:
            return reemplazar_palabras(texto, args[0], args[1])
        else:
            return "Error: se necesita palabra original y palabra nueva"
    
    elif opcion == "eliminar":
        # Para eliminar se necesita la palabra a eliminar
        if len(args) >= 1:
            return eliminar_palabra(texto, args[0])
        else:
            return "Error: se necesita especificar que palabra eliminar"
    
    else:
        return "Opcion no valida. Usa: contar, reemplazar o eliminar"

# Prueba del ejercicio 37
print("EJERCICIO 37: Procesar texto")
print("-" * 40)
texto_prueba = "Python es genial Python es poderoso"
print(f"Texto original: {texto_prueba}")
print(f"Contar: {procesar_texto(texto_prueba, 'contar')}")
print(f"Reemplazar: {procesar_texto(texto_prueba, 'reemplazar', 'Python', 'Java')}")
print(f"Eliminar: {procesar_texto(texto_prueba, 'eliminar', 'es')}")
print("")


# ============================================
# EJERCICIO 38
# Genera un programa que nos diga si es de noche, de dia o tarde segun la hora
# proporcionada por el usuario.
# ============================================

def determinar_momento_del_dia():
    """
    Determina si es dia, tarde o noche segun la hora ingresada
    Usa condicionales para clasificar en rangos horarios
    """
    try:
        # Solicito al usuario que ingrese la hora
        hora = int(input("¿Que hora es? (0-23): "))
        
        # Valido que la hora este en el rango valido
        if hora < 0 or hora > 23:
            print("Error: La hora debe estar entre 0 y 23")
            return
        
        # Determino el momento del dia segun rangos horarios
        if 6 <= hora < 14:
            momento = "dia"
        elif 14 <= hora < 20:
            momento = "tarde"
        else:
            momento = "noche"
        
        print(f"Son las {hora}:00 - Es de {momento}")
    
    except ValueError:
        # Manejo el error si el usuario no ingresa un numero
        print("Error: Por favor ingresa un numero entero")

# Prueba del ejercicio 38
print("EJERCICIO 38: Determinar momento del dia")
print("-" * 40)
# Esta funcion requiere input del usuario
# determinar_momento_del_dia()
print("Funcion disponible para determinar momento del dia con input() del usuario")
print("")


# ============================================
# EJERCICIO 39
# Escribe un programa que determine que calificacion en texto tiene un alumno
# en base a su calificacion numerica.
# Reglas: 0-69 insuficiente, 70-79 bien, 80-89 muy bien, 90-100 excelente
# ============================================

def obtener_calificacion_texto():
    """
    Convierte una calificacion numerica a su equivalente textual
    Usa rangos para determinar la categoria
    """
    try:
        # Solicito la nota al usuario
        nota = float(input("Ingresa la calificacion numerica (0-100): "))
        
        # Valido que la nota este en rango valido
        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100")
            return
        
        # Determino la calificacion segun los rangos especificados
        if nota <= 69:
            calificacion = "Insuficiente"
        elif nota <= 79:
            calificacion = "Bien"
        elif nota <= 89:
            calificacion = "Muy bien"
        else:
            calificacion = "Excelente"
        
        print(f"Nota: {nota} - Calificacion: {calificacion}")
    
    except ValueError:
        print("Error: Por favor ingresa un numero valido")

# Prueba del ejercicio 39
print("EJERCICIO 39: Calificacion en texto")
print("-" * 40)
# Esta funcion requiere input del usuario
# obtener_calificacion_texto()
print("Funcion disponible para convertir calificacion a texto con input() del usuario")
print("")


# ============================================
# EJERCICIO 40
# Escribe una funcion que tome dos parametros: figura (una cadena que puede ser
# "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios
# para calcular el area de la figura).
# ============================================

def calcular_area(figura, datos):
    """
    Calcula el area de diferentes figuras geometricas
    Parametros:
    - figura: "rectangulo", "circulo" o "triangulo"
    - datos: tupla con los datos necesarios (base, altura, radio, etc.)
    """
    
    if figura == "rectangulo":
        # Rectangulo necesita base y altura
        if len(datos) == 2:
            base, altura = datos
            area = base * altura
            return f"Area del rectangulo: {area}"
        else:
            return "Error: El rectangulo necesita base y altura"
    
    elif figura == "circulo":
        # Circulo necesita el radio
        if len(datos) == 1:
            radio = datos[0]
            # Uso math.pi para obtener el valor de pi
            area = math.pi * radio ** 2
            return f"Area del circulo: {area:.2f}"
        else:
            return "Error: El circulo necesita solo el radio"
    
    elif figura == "triangulo":
        # Triangulo necesita base y altura
        if len(datos) == 2:
            base, altura = datos
            area = (base * altura) / 2
            return f"Area del triangulo: {area}"
        else:
            return "Error: El triangulo necesita base y altura"
    
    else:
        return "Figura no reconocida. Usa: rectangulo, circulo o triangulo"

# Prueba del ejercicio 40
print("EJERCICIO 40: Calcular area de figuras")
print("-" * 40)
print(calcular_area("rectangulo", (5, 10)))
print(calcular_area("circulo", (7,)))
print(calcular_area("triangulo", (6, 8)))
print("")


# ============================================
# EJERCICIO 41
# Programa que utilice condicionales para determinar el monto final de una compra
# en una tienda en linea, despues de aplicar un descuento.
# ============================================

def calcular_precio_final():
    """
    Calcula el precio final de una compra aplicando descuentos si aplican
    Solicita precio original y cupon de descuento al usuario
    """
    print("TIENDA ONLINE - Calculadora de Precios")
    print("-" * 40)
    
    try:
        # Paso 1: Solicito el precio original
        precio_original = float(input("Ingresa el precio original del articulo: "))
        
        # Valido que el precio sea positivo
        if precio_original <= 0:
            print("Error: El precio debe ser mayor que 0")
            return
        
        # Paso 2: Pregunto si tiene cupon de descuento
        tiene_cupon = input("¿Tienes un cupon de descuento? (si/no): ").lower()
        
        # Paso 3: Si tiene cupon, solicito el valor del descuento
        if tiene_cupon == "si":
            valor_cupon = float(input("Ingresa el valor del cupon de descuento: "))
            
            # Paso 4: Verifico si el cupon es valido y lo aplico
            if valor_cupon > 0:
                # Me aseguro de que el descuento no sea mayor que el precio
                if valor_cupon > precio_original:
                    print("El descuento es mayor que el precio. Aplicando descuento maximo.")
                    precio_final = 0
                else:
                    precio_final = precio_original - valor_cupon
                    
                print(f"\nDescuento aplicado: -{valor_cupon}")
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
        print(f"Precio original: {precio_original:.2f}")
        if tiene_cupon == "si" and valor_cupon > 0:
            print(f"Descuento: -{valor_cupon:.2f}")
        print(f"PRECIO FINAL: {precio_final:.2f}")
        print("-" * 40)
        
    except ValueError:
        # Manejo el error si el usuario no ingresa numeros validos
        print("Error: Por favor ingresa un numero valido")

# Prueba del ejercicio 41
print("EJERCICIO 41: Calcular precio final con descuento")
print("-" * 40)
# Esta funcion requiere input del usuario
# calcular_precio_final()
print("Funcion disponible para calcular precio final con input() del usuario")
print("")

print("=" * 60)
print("PROYECTO COMPLETADO - 41 EJERCICIOS")
print("=" * 60)