#Sistema de reserva hotel
#Se solicita crear un sistema de reservación de un hotel. Se debe pedir la siguiente información al usuario:
#- Nombre del cliente
#- Días de estadía en el hotel
#- ¿Cuarto con vista al mar?
#El hotel tiene las siguientes tarifas:
#- Cuarto sin vista al mar: $150.50 por día
#- Cuarto con vista al mar: $190.50 por día
#El sistema debe calcular el costo total de la estadía dependiendo si escogió un 
#cuarto con vista al mar o no. Además de indicar si escogió un cuarto con vista al mar o no.

print('***Sistema de Reserva de Hotel***')

nombre_cliente = input("Ingrese el nombre del cliente por favor: ")
dias_de_estadia = int(input("Ingrese los días de estadía en el hotel: "))
vista_al_mar = input("¿Usted quiere un cuarto con vista al mar? (si/no): ").strip().lower()

tarifa_sin_vista = 150.50
tarifa_con_vista = 190.50

if vista_al_mar == "si": 
    tarifa = tarifa_con_vista
    vista = "con vista al mar"
else:
    tarifa = tarifa_sin_vista
    vista = "sin vista al mar"

costo_total = tarifa * dias_de_estadia  
print(f"Nombre del Cliente: {nombre_cliente}")
print(f"Los días de estadía: {dias_de_estadia}")
print(f"El cuarto es: {vista}")
print(f"El costo total de la estadía es: ${costo_total}") 