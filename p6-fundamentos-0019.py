# ==============================================================================
# EJERCICIOS DE PYTHON - EJEMPLOS PRÁCTICOS
# Archivo único listo para ejecutar en VS Code (.py)
# JESUS ARRIAGA NC= 0019
# ==============================================================================

def separador(titulo):
    print("\n" + "="*60)
    print(f" {titulo.upper()} ")
    print("="*60)


# ==============================================================================
# 1. PYTHON VARIABLES (3 Ejemplos)
# Ref: https://www.w3schools.com/python/python_variables.asp
# ==============================================================================
separador("1. Variables en Python")

# Ejemplo 1.1: Creación básica de variables (texto y números)
nombre_usuario = "Carlos"
edad_usuario = 25
print(f"Ejemplo 1.1: Nombre: {nombre_usuario}, Edad: {edad_usuario}")

# Ejemplo 1.2: Reasignación de variables y cambio de tipo
variable_dinamica = 100
print(f"Ejemplo 1.2 (antes): {variable_dinamica} - Tipo: {type(variable_dinamica)}")
variable_dinamica = "Ahora soy un texto"
print(f"Ejemplo 1.2 (después): {variable_dinamica} - Tipo: {type(variable_dinamica)}")

# Ejemplo 1.3: Casting / Conversión explícita de tipos
numero_texto = str(3)     # Convertir entero a string: '3'
numero_entero = int(3.8)   # Convertir flotante a entero: 3
numero_flotante = float(3) # Convertir entero a float: 3.0
print(f"Ejemplo 1.3: str: '{numero_texto}', int: {numero_entero}, float: {numero_flotante}")


# ==============================================================================
# 2. PYTHON MULTIPLE VARIABLES (3 Ejemplos)
# Ref: https://www.w3schools.com/python/python_variables_multiple.asp
# ==============================================================================
separador("2. Asignación Múltiple de Variables")

# Ejemplo 2.1: Asignar múltiples valores a múltiples variables en una sola línea
ciudad, pais, continente = "Madrid", "España", "Europa"
print(f"Ejemplo 2.1: {ciudad} está en {pais}, continente {continente}")

# Ejemplo 2.2: Asignar un mismo valor a múltiples variables a la vez
puntaje_jugador1 = puntaje_jugador2 = puntaje_jugador3 = 0
print(f"Ejemplo 2.2: Puntos -> J1: {puntaje_jugador1}, J2: {puntaje_jugador2}, J3: {puntaje_jugador3}")

# Ejemplo 2.3: Desempaquetado de una lista (Unpack)
frutas = ["Manzana", "Banana", "Cereza"]
f1, f2, f3 = frutas
print(f"Ejemplo 2.3: Fruta 1: {f1}, Fruta 2: {f2}, Fruta 3: {f3}")


# ==============================================================================
# 3. PYTHON DATA TYPES (3 Ejemplos)
# Ref: https://www.w3schools.com/python/python_datatypes.asp
# ==============================================================================
separador("3. Tipos de Datos (Data Types)")

# Ejemplo 3.1: Tipos numéricos y de texto (str, int, float, complex)
texto = "Hola Python"
entero = 42
decimal = 19.99
complejo = 1j
print(f"Ejemplo 3.1: Texto: {type(texto)}, Entero: {type(entero)}, Decimal: {type(decimal)}, Complejo: {type(complejo)}")

# Ejemplo 3.2: Colecciones (list, tuple, range, dict, set)
lista = ["apple", "banana"]        # Lista (mutable)
tupla = ("apple", "banana")        # Tupla (inmutable)
rango = range(5)                   # Rango de números
diccionario = {"nombre": "Ana"}    # Clave-Valor
conjunto = {"manzana", "pera"}     # Set (elementos únicos)
print(f"Ejemplo 3.2: list: {type(lista)}, tuple: {type(tupla)}, dict: {type(diccionario)}, set: {type(conjunto)}")

