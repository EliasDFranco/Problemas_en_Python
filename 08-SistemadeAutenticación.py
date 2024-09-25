#Crear un sistema para validar los valores de usuario y password proporcionados.
#Se deben definir dos constantes con los valores validos de usuario y
#password. Y el sistema debe comparar los valores validos con los valores proporcionados.
#Se deben considerar 4 cosas:
#1-Usuario y password validos. Debe imprimir bienvenidos al sistema.
#2-Usuario invalido.
#3-Password invalido.
#4-Usuario y password invalidos

print('***Sistema de Autenticación***')

usuario_valido = "Elias Franco"
contraseña_valida = "Brasil123$"

usuario_ingresado = input("Ingresar su usario por favor: ")
contraseña_ingresada = input("Ingrese su contraseña por favor: ")

if usuario_ingresado == usuario_valido and contraseña_ingresada == contraseña_valida:
  print("Bienvenido al sistema de Autenticación")
elif usuario_ingresado != usuario_valido and contraseña_ingresada != contraseña_valida:
  print("El nombre de usuario y contraseña son inválidos.") 
elif usuario_ingresado != usuario_valido: 
  print("El usuario que ha ingresado es inválido")
elif contraseña_ingresada != contraseña_valida:
  print("La contraseña es inválida")