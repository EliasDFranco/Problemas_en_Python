print("BIENVENIDO ALTO-DO LIST")
print(" ")
Tareas = []

while True:
    Tarea = input("Introduce una tarea para realizar por favor! (Sino, escribir salir)")
    
    if Tarea.lower() == 'salir':
       break

    Tareas.append(Tarea)

print("\n Tus tareas son: ")
for i, Tarea in enumerate(Tareas, 1):
   print(f"{i}. {Tarea}")