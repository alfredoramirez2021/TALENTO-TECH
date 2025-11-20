# Código de la pre-entrega desarrollado el 14 de octubre en Clase

productos = [
                ["Peine" , "Higiene", 1200],    
                ["Crema" , "Estética", 7000],
                ["Jabon de Tocador" , "Higiene", 2000]
            ]

def agregar_producto():
    print("\nAlta de Producto\n")
        
    # Agregar un producto
    nombre = input("Ingrese el nombre del producto: ").strip()        
    categoria = input("Ingrese la categoría del producto: ").strip() 
    precio = input("Ingrese el precio del producto: ").strip() 
    
    if nombre == "" or categoria == "" or precio == "":
        print("Ningún campo puede estar vacío")
    else:
        precio = int(precio)
        productos.append([nombre, categoria, precio])
        
        
def listar_productos():        
    print("\nListado de productos\n")  
    
    for i in range(0,len(productos),1):
        print("Número de producto:", i)
        print("Nombre del producto:", productos[i][0])
        print("Categoria:", productos[i][1])
        print("Precio:", productos[i][2])
        print("")        


def buscar_producto():
    print("\nBúsqueda de un Producto\n")
    
    producto_buscado = input("Ingrese el nombre del producto que desea consultar: ").strip()
            
    for producto in productos:    
        if producto_buscado.lower() in producto[0].lower():
            print("Nombre del producto:", producto[0])
            print("Categoria:", producto[1])
            print("Precio:", producto[2])
            
            break 
    else:
        print("\nEl producto buscado no está en la lista\n")
    

def eliminar_producto():
    print("\nBaja de Producto\n") 
    
    listar_productos()

    indice = int(input("Ingrese el número de producto que desea eliminar"))

    if indice >= 0 and indice < len(productos):
        productos.pop(indice)
        print("El producto ha sido eliminado")
    else:  
        print("Producto inexistente")  


def menu_principal():
    print("\nSistema de Gestión Básica De Productos\n")

    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir\n")



### Programa Principal ###

menu_principal()
opcion = int(input("Ingrese la opción deseada: "))

while opcion != 5:
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        listar_productos()
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        eliminar_producto()
    else: 
        print("Ingresó una opción incorrecta")          
        
    menu_principal()

    opcion = int(input("Ingrese la opción deseada: "))

print("Gracias por usar la aplicación")
    