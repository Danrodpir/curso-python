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