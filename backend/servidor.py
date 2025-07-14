#menu
from conexion import conectar
def main():
    print("---Menu del servidor---")
    print("1. Registrar Usuario")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")


    #Opcines del menu
    if opcion == "1":
        nombre = input("Digite su nombre: ")
        apellido = input("Digite su apellido: ")
        correo = input("Digite su correo: ")
        telefono = input("Digite su telefono ")
        direccion = input("Digite su direccion: ")
        contraseña = input("Digite su contraseña: ")
        rol = input("Digite el codigo rol: ")
        
        conexion = conectar()
        cursor = conexion.cursor()


        




main()
