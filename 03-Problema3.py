#Una juguetería tiene mucho éxito en dos de sus productos:
# payasos y autitos.
# Suele hacer venta por correo y 
#la empresa de logística les cobra por peso de cada paquete así que deben calcular
#el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
#Cada payaso pesa 300 g y cada muñeca 100 g. Escribir un programa que lea el número de payasos
#y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

weight_clowns = 300 
weight_cars = 100

clowns = int(input("How many clowns toys do you want to send my bro: "))
cars = int(input("How many cars toys do you want to send my bro: "))
total_weight = weight_cars * cars + weight_clowns * clowns

print("The total weight of the package is: " + str(total_weight))


