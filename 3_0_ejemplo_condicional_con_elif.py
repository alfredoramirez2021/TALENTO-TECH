# Ejercicio Planteo

# Desarrolle un algoritmo que solicite al usuario el ingreso de un número del 1 al 3, e imprima ese número en letras.

numero = int(input("Ingrese un número del 1 al 4: "))

'''
if numero == 1:
    print("uno")
elif numero == 2:
    print("dos")
elif numero == 3:
    print("tres")
elif numero == 4:
    print("cuatro")
else:
    print("Ingresó un número incorrecto")    
'''

match numero:    
    case 1: print("uno")
    case 2: print("dos")
    case 3: print("tres")
    case 4: print("cuatro")
    case _: print("Ingresó un número incorrecto")
    