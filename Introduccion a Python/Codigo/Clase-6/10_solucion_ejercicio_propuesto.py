# Solución del Ejercicio Propuesto en la Clase 6


# PARTE 1: Crear lista de clientes
clientes = ["Ana", "Juan", "", "Marta", "Carlos", ""]

# Recorremos la lista y mostramos nombre + posición
print("\n=== LISTADO DE CLIENTES ===\n")
for i in range(len(clientes)):
    nombre = clientes[i]
    if nombre == "":
        print(f"Cliente {i + 1}: Nombre inválido")
    else:
        print(f"Cliente {i + 1}: {nombre}")


# PARTE 2: Contar cuántos nombres válidos e inválidos hay
validos = 0
invalidos = 0

for i in range(len(clientes)):
    if clientes[i] == "":
        invalidos = invalidos + 1
    else:
        validos = validos + 1

print("\n=== RESUMEN ===\n")
print(f"Clientes válidos: {validos}")
print(f"Nombres inválidos: {invalidos}")


# PARTE 3: Crear una nueva lista solo con los nombres válidos
clientes_validos = []

for i in range(len(clientes)):
    if clientes[i] != "":
        clientes_validos.append(clientes[i])

print("\n=== CLIENTES VÁLIDOS ===\n")
for i in range(len(clientes_validos)):
    print(f"Cliente {i + 1}: {clientes_validos[i]}")
