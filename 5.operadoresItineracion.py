# Apuntes Google Colab:
# https://colab.research.google.com/drive/12gLwbSuCEk4fl2si9duS0TULoDYcHy-j

# While:
i = 1 
while i <= 10: 
  print(i) 
  i += 1 

# Comando break:
fibo_ant = 1
fibo = 1
indx = 3

print("El termino {} ocupa la posición {}".format(fibo_ant, 1))
print("El termino {} ocupa la posición {}".format(fibo, 2))

while fibo <= 500000:
  temp = fibo
  fibo = fibo + fibo_ant
  fibo_ant = temp

  print("El termino {} ocupa la posición {}".format(fibo, indx))

  if indx == 20:
    break
  
  indx+= 1

# Combinacion While... else:
i = 10
print("Cuenta atras")

while i >= 0:
  print(i)
  i -= 1
else:
  print("Fin de la cuenta atras")

# Bucle For:
s = "Un string no deja de ser una coleccion de objetos en Python"

for c in s:
  print(c)

# Funcion range(start, stop, step):
# Poemos poner solo un valor, que será el valor de parada. Si ponemos dos valores, serán start y stop.
for i in range(1, 11, 1):
  print(i)

for i in range(10, 0, -1):
  print(i)

for i in range(5):
  print(i)

for i in range(1, 11):
  print(i)

# Comando continue:
# Similar al break pero en lugar de salir del bucle, interrumpe la iteración en curso y empezar la siguiente.
for i in range(10):
  if i % 2 == 0 or i % 5 == 0:
    continue
  print(i)

# Bucles anidados:
for i in range(1, 11):
  print("\nTabla de multiplicar del {}".format(i))
  
  for j in range(1,11):
    print("{} x {} = {}".format(i, j, i * j))