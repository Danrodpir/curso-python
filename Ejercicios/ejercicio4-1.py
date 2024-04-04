# Dado un string, vamos a comprobar si contiene espacios en blanco y, en caso de ser cierto, contaremos cuántos tiene:
s = "String de prueba para ejercicio de cuenta de espacios en blanco"

if s.find(" ") > 0:
    print("Espacios en blanco: {}".format(s.count(" ")))

# Solución del profesor:
s = "Mi gato mola mucho"
c =  " "

if c in s:
    print("El string tiene {} espacios en blanco".format(s.count(c)))