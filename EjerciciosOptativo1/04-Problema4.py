# Se necesita un sistema para un supermercado llamado "Super PULP FICTION", el cual dará un 30% de
# descuento a las personas que compren más de Gs150.000 y un descuento del 15% a las que compren menos de
# 100000, al cliente se le debe mostrar el total a pagar.
print("BIENVENIDO AL SUPERMERCADO PULP FICTION ")
print(" ")
monto_baseMayor = 150000
monto_baseMenor = 100000

porcentaje_descuentoMayor = 0.30
porcentaje_descuentoMenor = 0.15

compra = 0
descuento = 0
total_pagar = 0

compra = int(input("Ingresar el monto de su compra: "))

print(f"La compra total fue de: {compra} Guaranies")
if compra > monto_baseMayor:
    descuento = compra * porcentaje_descuentoMayor
    total_pagar = compra - descuento

elif compra < monto_baseMenor:
    descuento = compra * porcentaje_descuentoMenor
    total_pagar = compra - descuento
else:
    total_pagar = compra

print(f"EL descuento aplicado es: {descuento} Guaraníes")
print(f"El total a pagar es: {total_pagar} Guaraníes")

print(" ")

print("MUCHAS GRACIS POR COMPRAR AQUI")
