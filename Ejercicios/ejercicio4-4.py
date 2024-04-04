# Comprobar si un punto del plano euclidiano de la forma (x, y) pertenece o no al cuadrado unidad.
# El cuadrado unidad es el que tiene por vértices los puntos (0, 0), (0, 1), (1, 0) y (1, 1).

x = float(input("x: "))
y = float(input("y: "))

if ((x >= 0) and (x <= 1)) and ((y >= 0) and (y <= 1)) :
    print("X e Y OK")

# Solución del profesor:
x = float(input("x = "))
y = float(input("y = "))

if x >= 0 and x <= 1 and y >= 0 and y <= 1:
  print("el punto ({}, {}) se encuentra en el cuadrado unidad".format(x, y))
else:
  print("el punto ({}, {}) no pertenece al cuadrado unidad".format(x, y))