# Ejemplo 3.3: Tipo Booleano (bool) y NoneType
es_mayor_de_edad = True
datos_vacios = None
print(f"Ejemplo 3.3: Booleano: {es_mayor_de_edad} ({type(es_mayor_de_edad)}), Nulo: {datos_vacios} ({type(datos_vacios)})")


# ==============================================================================
# 4. ARITHMETIC OPERATORS (3 Ejemplos)
# Ref: https://www.w3schools.com/python/python_operators_arithmetic.asp
# ==============================================================================
separador("4. Operadores Aritméticos")

# Ejemplo 4.1: Suma (+), Resta (-) y Multiplicación (*)
a = 15
b = 4
print(f"Ejemplo 4.1: {a} + {b} = {a + b} | {a} - {b} = {a - b} | {a} * {b} = {a * b}")

# Ejemplo 4.2: División (/), División Entera (//) y Módulo/Residuo (%)
print(f"Ejemplo 4.2: División normal (15/4): {a / b}")
print(f"Ejemplo 4.2: División entera (15//4): {a // b}")
print(f"Ejemplo 4.2: Módulo/Residuo (15%4): {a % b}")

# Ejemplo 4.3: Exponenciación / Potencia (**)
base = 3
exponente = 4
print(f"Ejemplo 4.3: {base} elevado a la {exponente} ({base} ** {exponente}) = {base ** exponente}")


# ==============================================================================
# 5. COMPARISON OPERATORS (3 Ejemplos)
# Ref: https://www.w3schools.com/python/python_operators_comparison.asp
# ==============================================================================
separador("5. Operadores de Comparación")

x = 10
y = 20

# Ejemplo 5.1: Igualdad (==) y Desigualdad (!=)
print(f"Ejemplo 5.1: ¿{x} es igual a {y}? (x == y): {x == y}")
print(f"Ejemplo 5.1: ¿{x} es diferente de {y}? (x != y): {x != y}")

# Ejemplo 5.2: Mayor que (>) y Menor que (<)
print(f"Ejemplo 5.2: ¿{x} es mayor que {y}? (x > y): {x > y}")
print(f"Ejemplo 5.2: ¿{x} es menor que {y}? (x < y): {x < y}")

# Ejemplo 5.3: Mayor o igual (>=) y Menor o igual (<=)
limite = 10
print(f"Ejemplo 5.3: ¿{x} es mayor o igual a {limite}? (x >= limite): {x >= limite}")
print(f"Ejemplo 5.3: ¿{y} es menor o igual a {limite}? (y <= limite): {y <= limite}")


# ==============================================================================
# 6. LOGICAL OPERATORS (3 Ejemplos)
# Ref: https://www.w3schools.com/python/python_operators_logical.asp
# ==============================================================================
separador("6. Operadores Lógicos")

# Ejemplo 6.1: Operador `and` (devuelve True si AMBAS condiciones son verdaderas)
edad = 22
tiene_licencia = True
puede_conducir = (edad >= 18) and tiene_licencia
print(f"Ejemplo 6.1 (and): ¿Edad >= 18 Y tiene licencia?: {puede_conducir}")

# Ejemplo 6.2: Operador `or` (devuelve True si AL MENOS UNA condición es verdadera)
es_fin_de_semana = False
es_dias_festivo = True
hay_descanso = es_fin_de_semana or es_dias_festivo
print(f"Ejemplo 6.2 (or): ¿Es fin de semana O día festivo?: {hay_descanso}")

# Ejemplo 6.3: Operador `not` (invierte el resultado booleano)
sistema_bloqueado = False
permiso_acceso = not sistema_bloqueado
print(f"Ejemplo 6.3 (not): Sistema bloqueado = {sistema_bloqueado} -> ¿Permitir acceso? (not sistema_bloqueado): {permiso_acceso}")
print("Programa realizado por Jesus Arriaga NC = 0019")