# Método count (devuelve la cantidad de elementos iguales al valor colocado como parámetro)

fruits = ['apple', 'banana', 'cherry','cherry', 'cherry']

x = fruits.count("cherry")

print(x)

# Método append (permite agregar un elemento al final de la lista)

fruits = ['apple', 'banana', 'cherry','cherry', 'cherry']

fruits.append("kiwi")

print(x)

# Metodo extend (extiendo una lista con otra)

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

# insert (permite insertar un elemento en una lista, pero eligiendo la posición)

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

# método remove permite remover un elemento especificado

productos = ["pan", "leche", "queso"]
productos.remove("pan")

print(productos)  

# Método pop elimina el último elemento de la lista y devuelve su valor

print("\nMétodo pop elimina el último elemento de la lista y devuelve su valor\n")

productos = ["pan", "leche", "queso"]

print(productos)

ultimo_producto_eliminado = productos.pop()

print(productos)

print("Ud ha eliminado el producto", ultimo_producto_eliminado)


print("\nModificando un valor de la lista\n")

productos = ["pan", "leche", "queso"]

print(productos)

productos[2] = "queso crema"

print(productos[2])

