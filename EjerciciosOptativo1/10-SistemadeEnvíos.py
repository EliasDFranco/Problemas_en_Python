#Sistema de envíos
#Crea un programa para determinar el costo de envió de un paquete según el destino (nacional o internacional) y el peso del paquete.
#Costo tarifas:
#Nacional  10 x kilo
#Internacional  20 x kilo
#El programa debe solicitar dos valores:
#1-Destino (nacional o internacional)
#2-Peso (kilogramos) del paquete

print('***Sistema de envio***')

destino = input("Elija el destino del paquete (nacional o internacional): ").lower()
peso = float(input("Ingrese el peso de su paquete en kilogramos: "))

if destino == "nacional":
    costo_de_envio = 10 * peso

elif destino == "internacional":
    costo_de_envio = 20 * peso

else:
    print("El destino es inválido, por favor seleccione: nacional o internacional")

print(f"EL costo del envio es: {costo_de_envio} guaranies")