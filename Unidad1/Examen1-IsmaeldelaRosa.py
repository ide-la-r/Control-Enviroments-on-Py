class DemasiadosIntentos(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

contrasenia = "ismaeldelarosa"

contrarepe = input("Repite la contraseña: ")
contador = 1

try:
    if contrarepe != contrasenia:
        while contrarepe != contrasenia:
            contrarepe = input("Introduce la contraseña de nuevo: ")
            contador += 1
            if contador == 3:
                raise DemasiadosIntentos("Has superado el limite de intentos")
    else:
        print("Enhorabuena has introducido la contraseña correcta")

except Exception as e:
    print(e)