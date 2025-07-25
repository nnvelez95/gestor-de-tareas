# app.py

from flask import Flask

# Creación de una instancia de la aplicación Flask
# __name__ es una variable especial en Python que obtiene el nombre del módulo actual.
# Flask lo usa para saber dónde buscar recursos como plantillas y archivos estáticos.
app = Flask(__name__)

# Definición de la ruta principal ("/")
# El decorador @app.route() le dice a Flask qué URL debe activar nuestra función.
@app.route('/')
def hola_mundo():
    """
    Esta función se ejecuta cuando alguien visita la página de inicio de nuestro sitio web.
    Devuelve un simple string que se mostrará en el navegador.
    """
    return '¡Hola, Mundo! Este es el inicio de nuestro Gestor de Tareas.'

# Punto de entrada para ejecutar la aplicación
# Este bloque de código se asegura de que el servidor de desarrollo solo se ejecute
# cuando el script es ejecutado directamente (y no cuando es importado).
if __name__ == '__main__':
    # app.run() inicia el servidor de desarrollo de Flask.
    # debug=True activa el modo de depuración, que reinicia automáticamente el servidor
    # cuando haces cambios en el código y muestra errores detallados en el navegador.
    app.run(debug=True)