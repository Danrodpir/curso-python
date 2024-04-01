# Documento Google Colab del curso:
# https://colab.research.google.com/drive/1GedWsyCSvbU0CWYt5skHtA-HOVw3On7m#scrollTo=z_7YiTa_JJBl 

# Tipo de un string:
cadena = "El string se puede poner con comillas dobles o simples"
type(cadena)

# String Literals:
# \\	Backslash, \
# \'	Comilla simple, '
# \"	Comilla doble, "
# \n	Salto de línea
# \t	Tabulación horizontal

# Todos los literales en: https://docs.python.org/3.7/reference/lexical_analysis.html#string-and-bytes-literals

# Concatenar strings:
c1 = "Bienvenido a "
c2 = "Python"
c1 + c2

# Repetición de strings:
cadena = "¿Falta mucho? "
cadena * 5

# Print:
print(cadena)
print(cadena + " y añadidos")
print(cadena, "y añadidos")    # La "," funciona igual que el "+" pero añade un espacio en blanco.
print(cadena * 5)              # print() permite la repetición de strings.

# str():
# No se puede concatenar una variable numerica en un string, así que con esta función podemos unirlas sin errores.
nombre = "María"
edad = 22
print("Mi hermana se llama " + nombre + " y su edad es " + str(edad))

# .format():
# Agrupa todas las variables en el metodo y lo coloca en una cadena, sustituyendo consecutivamente parejas de {}.
nombre = "Alicia"
numero_gatos = 2
print("Mi amiga se llama {} y tiene {} gatos.".format(nombre, numero_gatos))

# Substring;
s = "Soy fan de los videojuegos"
s[0]     # Muestra el primer caracter.
s[5]     # Muestra el sexto caracter.
s[-1]    # Muestra el último caracter.
s[-7]    # Muestra el séptimo caracter empezando por el final.
s[4:7]   # Muestra del quinto al septimo elemento.
s[:7]    # Muestra del primer al septimo elemento.
s[8:]    # Muestra del noveno al último elemento.
s[-10:]  # Muestra los diez últimos elementos.
s[:-10]  # Muestra desde el principio hasta el decimo último elemento.

# Otros metodos:
s = "Me ENCANTA leer"
s.lower()                        # 'me encanta leer'
s.upper()                        # 'ME ENCANTA LEER'
s.count("e")                     # 3
s.capitalize()                   # 'Me encanta leer'
s.title()                        # 'Me Encanta Leer'
s.swapcase()                     # 'mE encanta LEER'
s.replace("Me ENCANTA", "ODIO")  # 'ODIO leer'
s.split(" ")                     # ['Me', 'ENCANTA', 'leer']
len(s)                           # 15
s.startswith("m")                # False
s.endswith("r")                  # True

# isalnum() evalua si el string que le pasas solo tiene mayúsculas, minúsculas y números:
s = "Farenhein451"
s.isalnum()

# isalpha() evalua si el string que le pasas solo tiene mayúsculas y minúsculas:
s = "Dune"
s.isalpha()

# isdigit() evalua si el string que le pasas solo tiene números:
s = "2546897"
s.isdigit()

# isspace() evalua si el string que le pasas solo tiene espacios:
s = "       "
s.isspace()

# islower() e isupper() evalua si el string que le pasas esta en minúscula y mayusculas, respectivamente (ignora espacios en blanco):
s = "Todo arde"
s.islower()
s.isupper()

# istitle() evalua si cada palabra empieza en mayúscula y el resto en minúsculas (ignora espacios en blanco):
s = "El Señor De Los Anillos"
s.istitle()

# El metodo .find() y el metodo .index() tienen dos parametros opcionales, start y end, para indicar donde queremos que empiece la busqueda y donde queremos que acabe.
# Ambos funcionan de la misma manera, excepto al devolver un error: .index() devuelve "error", mientras que .find() devuelve -1.
s.find("leer")                   # 11
s.find("e", 3)                   # 12
s.find("e", 1, 5)                # 1

s.index("leer")                  # 11
s.index("e", 3)                  # 12
s.index("e", 1, 5)               # 1

# .rindex() busca el caracter indicado, mostrando la última opción:
s.rindex("leer")                  # 11
s.rindex("e", 3)                  # 13
s.rindex("e", 1, 5)               # 1

s = "    Me ENCANTA leer    "
s.lstrip()                       # 'Me ENCANTA leer    '
s.strip()                        # 'Me ENCANTA leer'
s.rstrip()                       # '    Me ENCANTA leer'

# input():
print("Introduce tu nombre:")
name = input()

print("Introduce tu edad:")
age = int(input())

print("Introduce tu altura:")
height = float(input())

print("La edad de {} es {} y mide {}m".format(name, age, height))