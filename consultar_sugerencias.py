import sqlite3

# Conectarse a la base de datos
conexion = sqlite3.connect('sugerencias.db')
cursor = conexion.cursor()

try:
    # Seleccionar todas las sugerencias
    cursor.execute('SELECT * FROM sugerencias')
    sugerencias = cursor.fetchall()

    # Mostrar las sugerencias
    for sugerencia in sugerencias:
        print(f"ID: {sugerencia[0]}, Usuario: {sugerencia[1]}, Fecha: {sugerencia[2]}, Sugerencia: {sugerencia[3]}")
except sqlite3.Error as e:
    print(f"Error al consultar la base de datos: {e}")
finally:
    # Cerrar la conexión
    conexion.close()
