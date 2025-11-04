# Determinar el porcentaje de descuento que corresponde según el monto de compra de un cliente:

# Si el monto es mayor o igual a 100000 el descuento será del 20%
# Si el monto es mayor o igual a 50000 pero menor de 100000 el descuento será del 10%
# Si el monto es mayor o igual a 10000 y menor a 50000 el descuento será del 5%
# si el monto es menor a 10000 no habrá descuento

# Como dato de entrada el programa pedirá el monto de la compra y como dato de salida, el monto del descuento y el precio final a pagar. 

monto_compra = int(input("Ingrese el monto de la compra: "))
monto_a_pagar = monto_compra
descuento = 0

'''
if monto_compra >= 100000:
    descuento = monto_compra * 20 / 100
    monto_a_pagar = monto_compra - descuento
    print(f"El descuento es de {descuento} y el monto a pagar es {monto_a_pagar}")
elif monto_compra >= 50000:
    descuento = monto_compra * 10 / 100
    monto_a_pagar = monto_compra - descuento    
    print(f"El descuento es de {descuento} y el monto a pagar es {monto_a_pagar}")
elif monto_compra >= 10000:
    descuento = monto_compra * 5 / 100
    monto_a_pagar = monto_compra - descuento    
    print(f"El descuento es de {descuento} y el monto a pagar es {monto_a_pagar}")
else:
    print(f"El descuento es de {descuento} y el monto a pagar es {monto_a_pagar}")
'''


if monto_compra >= 100000:
    porc_descuento = 20 
elif monto_compra >= 50000:
    porc_descuento = 10 
elif monto_compra >= 10000:
    porc_descuento = 5 
else:
    porc_descuento = 0 
    
descuento = monto_compra * porc_descuento / 100 
monto_a_pagar = monto_compra - descuento     


print(f"El descuento es de {descuento} y el monto a pagar es {monto_a_pagar}")


