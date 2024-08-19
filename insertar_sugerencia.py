import sqlite3
from datetime import datetime

# Conectarse a la base de datos
conexion = sqlite3.connect('sugerencias.db')
cursor = conexion.cursor()

# Datos de ejemplo para insertar
usuario = "Juan"
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sugerencia = "Me gustaría que el sitio tuviera un modo oscuro."

try:
    # Insertar la sugerencia en la tabla
    cursor.execute('''
        INSERT INTO sugerencias (usuario, fecha, sugerencia)
        VALUES (?, ?, ?)
    ''', (usuario, fecha, sugerencia))

    # Confirmar los cambios
    conexion.commit()
    print("Sugerencia insertada exitosamente.")
except sqlite3.Error as e:
    print(f"Error al insertar en la base de datos: {e}")
finally:
    # Cerrar la conexión
    conexion.close()
