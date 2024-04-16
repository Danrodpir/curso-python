# Ejercicio 1
# Haz que un usuario introduzca un número real y evalúa si dicho número es positivo, negativo o cero. Devuelve
# por pantalla el resultado en cada caso.

num = float(input("Introduzca un número: "))

if num > 0:
    print("Número positivo")
elif num == 0:
    print("Cero")
elif num < 0:
    print("Número negativo")
else:
    print("No ha introducido un número correcto")

# Ejercicio 2
# Haz que un usuario introduzca su nombre y evalúa con operadores if y else si dicho nombre tiene una
# longitud mayor a 10 caracteres o no. Devuelve por pantalla el resultado en cada caso.

nombre = input("Introduzca su nombre: ")

if len(nombre) > 10:
    print("Más de 10 caracteres: ({})".format(len(nombre)))
else:
    print("igual o menos de 10 caracteres: ({})".format(len(nombre)))

# Ejercicio 3
# Realiza el ejercicio anterior con el uso del operador ternario.

nombre = input("Introduzca su nombre: ")

print("Más de 10 caracteres: ({})".format(len(nombre))) if len(nombre) > 10 else print("igual o menos de 10 caracteres: ({})".format(len(nombre)))

# Ejercicio 4
# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el primer número introducido
# por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve por pantalla el
# resultado en cada caso.
# PISTA: Asegúrate de hacer uso de la función int() donde pertoque.

num1 = int(input("Introduzca un primer número: "))
num2 = int(input("Introduzca un segundo número: "))

if num1 <= 0 or num2 <= 0:
    print("Los números deben ser positivos")
elif num1 >= num2:
    print("{} es mayor o igual a {}".format(num1, num2))
else: 
    print("{} es menor a {}".format(num1, num2))

# Ejercicio 5
# Haz que un usuario introduzca dos números enteros positivos. Suponiendo que el primer número introducido
# por el usuario es mayor o igual al segundo número introducido por el usuario, comprueba que la división del
# primer número entre el segundo número es exacta.
# En caso de la división ser exacta, devuelve el cociente por pantalla e indica que la división en efecto es exacta.
# En caso de la división no ser exacta, devuelve el cociente y el resto por pantalla e indica que la división entre
# los dos números no es exacta

num1 = int(input("Introduzca un primer número: "))
num2 = int(input("Introduzca un segundo número: "))

if num1 <= 0 or num2 <= 0:
    print("Los números deben ser positivos")
elif num1 >= num2:
    print("{} es mayor o igual a {}".format(num1, num2))
else: 
    print("{} es menor a {}".format(num2, num1))


# Ejercicio 6
# Fusiona lo hecho en los ejercicios 4 y 5 para que:
# 1. Un usuario introduzca dos números enteros por pantalla.
# 2. Comprobar si el primer número es mayor o igual al segundo número introducido por el usuario. Devolver
# por pantalla en que caso nos encontramos.
# 3. Hacer la división entera pertinente en cada caso.
# 4. Si la división es exacta, entonces devolver por pantalla el cociente e indicar que la división es exacta.
# Si la división no es exacta, entonces devolver por pantalla el cociente y el resto e indicar que la división
# realizada no es exacta.

num1 = int(input("Introduzca un primer número: "))
num2 = int(input("Introduzca un segundo número: "))

if num1 >= num2:
    print(num1 / num2)
    print("{} es mayor o igual a {}".format(num1, num2))
else: 
    print(num2 / num1)
    print("{} es menor a {}".format(num2, num1))
    

# Ejercicio 7
# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
# Devuelve por pantalla el resultado en cada caso.

# Ejercicio 8
# Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
# por pantalla el resultado en cada caso.

word = input("Incerte una palabra: ")

if word.istitle():
    print("{} empieza por mayúscula".format(word))
else:
    print("{} empieza por minúscula".format(word))

# Ejercicio 9
# Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
# de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño
# 1.
# PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones
# Ejercicio 10
# Dada una ecuación de segundo grado ax2 + bx + c = 0, sabemos que las soluciones vienen dadas por
# x =
# −b ±
# √
# b
# 2 − 4ac
# 2a
# siempre y cuando a 6= 0.
# El número de soluciones dentro del conjunto de los números reales R viene dado en función del signo
# que tome el discriminante, 4 = b
# 
# 2 − 4ac. Si 4 > 0, entonces tendremos dos soluciones diferentes en R
# x =
# −b+
# √
# 4
# 2a
# y x =
# −b−
# √
# 4
# 2a
# 
# . Si 4 = 0, entonces tendremos dos soluciones que serán iguales
# x =
# −b
# 2a
# 
# . Si
# 4 < 0, entonces no existe solución dentro del conjunto de los números reales para esta ecuación de segundo
# grado.
# Con toda esta información, haz que el usuario introduzca los valores de los coeficientes a, b, c. Con ello,
# 1. Comprueba que el coeficiente a es distinto de 0
# 2. En función del discriminante, calcula cuántas soluciones va a tener la ecuación de segundo grado
# ax2 + bx + c = 0.
# 3. Devuelve por pantalla el resultado en cada caso (tanto el número de soluciones en los números reales
# como el valor de éstas).
# PISTA: Para calcular la raíz cuadrada, vas a necesitar la función math.sqrt() de la librería math.
