# Type para saber que tipo de dato es:
type(1)    # int
type(1.0)  # float

# Casteo de números. La conversión de float a int pierde la parte decimal:
float(1)  # 1.0
int(5.8)  # 5

# Operaciones:
1 + 2  # 3
4 - 2  # 2
2 * 5  # 10
6 / 5  # 1.2

# Combinar en una operación aritmetica de un int con un float deja el número resultante como un float:
1 + 2.5 # 3.5

# Cociente de división entera (//) y resto(%):
10 / 3   # 3.3333333333333335
10 // 3  # 3 
10 % 3   # 1

# Potencia:
5 ** 3     # 125
pow(5, 3)  # 125

# Números complejos:
z = 2 + 5j
z           # (2+5j)
type(z)     # complex

# complex() permite definir un número complejo. En este caso 1 es el número real, mientras que -7 es el imaginario:
z = complex(1, -7)
z                   # (1-7j)
type(z)             # complex

# Funciones para extraer la parte real y la imaginaria:
z.real  # 1.0
z.imag  # -7.0

# Operaciones de números complejos:
z1 = 2-6j
z2 = 5+4j

z1 + z2  # (7-2j)
z1 - z2  # (-3-10j)
-1 * z1  # (-2+6j)
z1 * z2  # (34-22j)

z1 = -1 - 1j
z2 = 1 - 1j

z1 / z2