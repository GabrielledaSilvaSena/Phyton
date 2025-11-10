# PROYECTO LOGICA: Katas de Python
# -----------------------------------------------------------------------------
# EJERCICIO 1
# Escribe una funcion que reciba una cadena de texto como parametro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# EJERCICIO 2
# Dada una lista de numeros, obten una nueva lista con el doble de cada valor.
# Usa la funcion map()
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# EJERCICIO 3
# Escribe una funcion que tome una lista de palabras y una palabra objetivo
# como parametros. La funcion debe devolver una lista con todas las palabras
# de la lista original que contengan la palabra objetivo.
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# EJERCICIO 4
# Genera una funcion que calcule la diferencia entre los valores de dos listas.
# Usa la funcion map()
# -----------------------------------------------------------------------------

def calcular_diferencia(num1, num2):
    return num1 - num2

def diferencia_listas(lista1, lista2):
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


# -----------------------------------------------------------------------------
# EJERCICIO 5
# Escribe una funcion que tome una lista de numeros como parametro y un valor
# opcional nota_aprobado, que por defecto es 5. La funcion debe calcular la
# media de los numeros en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es asi, el estado sera "aprobado", de lo contrario,
# sera "suspenso". La funcion debe devolver una tupla que contenga la media
# y el estado.
# -----------------------------------------------------------------------------

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


# EJERCICIO 6
# ==========================================
# Escribe una función que calcule el factorial de un número de manera recursiva.

def calcular_factorial(numero):
    # Si el número es 0 o 1, el factorial es 1 (caso base)
    if numero == 0 or numero == 1:
        return 1
    else:
        # Si no, multiplicamos el número por el factorial del número anterior
        # Esto se llama recursión porque la función se llama a sí misma
        return numero * calcular_factorial(numero - 1)

# Prueba del ejercicio 6
print("=== EJERCICIO 6: Factorial ===")
resultado = calcular_factorial(5)
print(f"El factorial de 5 es: {resultado}")  # 5! = 5 x 4 x 3 x 2 x 1 = 120
print()


# ==========================================
# EJERCICIO 7
# ==========================================
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

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


# ==========================================
# EJERCICIO 8
# ==========================================
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada.

def dividir_numeros_con_ejemplos(num1, num2):
    # Versión con parámetros para poder probarla fácilmente
    try:
        # Intentamos convertir a números
        numero1 = float(num1)
        numero2 = float(num2)
        
        # Intentamos hacer la división
        resultado = numero1 / numero2
        
        # Si todo salió bien, mostramos el resultado
        print(f"✓ La división fue exitosa: {numero1} / {numero2} = {resultado}")
        
    except ValueError:
        # Si el valor no es un número
        print("✗ Error: Debes ingresar valores numéricos")
        
    except ZeroDivisionError:
        # Si intentó dividir por cero
        print("✗ Error: No se puede dividir por cero")

# Prueba del ejercicio 8
print("=== EJERCICIO 8: División con manejo de errores ===")

# Caso 1: División normal (funciona bien)
print("Caso 1: Dividir 10 entre 2")
dividir_numeros_con_ejemplos(10, 2)

# Caso 2: División por cero (error controlado)
print("\nCaso 2: Dividir 10 entre 0")
dividir_numeros_con_ejemplos(10, 0)

# Caso 3: Valor no numérico (error controlado)
print("\nCaso 3: Dividir 10 entre 'abc'")
dividir_numeros_con_ejemplos(10, "abc")

print()

# ==========================================
# EJERCICIO 9
# ==========================================
# Escribe una función que tome una lista de nombres de mascotas como parámetro
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Usa la función filter()

def filtrar_mascotas_permitidas(lista_mascotas):
    # Lista de mascotas prohibidas en España
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    # Usamos filter() para quedarnos solo con las mascotas que NO están prohibidas
    # lambda es una función pequeña que revisa si la mascota NO está en la lista de prohibidas
    mascotas_permitidas = list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))
    
    return mascotas_permitidas

# Prueba del ejercicio 9
print("=== EJERCICIO 9: Filtrar mascotas prohibidas ===")
todas_las_mascotas = ["Perro", "Gato", "Tigre", "Conejo", "Serpiente Pitón", "Hámster", "Oso"]
print(f"Lista original: {todas_las_mascotas}")
permitidas = filtrar_mascotas_permitidas(todas_las_mascotas)
print(f"Mascotas permitidas: {permitidas}")
print()


# ==========================================
# EJERCICIO 10
# ==========================================
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# Primero creamos nuestra propia excepción personalizada
class ListaVaciaError(Exception):
    # Esta es una clase que representa un error personalizado
    pass

def calcular_promedio(lista_numeros):
    # Verificamos si la lista está vacía
    if len(lista_numeros) == 0:
        # Si está vacía, lanzamos nuestro error personalizado
        raise ListaVaciaError("Error: La lista está vacía, no se puede calcular el promedio")
    
    # Si no está vacía, calculamos el promedio
    suma = sum(lista_numeros)  # Sumamos todos los números
    promedio = suma / len(lista_numeros)  # Dividimos entre la cantidad de números
    
    return promedio

