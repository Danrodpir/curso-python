# vamos a comprobar si un año es bisiesto o no.
# Un año es bisiesto si es divisible entre cuatro pero no es múltiplo de cien a no ser que los sea de 400.

year = 2025

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("El año {} es bisiesto".format(year))
    else: print("El año {} no es bisiesto".format(year))
  else: print("El año {} es bisiesto".format(year))
else: print("El año {} no es bisiesto".format(year))
 