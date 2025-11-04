# producto = ["Peine", "Cuidado Personal", 1200]


producto = {"nombre":"Peine", 
            "categoria": "Cuidado Personal",
            "precio": 1200}

print(producto["nombre"])
print(producto["precio"])

print(producto)

# Modificar el precio del producto

producto["precio"] = 1800

print(producto)

producto["proveedor"] = "Estetica Rosales"

print(producto)

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Buenos Aires",
    "hobbies": ["Ajedrez", "Guitarra", "Tenis"]
}


productos = {
   "manzana": 150,
   "banana": 120,
   "naranja": 180
}

productos = [
    {"nombre": "manzana", "cantidad": 150},
    {"nombre": "banana", "cantidad": 120}
]

productos.append({"nombre": "frutilla", "cantidad": 3500})


