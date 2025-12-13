# PROYECTO LÓGICA: Katas de Python

## Introducción

Este proyecto forma parte del **módulo de Python** del bootcamp de **Data & Analytics**. Consiste en la resolución de **41 katas** (ejercicios de programación) que abarcan los conceptos fundamentales del lenguaje.

Como estudiante **sin experiencia previa en programación**, este proyecto ha sido un reto importante. Durante su desarrollo he tenido que investigar, practicar y revisar conceptos varias veces hasta conseguir que funcionaran correctamente.

---

## ¿Qué es una Kata?

Una kata en programación es un ejercicio práctico diseñado para mejorar habilidades de codificación mediante la práctica repetida. El término proviene de las artes marciales, donde las katas son secuencias de movimientos que se practican hasta dominarlas. En este contexto, cada kata representa un problema específico que debe resolverse aplicando conceptos de Python.

---

## Objetivos del Proyecto

El objetivo principal es resolver las 41 katas propuestas, demostrando conocimientos en:

- Manejo de **tipos de datos básicos** y funciones incorporadas
- Estructuras de datos en Python (**listas, diccionarios, tuplas, sets**)
- **Condicionales** y estructuras de control
- **Bucles** e iteraciones
- **Funciones** y funciones **lambda**
- **Programación orientada a objetos** (Clases)
- **Manejo de excepciones**
- Uso de funciones avanzadas: **map()**, **filter()**, **reduce()**
- **Buenas prácticas** de programación

---

## Estructura del Repositorio

```
proyecto-logica-python/
│
├── Proyecto.py                         # Archivo principal con los 41 ejercicios
├── README.md                           # Documentación del proyecto
└── EnunciadoDataProjectPython.pdf     # Enunciados originales
```

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Editor:** Visual Studio Code
- **Módulos importados:**
  - `functools` (para la función reduce)
  - `math` (para cálculos geométricos)

---

## Cómo Ejecutar el Proyecto

**1. Clonar el repositorio:**
```bash
git clone [URL-de-tu-repositorio]
```

**2. Verificar la instalación de Python** (versión 3.x recomendada):
```bash
python --version
```

**3. Ejecutar el archivo principal:**
```bash
python Proyecto.py
```

**4. Interacción con el usuario:** Algunos ejercicios (**11, 31, 38, 39, 41**) requieren entrada de datos por teclado. Seguir las instrucciones que aparecen en consola.

---

## Resumen de los Ejercicios

### Ejercicios 1-10: Fundamentos
- Frecuencias de letras en texto
- Uso de **map()** para transformar listas
- Filtrado de palabras
- Cálculo de diferencias entre listas
- Promedios y estados (aprobado/suspenso)
- **Recursividad** (factorial)
- Conversión de tuplas a strings
- **Manejo de excepciones** (división)
- Filtrado con **filter()** (mascotas)
- **Excepciones personalizadas**

### Ejercicios 11-20: Funciones Avanzadas
- Validación de edad con excepciones
- Longitud de palabras
- Mayúsculas y minúsculas
- Filtrado por letra inicial
- **Funciones lambda** básicas
- Palabras más largas que n
- Conversión de dígitos a número
- Filtrado de estudiantes
- Números impares
- Filtrado de tipos de datos

### Ejercicios 21-30: Operaciones Complejas
- Cálculo del cubo con **lambda**
- Producto total con **reduce()**
- Concatenación con **reduce()**
- Diferencia total con **reduce()**
- Conteo de caracteres
- Resto de división con **lambda**
- Cálculo de promedios
- Búsqueda de duplicados
- Enmascaramiento de texto
- Detección de **anagramas**

### Ejercicios 31-37: Programación Orientada a Objetos
- Búsqueda en listas con excepciones
- Búsqueda de empleados
- Suma de listas con **lambda**
- **Clase Arbol** (con métodos)
- **Clase UsuarioBanco** (con transferencias)
- Procesamiento de texto (múltiples funciones)

