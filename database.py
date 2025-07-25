import sqlite3

DATABASE_NAME = 'tareas.db'

def crear_tabla():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                completada INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

def obtener_conexion():
    return sqlite3.connect(DATABASE_NAME)
