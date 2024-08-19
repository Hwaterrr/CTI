import sqlite3

# Conectarse a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('sugerencias.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla de sugerencias si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sugerencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        fecha TEXT NOT NULL,
        sugerencia TEXT NOT NULL
    )
''')

# Confirmar los cambios
conexion.commit()

# Cerrar la conexión a la base de datos
conexion.close()

print("Base de datos y tabla creadas exitosamente.")
