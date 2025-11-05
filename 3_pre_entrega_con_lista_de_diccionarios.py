# Código de la pre-entrega desarrollado el 14 de octubre en Clase

productos = [
               {
               "nombre":"Peine", "categoria": "Higiene", "precio":1200
               }
               ,    
               {
                "nombre":"Crema", "categoria":"Estética", "precio":7000
               }
               ,
               {
                 "nombre": "Jabon de Tocador" , "categoria": "Higiene", "precio": 2000
               }
            ]

print("\nSistema de Gestión Básica De Productos\n")

print("1. Agregar producto")
print("2. Mostrar productos")
print("3. Buscar producto")
print("4. Eliminar producto")
print("5. Salir\n")

opcion = int(input("Ingrese la opción deseada: "))

while opcion != 5:
    if opcion == 1:
        print("\nAlta de Producto\n")
        
        # Agregar un producto
        nombre = input("Ingrese el nombre del producto: ").strip()        
        categoria = input("Ingrese la categoría del producto: ").strip() 
        precio = input("Ingrese el precio del producto: ").strip() 
        
        if nombre == "" or categoria == "" or precio == "":
            print("Ningún campo puede estar vacío")
        else:
            precio = int(precio)
            productos.append({"nombre": nombre , "categoria":categoria, "precio": precio})

    elif opcion == 2:

        print("\nListado de productos\n")  
        
        for i in range(0,len(productos),1):
            print("Número de producto:", i)
            print("Nombre del producto:", productos[i]["nombre"])
            print("Categoria:", productos[i]["categoria"])
            print("Precio:", productos[i]["precio"])
            print("")

    elif opcion == 3:
        print("\nBúsqueda de un Producto\n")
        
        producto_buscado = input("Ingrese el nombre del producto que desea consultar: ").strip()
              
        for producto in productos:    
            if producto["nombre"].lower() == producto_buscado.lower():
                print(f"Nombre del producto: ${producto["nombre"]}")
                print("Categoria:", producto["categoria"])
                print("Precio:", producto["precio"])
                
                break 
        else:
            print("\nEl producto buscado no está en la lista\n")
        
    elif opcion == 4:
        print("\nBaja de Producto\n") 

        indice = int(input("Ingrese el número de producto que desea eliminar"))

        if indice >= 0 and indice < len(productos):
            productos.pop(indice)
            print("El producto ha sido eliminado")
        else:  
            print("Producto inexistente")  

    else: 
        print("Ingresó una opción incorrecta")          
        
    print("\nSistema de Gestión Básica De Productos\n")

    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir\n")

    opcion = int(input("Ingrese la opción deseada: "))


print("Gracias por usar la aplicación")
    