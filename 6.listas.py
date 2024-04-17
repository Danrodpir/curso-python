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