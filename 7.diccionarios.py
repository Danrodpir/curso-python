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

