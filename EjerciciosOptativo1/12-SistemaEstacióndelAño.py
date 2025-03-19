# Estación del año
#Se solicita proporcionar el valor de un mes (valor numérico entre 1 y 12), e indicar la estación del año según lo siguiente:
 #   • Meses 1, 2 o 12  Invierno
 #   • Meses 3, 4 y 5  Primavera
 #   • Meses 6, 7 u 8  Verano
 #   • Meses 9, 10 u 11 Otoño
 #   • Cualquier otro valor  estación desconocida

print('***Estación del año***')

mes_del_año = int(input("Ingrese el valor del mes (1 a 12): "))

estacion_del_año = None

if mes_del_año == 1 or mes_del_año == 2 or mes_del_año == 12:
   estacion_del_año = "Invierno"
elif mes_del_año == 3 or mes_del_año == 4 or mes_del_año == 5:
   estacion_del_año = "Primavera"
elif mes_del_año == 6 or mes_del_año == 7 or mes_del_año == 8:
  estacion_del_año = "Verano"
elif mes_del_año == 9 or mes_del_año == 10 or mes_del_año == 11:
   estacion_del_año = "Otoño"
else:
    
    print("Estación desconocida")

print(f"El mes número {mes_del_año} corresponde a la estación {estacion_del_año}")