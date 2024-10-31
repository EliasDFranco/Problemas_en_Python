#Cajero automático.
#Crear una aplicación de cajero automático. 
# Las funciones principales del cajero automático son:
#1- Depositar.
#2- Retirar.
#3- Consultar saldo.
#4- Salir
#El saldo debe tener un valor inicial por ejemplo de 3000$. Si realizas un
#retiro se resta de tu saldo, si realizas un depósito se suma a tu saldo.
print("**CAJERO AUTOMÁTICO**")

saldo_dinero = 3000
salir = False

while not salir:
    print("1- Depositar Dinero")
    print("2- Retirar Dinero")
    print("3- Consultar saldo")
    print("4- Salir")
    opcion = input("Seleccionar una opción por favor: ")

    if opcion == "1":
        monto_dinero = float(input("Ingrese la cantidad de dinero que desea depositar: "))
        if monto_dinero > 0:
            saldo_dinero += monto_dinero
            print(f"Usted ha depositado {monto_dinero}. Tu saldo nuevo es: {saldo_dinero}")
        else:
            print("El monto ingresado debe de ser mayor a 0.")

    elif opcion == "2":
        monto_dinero = float(input("Cuánto dinero desea retirar: "))
        if 0 < monto_dinero <= saldo_dinero:
            saldo_dinero -= monto_dinero
            print(f"Usted ha retirado {monto_dinero}. Tu saldo nuevo es: {saldo_dinero}")
        else:
            print("El monto a retirar debe de ser mayor a 0 y no puede exceder el saldo disponible.")

    elif opcion == "3":
        print(f"Tu saldo actual es: {saldo_dinero}")

    elif opcion == "4":
        print("Gracias por usar el Cajero Automático!!!")
        salir = True

    else:
        print("Esta opción es inválida. Intente de nuevo.")