# Prueba del ejercicio 10
print("=== EJERCICIO 10: Promedio con excepción personalizada ===")

# Caso 1: Lista con números (funciona bien)
numeros = [8, 7, 9, 6, 10]
try:
    resultado = calcular_promedio(numeros)
    print(f"El promedio de {numeros} es: {resultado}")
except ListaVaciaError as error:
    print(error)

# Caso 2: Lista vacía (lanza el error)
lista_vacia = []
try:
    resultado = calcular_promedio(lista_vacia)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as error:
    print(error)


# ================================================================================================
# EJERCICIO 11: Escribe un programa que pida al usuario que introduzca su edad. Si el usuario 
# ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o 
# mayor que 120), maneja las excepciones adecuadamente.
# ================================================================================================

def validar_edad():
    # Esta función le pide al usuario su edad y verifica que sea válida
    try:
        # Pedimos al usuario que escriba su edad
        edad = input("Por favor, introduce tu edad: ")
        
        # Intentamos convertir lo que escribió el usuario a un número entero
        edad_numerica = int(edad)
        
        # Verificamos que la edad esté en un rango razonable (0 a 120 años)
        if edad_numerica < 0:
            print("Error: La edad no puede ser negativa")
        elif edad_numerica > 120:
            print("Error: La edad no puede ser mayor a 120 años")
        else:
            # Si todo está bien, mostramos la edad
            print(f"Tu edad es: {edad_numerica} años")
    
    except ValueError:
        # Si el usuario escribió algo que no es un número, mostramos este error
        print("Error: Debes introducir un número válido")

# Probamos la función
print("=== Ejercicio 11: Validar edad ===")
validar_edad()
print()


# ================================================================================================
# EJERCICIO 12: Genera una función que al recibir una frase devuelva una lista con la longitud 
# de cada palabra. Usa la función map()
# ================================================================================================

def longitud_palabras(frase):
    # Esta función cuenta cuántas letras tiene cada palabra de una frase
    
    # Separamos la frase en palabras
    palabras = frase.split()
    
    # Creo una lista vacía para guardar las longitudes
    longitudes = []
    
    # Recorro cada palabra y cuento sus letras
    for palabra in palabras:
        longitudes.append(len(palabra))
    
    return longitudes

# Probamos la función
print("=== Ejercicio 12: Longitud de palabras ===")
frase_ejemplo = "Hola me llamo Gabi y estudio análisis de datos"
resultado = longitud_palabras(frase_ejemplo)
print(f"Frase: {frase_ejemplo}")
print(f"Longitudes: {resultado}")
print()


# ================================================================================================
# EJERCICIO 13: Genera una función la cual, para un conjunto de caracteres, devuelva una lista 
# de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map()
# ================================================================================================

def mayusculas_minusculas(caracteres):
    # Esta función toma letras y devuelve tuplas con versión mayúscula y minúscula
    
    # Primero eliminamos las letras repetidas usando set()
    # set() crea un conjunto sin duplicados
    letras_unicas = set(caracteres)
    
    # Usamos map() para crear una tupla (mayúscula, minúscula) para cada letra
    # lambda es una función pequeña que se escribe en una línea
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))
    
    return resultado

# Probamos la función
print("=== Ejercicio 13: Mayúsculas y minúsculas ===")
caracteres_ejemplo = "aabbccdefgh"
resultado = mayusculas_minusculas(caracteres_ejemplo)
print(f"Caracteres originales: {caracteres_ejemplo}")
print(f"Tuplas (mayúscula, minúscula): {resultado}")
print()


# ================================================================================================
# EJERCICIO 14: Crea una función que retorne las palabras de una lista de palabras que comience 
# con una letra en específico. Usa la función filter()
# ================================================================================================

def palabras_con_letra(lista_palabras, letra_inicial):
    # Esta función filtra palabras que empiezan con una letra específica
    
    # Usamos filter() para quedarnos solo con las palabras que empiezan con la letra que queremos
    # lambda verifica si la primera letra de cada palabra coincide con la letra_inicial
    palabras_filtradas = list(filter(lambda palabra: palabra[0].lower() == letra_inicial.lower(), lista_palabras))
    
    return palabras_filtradas

# Probamos la función
print("=== Ejercicio 14: Palabras que empiezan con letra específica ===")
lista_palabras = ["Manzana", "Pera", "Plátano", "Mango", "Naranja", "Melón"]
letra = "M"
resultado = palabras_con_letra(lista_palabras, letra)
print(f"Lista de palabras: {lista_palabras}")
print(f"Palabras que empiezan con '{letra}': {resultado}")
print()


# ================================================================================================
# EJERCICIO 15: Crea una función lambda que sume 3 a cada número de una lista dada.
# ================================================================================================

