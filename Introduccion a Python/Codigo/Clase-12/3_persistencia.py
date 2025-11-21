# Escribir nombres

archivo = open("nombres.txt", "w", encoding = "utf-8")
archivo.write("María\n")
archivo.write("Carlos\n")
archivo.write("Lucía\n")
archivo.close()

# Leer y mostrar los nombres

archivo = open("nombres.txt", "r", encoding = "utf-8")
print("Contenido del archivo:")
for linea in archivo:
    print(linea.strip())
archivo.close()
