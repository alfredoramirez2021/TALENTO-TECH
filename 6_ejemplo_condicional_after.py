# Programa que verifica si una persona tiene las condiciones para poder circular

'''
edad = int(input("Ingrese su edad: "))
tiene_licencia = input("Tiene licencia de conducir (Si/No)")
antecedentes = input("Tiene antecedentes o infracciones (Si/No)")

if edad >= 18 and tiene_licencia == "Si" and antecedentes == "No":
    print("Puede conducir legalmente.")
else:
    print("No cumple los requisitos para conducir.")
'''    

# Programa que evalúa si un alumno/a aprobó la materia.
    
nota = 1
asistencia = 10
trabajo_entregado = True

if (nota >= 6 and asistencia >= 75) or trabajo_entregado == True:
    print("El alumno aprueba la materia.")
else:
    print("El alumno no aprueba.")  
    
