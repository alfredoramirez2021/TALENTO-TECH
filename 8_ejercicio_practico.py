nombre = input("Ingrese su nombre: ").title() # Solicita el nombre del usuario, convierte su primera letra a mayúscula y el resto a minúscula

apellido = input("Ingrese su apellido: ").title() # Solicita el apellido del usuario, convierte su primera letra a mayúscula y el resto a minúscula

correo = input("Ingrese su correo electrónico: ").strip().replace(" ", "") # Solicita el correo electrónico del usuario y elimina espacios en blanco al inicio, al final y en el medio

edad = int(input("Ingrese su edad: ")) # Solicita la edad del usuario y la convierte a entero

if correo.count("@") != 1:
    print("Su correo electrónico es inválido!")
elif edad <= 0:
    print("Edad no válida!")
else:
    if edad < 15:
        rango = "Niño/a"
    elif edad < 18:
        rango = "Adolescente"
    else:
        rango = "Adulto/a"
    print(f"Nombre: {nombre}\nApellido: {apellido}\nCorreo verificado: {correo}\nEdad: {edad}\nRango etario: {rango}")