# Ejercicio 1
# Utiliza las funciones de concatenar, + y repetir strings, *, junto con la función print() para dados los siguientes strings s1, s2, s3 y s4, 
# conseguir el resultado siguiente: Había una vez, un barquito chiquitito.
# Había una vez, un barquito chiquitito que no podía, que no podía, que no podía navegar.
s1 = "Había una vez, "
s2 = "un barquito chiquitito "
s3 = "que no podía, "
s4 = "que no podía navegar."

print((s1+s2)*2+s3*2+s4)

# Ejercicio 2
# Utiliza la función print() y el comando de salto de línea, \n, para reproducir exactamente el siguiente texto:
# Érase un hombre a una nariz pegado,
# Érase una nariz superlativa,
# Érase una alquitara medio viva,
# Érase un peje espada mal barbado;

print("Érase un hombre a una nariz pegado,\nÉrase una nariz superlativa,\nÉrase una alquitara medio viva,\nÉrase un peje espada mal barbado;")

# Ejercicio 3
# Transforma el siguiente string s a mayúsculas y muéstralo por pantalla con la función print():
s = "me encantan las matemáticas"

print(s.upper())

# Ejercicio 4
# Calcula la longitud del string s
s = "Mi pasión por el chocolate es superior a mis fuerzas"

len(s)

# Ejercicio 5
# Del string s del ejercicio anterior, obtén el substring chocolate y guárdalo en una variable llamada s_sub.
# No vale contar, deberás hallar los índices del substring con el método .find() (o el que mejor consideres) y
# la función len().
# Finalmente, imprime tu resultado por pantalla

word = "chocolate"
c = s.find(word)+len(word)
s_sub = s[s.find(word):c]
print(s_sub)

# Ejercicio 6
# Con la función input(), indícale al usuario que introduzca su nombre y guárdalo en la variable llamada
# nombre

nombre = input("Introduzca su nombre: ")
print(nombre)

# Ejercicio 7
# Con la función input(), indícale al usuario que introduzca su apellido y guárdalo en la variable llamada
# apellido

apellido = input("Introduzca su apellido: ")
print(apellido)

# Ejercicio 8
# Con la función input(), indícale al usuario que introduzca su edad y guárdala en la variable llamada edad.
# ¡Ojo con el tipo de dato!

edad = int(input("Introduzca su edad: "))
print(edad)

# Ejercicio 9
# Con la función input(), indícale al usuario que introduzca la ciudad en la que vive y guárdala en la variable
# llamada ciudad.

ciudad = input("Introduzca su ciudad: ")
print(ciudad)

# Ejercicio 10
# Con lo hecho en los ejercicios 6, 7, 8 y 9, imprime por pantalla todos los datos introducidos por el usuario
# tal y como se muestra en el siguiente ejemplo, donde el usuario ha indicado que su nombre es María; su
# apellido, Santos; su edad, 21; y su ciudad, Palma de Mallorca.
# Su nombre es María Santos, tiene 21 años y actualmente vive en Palma de Mallorca

print("Su nombre es {} {}, tiene {} años y actualmente vive en {}".format(nombre, apellido, edad, ciudad))