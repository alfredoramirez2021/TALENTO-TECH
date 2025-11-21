import sqlite3
conexion = sqlite3.connect("inventario.db")
print("Conexión establecida exitosamente.")

cursor = conexion.cursor()

cursor.execute('SELECT * FROM productos')

productos = cursor.fetchall()

for producto in productos:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")
    

conexion.commit()

conexion.close()    