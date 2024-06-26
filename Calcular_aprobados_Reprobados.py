from os import system
nota_aprobacion=6
aprobados =0
reprobados =0

def menuOpciones (email):
    print("----------- ESCUELA POLITECNICA NACIONAL -------------")
    print(f'\n\t Bienvenido {email}')
    print("\nMenú de opciones")
    print("\t1.- Calificaciones")
    print("\t2.- Alumnos que aprobaron")
    print("\t3.- Salir")
    opcion = int(input("Ingresar opción: "))
    return opcion

def validarMailPassword(email,password):
    while (email != "profesor@epn.com" or password != "epn*"):
        print("\n--------- ERROR --------------")
        print("Credenciales incorrectas\n")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu password: ")


def validar_numero_alumnos():
    numero_alumnos = int(input(" Ingrese el número de alumnos: "))
    while numero_alumnos <=0:
                print("\n\t----------- Error ---------")
                print("\n\t El número de productos es incorrecto")
                numero_alumnos = int(input("\n Ingrese el número de alumnos: "))
    return numero_alumnos

def calcular_aprobados_reprobados(aprobados, reprobados): 
    calificaciones = [float]
    for i in range(validar_numero_alumnos):
        calificaciones = [float(input(f"Ingrese la calificación del alumno {i+1}: "))]
        aprobados, reprobados = calcular_aprobados_reprobados(calificaciones)
    return aprobados, reprobados

def calcular_calificaciones(calificaciones, nota_aprobacion):
    
    for calificacion in calificaciones:
        if calificaciones >= nota_aprobacion:
            aprobados += 1
        else:
            reprobados += 1
    return aprobados, reprobados
        

def imprimir_aprobados_reprobados(numero_alumnos, aprobados, reprobados):
    print("------- CALIFICACIONES ------------\n")
    print(f"Numero de alumnos: {numero_alumnos}")
    print(f"El numero de estudiantes que aprobaron es: {aprobados}")
    print(f"El numero de reprobados es: {reprobados}")


def main():
    print("\n ------- LOGIN - POLITECNICA --------\n")
    email = input("Ingresa tu email: ")
    password = input("Ingresa tu password: ")
    validarMailPassword(email,password)
    system("clear")
    opcion = 0
    while (opcion != 3):
        opcion = menuOpciones(email)
        if opcion == 1:
            system("clear")
            numero_alumnos = validar_numero_alumnos()
            (aprobados, reprobados)= calcular_aprobados_reprobados(aprobados, reprobados)

        elif opcion == 2:
            system("clear")
            imprimir_aprobados_reprobados(numero_alumnos, aprobados, reprobados)
        
    system("clear")
    print("Muchas gracias por utilizar nuestro sistema")

main()