# Dado un string, vamos a pedir al usuario que introduzca una palabra perteneciente a dicho string y vamos a obtener el substring 
# sin la palabra indicada por el usuario utilizando el método .find() y la función len().
s = "El camino está cerrado pero seguro que podemos encontrar una alternativa"
print("Este es el string original:", end = " ")
print(s)

print("Introduce la palabra que quieras eliminar del string original:")
word = input("Palabra: ")

idx = s.find(word)
idx
sb = s[:idx] + s[(idx + len(word) + 1):]
print(sb)