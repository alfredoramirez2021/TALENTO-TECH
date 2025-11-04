venta = int(input("Ingrese el monto de la venta (finalice la carga con cero): "))
acum_ventas = 0

while venta != 0:
    acum_ventas = acum_ventas + venta
    venta = int(input("Ingrese el monto de la siguiente venta (finalice la carga con cero): "))
    
print("Las ventas totales fueron de", acum_ventas )   


