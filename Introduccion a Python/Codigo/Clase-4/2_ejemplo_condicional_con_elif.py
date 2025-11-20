# Ejercicio Planteo 3)

# Determinar y mostrar la clasificación de un estudiante según su nota:

# Si la nota es mayor o igual a 9 deberá imprimir "Excelente"
# Si la nota es mayor o igual a 7 (7 u 8) imprimir "Muy bueno"
# Si la nota es igual o mayor a 4 imprimir "Bueno"
# Si la nota es menor a 4 imprimir "Desaprobado"

nota =  int (input("Ingrese nota: \n"))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bueno")
elif nota >= 4:
    print("Bueno")
else:
    print("Desaprobado")        