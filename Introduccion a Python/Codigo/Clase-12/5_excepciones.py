# Manejar una excepción es manejar un error en tiempo de ejecución

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe.")
    print("Verificá el nombre o la ubicación del archivo.")
else:
    print("No hubo errores")
finally:
    print("El finally se ejecuta siempre")        