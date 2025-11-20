print("\nBienvenido al sistema del Banco Python\n")

print("1. Depositos")
print("2. Transferencia")
print("3. Extracción")
print("4. Consultas")
print("5. Cerrar Sesión")

opcion = int(input("\nIngrese el número de opción: "))

while opcion != 5:

    if opcion == 1:
        print("Depositando...")
    elif opcion == 2:    
        print("Transfiriendo...")
    elif opcion == 3:    
        print("Extrayendo...")
    elif opcion == 4:    
        print("Consultando...")
    else:
        print("Opción inválida.")        

    print("\nBienvenido al sistema del Banco Python\n")

    print("1. Depositos")
    print("2. Transferencia")
    print("3. Extracción")
    print("4. Consultas")
    print("5. Cerrar Sesión")

    opcion = int(input("\nIngrese el número de opción (finalice ingresando cero): \n"))
    
print("Cerrando la sesión...")
print("Gracias por usar nuestra aplicación!")
