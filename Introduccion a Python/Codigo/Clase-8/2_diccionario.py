mi_diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Buenos Aires"
}

print(mi_diccionario.get("nombre"))

print(mi_diccionario["nombre"])




# print(mi_diccionario)

# print(mi_diccionario["nombre"])  # Ana
# mi_diccionario["edad"] = 26
# mi_diccionario["profesión"] = "Ingeniera"

print(mi_diccionario.items())

print("")

# for clave, valor in mi_diccionario.items():
#     print(f"{clave}: {valor}")
    
print(mi_diccionario.values())    
    
for valor in mi_diccionario.values():
    print(f"{valor}")    