### Ejercicios 38-41: Condicionales y Validación
- Determinación de momento del día
- Calificaciones (numérico a texto)
- Cálculo de áreas geométricas
- Sistema de descuentos en tienda

---

## Proceso de Aprendizaje

### Principales Dificultades Encontradas

**Funciones lambda:** Inicialmente me resultó complicado entender su sintaxis y aplicación práctica. Después de varios intentos y ejemplos, comprendí que son útiles para operaciones breves que no requieren una función completa.

**Recursividad:** El concepto de una función que se invoca a sí misma no fue intuitivo al principio. El ejercicio del factorial requirió múltiples revisiones hasta entender correctamente el **caso base** y el **caso recursivo**.

**Map, Filter y Reduce:** Estas funciones de orden superior presentaron dificultad porque requieren pensar de forma diferente a los bucles tradicionales. Fue necesario consultar varios ejemplos y practicar con casos distintos para dominarlas.

**Programación Orientada a Objetos:** Las clases `Arbol` y `UsuarioBanco` fueron especialmente desafiantes. El uso de `self` y la estructura de métodos dentro de una clase requirieron bastante práctica. Tuve que revisar la teoría varias veces para implementarlas correctamente.

**Manejo de Excepciones:** Saber cuándo y cómo utilizar `try-except` no fue obvio desde el principio. Entender la diferencia entre excepciones estándar y personalizadas llevó tiempo.

### Conceptos Mejor Asimilados

Los **bucles for y while** resultaron intuitivos desde el inicio. Las estructuras de datos básicas (**listas, diccionarios**) y los **condicionales if-elif-else** se comprendieron con relativa facilidad. La manipulación de strings también fue accesible después de practicar con los primeros ejercicios.

### Errores y Correcciones

Durante el desarrollo encontré varios problemas:
- Al principio olvidé importar el módulo `math` para el ejercicio del círculo, lo que me generó errores de ejecución.
- En algunos ejercicios confundí la lógica para números **pares e impares**.
- Tuve problemas de codificación con caracteres especiales (ñ, tildes) en los comentarios.


---

## Recursos Consultados

Para la realización de este proyecto he consultado:
- **Documentación oficial de Python** (python.org)
- **Stack Overflow** para resolver dudas específicas y ver ejemplos prácticos
- **Tutoriales en vídeo** sobre conceptos que requerían mayor clarificación
- **Foros de programación** donde otros estudiantes compartían soluciones similares

---

## Notas sobre el Código

He incluido **comentarios detallados** en el código para explicar el razonamiento detrás de cada solución. Los comentarios están escritos en **primera persona** para reflejar mi proceso de aprendizaje durante el desarrollo del proyecto.

Aunque algunos ejercicios podrían optimizarse, funcionan correctamente y cumplen con los requisitos establecidos. El código refleja mi nivel actual de conocimiento en Python.

---

## Notas Importantes

- **Ejercicio 35:** Este ejercicio no aparece en el documento de enunciados proporcionado.
- **Interacción del usuario:** Los ejercicios **11, 31, 38, 39 y 41** requieren entrada de datos por consola durante su ejecución.
- **Errores en el proceso:** Algunos ejercicios pueden contener pequeños errores lógicos que forman parte del proceso natural de aprendizaje.

---

## Próximos Pasos

Tras completar este proyecto, los siguientes objetivos de aprendizaje incluyen:
- Profundizar en **programación orientada a objetos** y patrones de diseño
- Explorar módulos avanzados de Python para análisis de datos (**NumPy, Pandas**)
- Aplicar estos conocimientos en proyectos de **análisis de datos reales**
- Mejorar la **eficiencia y legibilidad** del código mediante mejores prácticas

---

**Fecha de entrega:** Diciembre 2025  
**Bootcamp:** Data & Analytics  

---

Este proyecto marca mi primera aproximación seria a la programación en Python. Aunque queda mucho camino por recorrer, considero que he logrado comprender los **fundamentos necesarios** para continuar desarrollando mis habilidades como futuro **Analista de Datos**.