# Una función lambda es una función pequeña y anónima que se escribe en una línea
# En este caso, tomamos un número y le sumamos 3
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Probamos la función lambda
print("=== Ejercicio 15: Sumar 3 a cada número ===")
numeros = [1, 5, 10, 15, 20]
resultado = sumar_tres(numeros)
print(f"Lista original: {numeros}")
print(f"Sumando 3 a cada número: {resultado}")
print()


# ================================================================================================
# EJERCICIO 16: Escribe una función que tome una cadena de texto y un número entero n como 
# parámetros y devuelva una lista de todas las palabras que sean más largas que n. 
# Usa la función filter()
# ================================================================================================

def palabras_mas_largas(texto, n):
    # Esta función encuentra palabras que tienen más letras que el número n
    
    # Separamos el texto en palabras individuales
    palabras = texto.split()
    
    # Usamos filter() para quedarnos solo con palabras que tienen más de n letras
    # len(palabra) > n verifica si la palabra es más larga que n
    palabras_largas = list(filter(lambda palabra: len(palabra) > n, palabras))
    
    return palabras_largas

# Probamos la función
print("=== Ejercicio 16: Palabras más largas que n ===")
texto_ejemplo = "Python es un lenguaje de programación increíble"
n = 5
resultado = palabras_mas_largas(texto_ejemplo, n)
print(f"Texto: {texto_ejemplo}")
print(f"Palabras con más de {n} letras: {resultado}")
print()


# ================================================================================================
# EJERCICIO 17: Crea una función que tome una lista de dígitos y devuelva el número 
# correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). 
# Usa la función reduce()
# ================================================================================================

def digitos_a_numero(digitos):
    # Esta función convierte una lista de dígitos en un número completo
    # Por ejemplo: [5, 7, 2] se convierte en 572
    
    # Convierto cada dígito a string y luego los junto
    numero_texto = ""
    for digito in digitos:
        numero_texto = numero_texto + str(digito)
    
    # Convierto el texto final a número
    numero = int(numero_texto)
    
    return numero

# Probamos la función
print("=== Ejercicio 17: Convertir dígitos a número ===")
digitos = [5, 7, 2]
resultado = digitos_a_numero(digitos)
print(f"Lista de dígitos: {digitos}")
print(f"Número formado: {resultado}")
print()


# ================================================================================================
# EJERCICIO 18: Escribe un programa en Python que cree una lista de diccionarios que contenga 
# información de estudiantes (nombre, edad, calificación) y use la función filter para extraer 
# a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
# ================================================================================================

def estudiantes_excelentes(lista_estudiantes):
    # Esta función filtra estudiantes que tienen calificación de 90 o más
    
    # Usamos filter() para quedarnos solo con estudiantes que tienen calificación >= 90
    estudiantes_filtrados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))
    
    return estudiantes_filtrados

# Creamos una lista de estudiantes con sus datos
print("=== Ejercicio 18: Estudiantes con calificación >= 90 ===")
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 85},
    {"nombre": "María", "edad": 21, "calificacion": 92},
    {"nombre": "Pedro", "edad": 23, "calificacion": 78},
    {"nombre": "Laura", "edad": 20, "calificacion": 98}
]

# Filtramos los estudiantes excelentes
resultado = estudiantes_excelentes(estudiantes)
print("Estudiantes con calificación >= 90:")
for estudiante in resultado:
    print(f"  - {estudiante['nombre']}: {estudiante['calificacion']} puntos")
print()


# ================================================================================================
# EJERCICIO 19: Crea una función lambda que filtre los números impares de una lista dada.
# ================================================================================================

# Una función lambda que filtra números impares
# Un número es impar cuando al dividirlo entre 2 NO queda resto
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

# Probamos la función lambda
print("=== Ejercicio 19: Filtrar números impares ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_impares(numeros)
print(f"Lista original: {numeros}")
print(f"Solo números impares: {resultado}")
print()


# ================================================================================================
# EJERCICIO 20: Para una lista con elementos tipo integer y string obtén una nueva lista sólo 
# con los valores int. Usa la función filter()
# ================================================================================================

def filtrar_solo_numeros(lista_mixta):
    # Esta función filtra solo los números enteros de una lista que tiene números y textos
    
    # Usamos filter() con isinstance() para verificar si cada elemento es un número entero
    # isinstance(elemento, int) devuelve True si el elemento es un número
    solo_numeros = list(filter(lambda elemento: isinstance(elemento, int), lista_mixta))
    
    return solo_numeros

# Probamos la función
print("=== Ejercicio 20: Filtrar solo números enteros ===")
lista_mixta = [1, "hola", 5, "Python", 10, "datos", 15, "análisis", 20]
resultado = filtrar_solo_numeros(lista_mixta)
print(f"Lista mixta: {lista_mixta}")
print(f"Solo números: {resultado}")
print()





