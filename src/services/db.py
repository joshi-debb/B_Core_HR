import pymysql
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener las variables de entorno
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', 3306))  # Por defecto el puerto 3306
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

#conexión a la base de datos
def connect():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor  # Esto permite obtener resultados como diccionarios
        )
        return conn
    except Exception as e:
        print("Error de conexión a MySQL:", e)
        return None
    
#funcion para probar la conexion
def test_connection():
    conn = connect()
    if conn is not None:
        print("Conexión exitosa")
        conn.close()
    else:
        print("Error de conexión")

def insert_personal_data(firstName, lastName, dpi, nit, phone, email, age, gender):
    conn = connect()
    if conn is not None:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO personal_data (firstName, lastName, dpi, nit, phone, email, age, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (firstName, lastName, dpi, nit, phone, email, age, gender))
        conn.commit()
        conn.close()
        return True
    return False

def get_empleados():
    conn = connect()
    if conn is not None:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM personal_data")
            empleados = cursor.fetchall()
            # print(empleados)
        conn.close()
        return empleados
    return []

def get_empelado():
    conn = connect()
    if conn is not None:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM personal_data WHERE id = %s", (id,))
            empleado = cursor.fetchone()
        conn.close()
        return empleado
    return None

