
# El bucle while suele tener 2 formatos. 
# Uno en base a contador o variables, donde el programa terminará la ejecución del bloque de código una vez
# se cumpla una condición 

# contador = 0

# while contador < 5:
#     print(f"El contador es: {contador}")
#     contador += 1


# El otro formato se basa en un True. Este formato necesita la sentencia break para romper el bucle 
# Se suele dar una opción al usuario, tomar el valor de esa opción para que se ejecute el bloque del break
while True: 
    print("Ejecutando el programa")

    opcion = int(input("Desea terminar la ejecución del programa?: 1. Si 2.No"))

    if opcion == 2: 
        break