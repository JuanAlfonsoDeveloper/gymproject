import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_gymproyect"
        )
        return conexion
    except mysql.connector.Error as error:
        print("❌ Error de conexión:", error)
        return None
