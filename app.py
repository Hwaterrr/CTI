from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el envío del formulario
@app.route('/enviar_sugerencia', methods=['POST'])
def enviar_sugerencia():
    usuario = request.form['usuario']
    sugerencia = request.form['sugerencia']
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Conectar a la base de datos y guardar la sugerencia
    conexion = sqlite3.connect('sugerencias.db')
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            INSERT INTO sugerencias (usuario, fecha, sugerencia)
            VALUES (?, ?, ?)
        ''', (usuario, fecha, sugerencia))
        conexion.commit()
    except sqlite3.Error as e:
        return f"Error al insertar en la base de datos: {e}"
    finally:
        conexion.close()

    return redirect(url_for('index'))

@app.route('/test')
def test():
    return "La aplicación Flask está funcionando correctamente."


if __name__ == '__main__':
    app.run(debug=True)
    
