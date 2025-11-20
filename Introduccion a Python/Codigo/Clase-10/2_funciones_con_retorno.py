def calcular_cuadrado(numero):
    resultado = numero ** 2
    return resultado

numero_ingresado = int(input("Ingresá un número: "))
cuadrado = calcular_cuadrado(numero_ingresado)
print(f"El cuadrado de {numero_ingresado} es {cuadrado}")