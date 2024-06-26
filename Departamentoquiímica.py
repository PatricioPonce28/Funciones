def main () :
    print ("Bienvenido al Departamento de Química de la EPN")
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la constraseña: ")
    validar_contraseña(user, password)
    menu_opciones()


def validar_contraseña (user,password) :
    while user != "Admin" or password != "Secret*" :
        print ("Credenciales incorrectas")
        user = input("Ingrese el usuario: ")
        password = input("Ingrese la constraseña: ")
    print ("Credenciales correctas")

def menu_opciones ():
    while True :
        print("Bienvendio al área de Bioinformática ¿Qué deseas hacer?" )
        print("1. Conversión de grados : ")
        print("2. Salir  ")
        respuesta = int(input("Ingresa una opción para continuar (1/2): "))
        if respuesta == 1 :
            Transforamciones()
        elif respuesta == 2 :
            print ("MUCHAS GRACIAS POR SU VISITA" )
            break
        else :
            print("Opción incorrecta intente de nuevo ")
            

def Transforamciones ():
    grados_input = input("Ingresa una cantidad para la transformación: ")
    grados = float(grados_input.replace(",", "."))
    print ("Tipos de conversión: ")
    print ("1. Grados Centígrados a Fahrenheit ")
    print ("2. Grados Kelvin a Centígrados ")
    conversion = int(input("Ingresa qué tipo de conversión vas a realizar (1 o 2): "))
    if conversion == 1:
        centigrados_a_Fahrenheit = (grados * 1.8) + 32
        print(f"La conversión de los grados que ingresaste {grados}°C a Fahrenheit es: {centigrados_a_Fahrenheit:.3f}°F") 
    elif conversion == 2:
        kelvin_a_centigrados = grados - 273.15
        print(f"La conversión de los grados que ingresaste {grados}K a Centígrados es: {kelvin_a_centigrados:.3f}°C")
    else:
        print("Opción no válida")


main ()


