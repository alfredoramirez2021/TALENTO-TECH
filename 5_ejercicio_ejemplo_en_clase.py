# Condiciones para jubilarse

# Para jubilarse
# Si es F tiene que tener 60 años o más 
# Si es M tiene que tener 65 años o más

genero = input("Ingrese su género (M masculino / F Femenino): ")
edad = int(input("Ingrese su edad: "))
años_aporte = int(input("Ingrese la cantidad de daños aportados")) 

if ((genero == "F" and edad >= 60) or (genero == "M" and edad >= 65)) and (años_aporte >= 30):
    print("Puede jubilarse")
else:
    print("No puede jubilarse")    
