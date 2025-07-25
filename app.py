# app.py

from flask import Flask, request, jsonify
from database import crear_tabla, obtener_conexion
# Creación de una instancia de la aplicación Flask
# __name__ es una variable especial en Python que obtiene el nombre del módulo actual.
# Flask lo usa para saber dónde buscar recursos como plantillas y archivos estáticos.
app = Flask(__name__)
crear_tabla()  # Llamada a la función para crear la tabla de tareas en la base de datos


# Definición de la ruta principal ("/")
# El decorador @app.route() le dice a Flask qué URL debe activar nuestra función.
@app.route('/')
def hola_mundo():
    """
    Esta función se ejecuta cuando alguien visita la página de inicio de nuestro sitio web.
    Devuelve un simple string que se mostrará en el navegador.
    """
    return '¡Hola, Mundo! Este es el inicio de nuestro Gestor de Tareas.'

# Ruta para obtener todas las tareas
# Esta ruta acepta solicitudes GET y devuelve una lista de todas las tareas en formato JSON.
@app.route('/api/tareas', methods=['GET'])
def obtener_tareas():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('SELECT id, titulo, descripcion, completada FROM tareas')
    tareas = [
        {
            'id': fila[0],
            'titulo': fila[1],
            'descripcion': fila[2],
            'completada': bool(fila[3])
        } for fila in cursor.fetchall()
    ]
    conn.close()
    return jsonify(tareas)

# Ruta para crear una nueva tarea
# Esta ruta acepta solicitudes POST para agregar nuevas tareas a la base de datos.
@app.route('/api/tareas', methods=['POST'])
def crear_tarea():
    datos = request.get_json()

    # Validamos que tenga al menos un título
    if not datos or 'titulo' not in datos:
        return jsonify({'error': 'El campo "titulo" es obligatorio'}), 400

    titulo = datos['titulo']
    descripcion = datos.get('descripcion', '')

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tareas (titulo, descripcion) VALUES (?, ?)', (titulo, descripcion))
    conn.commit()
    tarea_id = cursor.lastrowid
    conn.close()

    return jsonify({
        'id': tarea_id,
        'titulo': titulo,
        'descripcion': descripcion,
        'completada': False
    }), 201

# Punto de entrada para ejecutar la aplicación
# Este bloque de código se asegura de que el servidor de desarrollo solo se ejecute
# cuando el script es ejecutado directamente (y no cuando es importado).
if __name__ == '__main__':
    # app.run() inicia el servidor de desarrollo de Flask.
    # debug=True activa el modo de depuración, que reinicia automáticamente el servidor
    # cuando haces cambios en el código y muestra errores detallados en el navegador.
    app.run(debug=True)