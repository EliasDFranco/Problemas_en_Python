#Se necesita de un sistema que reciba tres notas parciales de un alumno y en base a esto darle su promedio y 
#si el promedio es menor a 60 se le dira que está reprobado, en caso contrario dará aprobado.

print("SISTEMA NOTAS UNIVERSIDAD AMERICANA")
print(" ")
puntaje_base = 60
promedio = 0.0

nota1 = int(input("Ingrese la nota de su primer parcial: "))
print(" ")
nota2 = int(input("Ingrese la nota de su segundo parcial: "))
print(" ")
nota3 = int(input("Ingrese la nota de su tercer parcial: "))

print(f"Las notas fueron: {nota1}, {nota2}, {nota3}")

promedio = (nota1 + nota2 + nota3) / 3
if promedio <= puntaje_base:
    print("Usted ha desaprobado la materia")
elif promedio >= puntaje_base:
    print("Usted ha aprobado la materia")

print(f"El promedio de las tres parciales es:{promedio}")