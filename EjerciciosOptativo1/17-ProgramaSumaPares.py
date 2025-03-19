#Números pares.
#Mostrar la suma y la cantidad de números pares comprendidos 
# entre dos números ingresados por teclado
print("**Suma y Contador de Números Pares**")
num1 = int(input("Introduce el 1er número: "))
num2 = int(input("Introduce el 2do número: "))

suma_par = 0 
cont_par = 0

if num1 > num2:
    print("El 1er número debe de ser igual o menor que el 2do.")
else:
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            suma_par += num
            cont_par += 1

    print(f"La suma de los números pares entre {num1} y {num2} es: {suma_par}")
    print(f"La cantidad de números pares entre {num1} y {num2} es: {cont_par}")