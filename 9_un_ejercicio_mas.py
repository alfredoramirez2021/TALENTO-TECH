usuarios = ["Ana", "Luis", "Andrés", "María", "Alejandro", "Lucía"]
letra_buscada = "L"

for nombre in usuarios:
    if nombre.startswith(letra_buscada):
        print(f"Nombre que empieza con '{letra_buscada}': {nombre}")