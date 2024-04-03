# Apuntes Google Colab:
# https://colab.research.google.com/drive/1SSlL_QVF-ByqfoOHGyhdFsqWOR1SUTsU

# El valor booleano debe escribirse con la primera letra en mayuscula:
is_adult = True
type(is_adult)

# Negación de un booleano (NOT):
A = True
not A

B = False
not B

# Conjunción de booleanos (AND):
A, B = True, True
A, B = True, False
A, B = False, False
A and B
A and (not B)

# Disyuncion de booleanos (OR):
A, B = True, True
A, B = True, False
A, B = False, False
A or B

# Operadores de comparación:
7 == 7.0
7 != "7"
3.14 > 9
0.01 <= 1

# Comparaciones multples simultáneas:
edad = 17
(edad >= 16) and (edad <= 40)

# Comparaciones entre strings.
# Esta comparación es por el orden de la primera letra de cada strings. Si fuera la mismas, pasariamos a la 
# segunda y así sucesivamente:
"Mallorca" < "Dubai"
"Mallorca" >= "Madrid"

# if else/elif
# Hay que respetar los dos puntos después de la condición y la identación, si no dará error:
edad = 23
if edad > 40:
    print("Tu edad pasa del límite.")
elif edad >= 18:
    print("Tienes la edad permitida")
else:
    print("No tienes la edad permitida para entrar.")

# Operador ternario
edad = 20
print("Eres mayor de edad") if edad >= 18 else print("Eres menor de edad")