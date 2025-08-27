def tomar_nombre():
    nombre_usuario = input("nombre del usuario")
    return nombre_usuario

def fecha(dato_fecha):
    aux = 2025 - dato_fecha
    print("la edad del usuario" + str(aux))

    def imprimir():
        print("fin de modulo......")

    #zona de codigo principal

    dato_nombre = tomar_nombre()
    print("nombre del usuario: " + dato_nombre )

    dato_fecha = 2006
    fecha(dato_fecha)