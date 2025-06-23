
# Las listas en Python son estructuras que permiten guardar múltiples valores en una sola variable. 
# Son ordenadas y modificables, lo que significa que podemos recorrerlas, agregar o eliminar elementos,
#  y acceder a ellos por su posición.

# El bucle for se utiliza para recorrer secuencias, como listas. 
# En cada iteración, toma un elemento de la lista y ejecuta un bloque de código con ese valor. Es especialmente útil cuando queremos procesar o verificar cada elemento de una colección.

# En este ejemplo, usamos un for para recorrer una lista de estudiantes y preguntar si están presentes. Si lo están, se agregan a una nueva lista de estudiantes presentes.
    

# Definimos una lista con varios nombres de estudiantes
lista = ["Ana", "Paula", "Cristian", "Astrid"]

# Creamos una lista vacía para guardar los estudiantes que están presentes
estudiantes_presentes = []

# Iniciamos un bucle for que recorre cada nombre dentro de la lista original
for nombre in lista:
    
    # Mostramos un mensaje preguntando si ese estudiante está presente
    print(f"Esta {nombre} presente?")
    
    # Solicitamos al usuario que indique con un número si está presente (1) o no (2)
    opcion = int(input("1. Si 2.No \n"))

    # Si el usuario ingresó 1 (presente), agregamos el nombre del estudiante a la nueva lista
    if opcion == 1: 
        estudiantes_presentes.append(nombre)

# Mostramos un mensaje final con los nombres de los estudiantes presentes
print("Los estudiantes presentes son \n")

# Recorremos la lista de presentes y los imprimimos uno por uno
for estudiante in estudiantes_presentes: 
    print(estudiante)
