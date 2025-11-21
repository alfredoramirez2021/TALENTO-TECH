# Creando una base de datos llamada inventario.db y dentro una tabla de productos

import sqlite3
conexion = sqlite3.connect("inventario.db")
print("Conexión establecida exitosamente.")

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL)
''')
conexion.commit()



conexion.close()