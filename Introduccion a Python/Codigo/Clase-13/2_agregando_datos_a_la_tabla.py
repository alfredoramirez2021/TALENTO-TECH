import sqlite3
conexion = sqlite3.connect("inventario.db")
print("Conexión establecida exitosamente.")

cursor = conexion.cursor()

cursor.execute('''
    INSERT INTO productos (nombre, precio)
    VALUES (?, ?)
    ''', ("Lapiz", 2500))

conexion.commit()

conexion.close()