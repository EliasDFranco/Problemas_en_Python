#Producto de múltiplos de 7.
#Crear un programa que solicite al usuario un número limite para utilizar los
#múltiplos de 7 contenidos desde cero hasta el numero limite y hallar el producto
#de los mismos, además mostrar un contador que deje visualizar la cantidad de
#múltiplos de 7 contenidos entre cero y el numero limite.
print("**Producto de Múltiplos de 7**")
num_limite = int(input("Introduce el número que será el límite: "))
cont = 0
producto = 1

for numero in range(0, num_limite + 1):
    if numero % 7 == 0 and numero != 0: 
        producto *= numero
        cont += 1
if cont > 0:
    print(f"El producto de los múltiplos de 7 entre 0 y {num_limite} es: {producto}")
    print(f"La cantidad de múltiplos de 7 entre 0 y {num_limite} es: {cont}")
else: 
    print("No existe ningún múltiplo de 7 en el rango que fue especificado.")