# Apuntes Google Colab:
# https://colab.research.google.com/drive/1kqmy1dUzM9dyss4x-YR_kVuXZ7ynhAdP#scrollTo=-59Ypfhk422D

# Las listas son un conjunto de elementos ordenados separados por comas:
lista = ["Daniel", 34, 198.3, True]
print(lista)
type(lista)

# Tamaño de una lista:
lista = [1, 2, 3, 4, 5, 6]
len(lista)

# Elementos de una lista:
nombres = ["Maria", "Juan", "Claudia", "Jorge", "Avelina"]

print(nombres[0])       # Maria
print(nombres[3])       # Jorge
print(nombres[-1])      # Ultimo elemento: Avelina
print(nombres[-3])      # Tercer elemento empezando por el final: Claudia

# [Comienzo:Fin] (el Fin no se incluye):
print(nombres[2:4])     # Claudia, Jorge
print(nombres[:3])      # Maria, Juan, Claudia
print(nombres[3:])      # Jorge, Avelina

# Modificar listas:
nombres[0] = "Marina"
nombres[3] = "Jaime"
print(nombres)

# .append() nos permite añadir nuevos elementos al final de la lista:
nombres.append("Andrea")
print(nombres)

# .insert() nos permite añadir un nuevo elemento en una posición especifica:
nombres.insert(0, "Andrés")
print(nombres)

# Bucles con listas:
for i in range(len(nombres)):
  print(nombres[i])

for nombre in nombres:
  print(nombre)

# Concatenar listas:
l1 = [True, 15, "perro"]
l2 = [False, 21, "gato"]
print(l1+l2)

# Repetición de listas:
abc = ["A", "B", "C"]
print(abc * 5)

# Listas vacias:
empty_list = []
print(empty_list)

# .count() recibe un elemento como argumento y cuenta la cantidad de veces que aparece en la lista:
numeros = [0, 1, 1, 2, 2, 2, 3, 3, 3]
counted = []

for element in numeros:
  if element not in counted:
    counted.append(element)
    print("El elemento {} aparece {} veces".format(element, numeros.count(element)))

# .extend() añade al final de la lista:
numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.extend([6])
print(numeros)
numeros.extend([7, 8])
print(numeros)
numeros.extend(range(9, 16))
print(numeros)

# .index() devuelve el indice de la primera aparicion en la lista:
numeros = [0, 1, 1, 2, 2, 2, 3, 4, 3, 4]
print(numeros.index(2))
print(numeros.index(4))

# .pop() devuelve el último elemento de la lista y lo borra de la misma:
print(numeros)
for i in range(5):
  print(numeros.pop())
  print(numeros)

# .remove() recibe como argumento un elemento y borra su primera aparición de la lista:
numeros = [1, 2, 4, 3, 4, 5, 6]
numeros.remove(4)
print(numeros)

# .reverse() devuelve la lista en orden inverso:
numeros = [-2, -1, 0, 1, 2]
numeros.reverse()
print(numeros)

# .sort() devuelve la vista en orden. También podemos ordenarla en orden inverso con reverse = True:
numeros = [0, 9, 1, 6, 3, 8, 7, 5, 2, 4]
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

# Conversión de listas:
print(range(0, 100, 1))
print(type(range(0, 100, 1)))

print(list(range(0, 100, 1)))
print(type(list(range(0, 100, 1))))

# Listas anidadas:
lista = [
  ["María", "Santos", "Fernández"],
  ["Juan", [1, 2, 3, 4, 5], 32],
  2  
]
print(lista)

print(lista[0][2])      # Fernández
print(lista[1][1][4])   # 5

# Matrices:
matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matriz)