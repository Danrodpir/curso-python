# Apuntes Google Colab:
# https://colab.research.google.com/drive/1RD4DimyI8qm3ZXckQate3UrcdCHYWxIK

# Los diccionarios son un conjuntos de datos tipo clave: valor. Deben tener una clave única.
# Los datos se ordenan automaticamente, numericamente y luego aplfabeticamente. Esto no ocurren con
# la funciñon print():
dicc = {"Jose": 32, "Marina": 21}
print(dicc)

# Elementos de un diccionario:
dicc = {
    "names": ["Ana", "Borja", "Carmen"],
    "ages" : [31, 25, 16]
    }

dicc["names"]    # ['Ana', 'Borja', 'Carmen']
dicc["ages"]     # [31, 25, 16]
dicc.keys()      # dict_keys(['names', 'ages'])
dicc.values()    # dict_values([['Ana', 'Borja', 'Carmen'], [31, 25, 16]])
dicc.items()     # dict_items([('names', ['Ana', 'Borja', 'Carmen']), ('ages', [31, 25, 16])])


# Modificar diccionarios:
dicc = {"names": ["Ana", "Borja", "Carmen"],
        "ages": [31, 25, 16]}
        
dicc["names"] = ["David", "Emilia", "Fernando"]
dicc["ages"][2] = 36

print(dicc)

ficha_usuario = {}
print("Introduzca su nombre:")
ficha_usuario["name"] = str(input())
print("Introduzca su edad:")
ficha_usuario["age"] = int(input())
print("¿Es usted una mujer? Responda f en caso afirmativo y m en caso contrario")
ficha_usuario["gender"] = "female" if input() == "f" else "male"
print(ficha_usuario)

# Bucles con listas:
dicc = {"username": "msf",
        "name": "María",
        "age": 22,
        "city": "Palma de Mallorca"}

for key in dicc:
  print(key, ":", dicc[key])

for item in dicc.items():
  print(item)

for key, value in dicc.items():
  print(key, ":", value)

# .clear() vacia el contenido del diccionario:
dicc = {"a": 4, "b": 3, "c": 2, "d": 1}
print(dicc)

dicc.clear()
print(dicc)

# .copy() duplica el contenido de un diccionario en otro, borrando su contenido si lo hubiera:
dicc = {"a": 4, "b": 3, "c": 2, "d": 5}
dicc_copy = dicc.copy()

print(dicc_copy)

# .fromkeys() recibe como parámetros un iterable y un valor y devuelve un diccionario 
# que contiene como claves los elementos del iterable con el mismo valor ingresado. Si los parametros
# de valor están en blanco, se mostrara un "none" en su lugar:
# dicc = dict.fromkeys(["a", "b", "c", "d", "e"], [1, 2, 3, 4])
# print(dicc)

# dicc = dict.fromkeys(["a", "b", "c", "d", "e"])
# print(dicc)

# .get() recibe como parámetro una clave y devuelve el valor de dicha clave. De no existir, mostrara la respuesta "none":
# dicc = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
# print(dicc.get("a"))