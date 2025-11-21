archivo = open("datos.txt", "r", encoding = "utf-8")

# contenido = archivo.read()
# print(contenido)


lineas = archivo.readlines()
for linea in lineas:
    print(linea.strip())
    
archivo.close()    