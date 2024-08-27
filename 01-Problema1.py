#Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
# el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

#Pedimos que ingrese sus horas laburadas y su coste por hora.
horas = float(input("Introduce las horas que has trabajado: "))
costexhora = float(input("Introduce lo que cobras por hora: "))

#Para calcular la paga 
paga = costexhora * horas

print("Tu salario es de: ", paga)
