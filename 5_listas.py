nombre_1 = "Juan"
nombre_2 = "Leonardo"
nombre_3 = "Mara"
nombre_4 = "Aldana"
nombre_5 = "Alina"

nombres = ["Juan", "Leonardo", "Mara", "Aldana","Alina", "Alejandro"]

# print(nombres[0])
# print(nombres[1])
# print(nombres[2])
# print(nombres[3])
# print(nombres[4])
# print(nombres[5])

# Agregar un elemento a una lista usamos el método append

nombres.append("Liliana")

# Como recorrer una lista y mostrar uno a uno sus datos

indice = 0

while indice < 7:
    print(nombres[indice])
    indice = indice + 1

