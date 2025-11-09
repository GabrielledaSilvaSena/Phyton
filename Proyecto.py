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

# VERSIÓN INTERACTIVA (COMENTADA)
# Si quieres probar pidiendo números al usuario, descomenta esto:
"""
def dividir_numeros_interactivo():
    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 / numero2
        print(f"✓ La división fue exitosa: {numero1} / {numero2} = {resultado}")
    except ValueError:
        print("✗ Error: Debes ingresar valores numéricos")
    except ZeroDivisionError:
        print("✗ Error: No se puede dividir por cero")

# Para usar la versión interactiva:
# dividir_numeros_interactivo()
"""


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



