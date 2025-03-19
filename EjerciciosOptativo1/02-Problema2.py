#Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

quantify = float(input("How much do you want to invest: "))
interes = float(input("What is the  annual interest rate: "))
years = int(input("Years?"))

print("Final Capital: " + str(round(quantify * (interes / 100 + 1) * years, 2)))

#The round() function in Python is used to round a number to a specified value of decimal places.