# Modo w

archivo = open("datos.txt", "w", encoding="utf-8")
archivo.write("Hola, este es un archivo de prueba.\n")
archivo.write("Segunda linea del archivo.\n")
archivo.close()


# Modo "a" (agregar)

archivo = open("datos.txt", "a", encoding="utf-8")
archivo.write("Tercera linea del archivo.\n")
archivo.close()