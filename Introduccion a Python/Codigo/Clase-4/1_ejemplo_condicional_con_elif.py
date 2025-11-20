# Planteo: desarrollar un programa en el que el usuario ingrese un numero entero e imprima si es positivo, igual a cero, o negativo.

numero = int(input("Ingrese un número entero: "))

if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero")
else:  
    print("El número es negativo")
        