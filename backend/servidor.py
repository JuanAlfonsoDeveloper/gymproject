#menu
from conexion import conectar
import hashlib

#-- FUNCIÓN PARA REGISTRAR USUARIOS --#


def registrar_usuario():
        nombre = input("Digite su nombre: ")
        apellido = input("Digite su apellido: ")
        correo = input("Digite su correo: ")
        telefono = input("Digite su telefono ")
        contraseña = input("Digite su contraseña: ")
        direccion = input("Digite su direccion: ")
        rol = input("Digite el codigo rol: ")
        
        conexion = conectar()
        cursor = conexion.cursor()

        sql = "INSERT INTO usuario (nombre_usuario, apellido_usuario, correo_usuario, telefono_usuario, contraseña_usuario, direccion_usuario, id_rol) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        hashed_pass = hashlib.sha256(contraseña.encode()).hexdigest()
        valores = (nombre, apellido, correo, telefono, hashed_pass, direccion,  rol)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Usuario registrado correctamente")
        cursor.close()
        conexion.close()


#-- FUNCIÓN PARA LA LISTA DE PRECIOS--#

def lista_usuarios():
     conexion = conectar()
     cursor = conexion.cursor()
     sql = "SELECT id_usuario, nombre_usuario, apellido_usuario, correo_usuario, telefono_usuario FROM usuario"
     cursor.execute(sql)
     usuarios = cursor.fetchall()
     for usuario in usuarios: 
          print(usuario)
     cursor.close()
     conexion.close()
lista_usuarios()

#-- FUNCIÓN PARA EL MENU --#
def main():
    print("---Menu del servidor---")
    print("1. Registrar Usuario")
    print("2. Salir")
    print("3. Lista de Usuarios")

    opcion = input("Seleccione una opción: ")
    #Opcines del menu
    if opcion == "1": 
        registrar_usuario()
    elif opcion == "3":
        lista_usuarios()
main()


