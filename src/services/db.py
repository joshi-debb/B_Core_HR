import pymysql
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener las variables de entorno
DB_HOST = os.getenv('HOSTDB')
DB_PORT = int(os.getenv('DB_PORT', 3306))  # Por defecto el puerto 3306
DB_USER = os.getenv('USERDB')
DB_PASSWORD = os.getenv('PASSWORDDB')
DB_NAME = os.getenv('SHEMADB')

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