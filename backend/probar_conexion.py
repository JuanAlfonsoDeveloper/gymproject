from conexion import conectar

# Usamos la función que ya creamos
conexion = conectar()

if conexion:
    print("✅ Conexión exitosa a la base de datos.")

    # Vamos a hacer una pequeña consulta para comprobar
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES;")  # Lista todas las tablas

    tablas = cursor.fetchall()
    print("📋 Tablas existentes en la base de datos:")
    for tabla in tablas:
        print(" -", tabla[0])

    cursor.close()
    conexion.close()
else:
    print("❌ No se pudo conectar a la base de datos.")
