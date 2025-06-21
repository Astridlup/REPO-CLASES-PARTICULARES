#Crear una calculadora que permita al usuario realizar operaciones matemáticas básicas 
# (suma, resta, multiplicación y división) entre dos números. El programa debe utilizar
#  condicionales para determinar la operación a realizar.


ingrese_numero1=int(input("Ingrese el promer numero: "))
ingrese_numero2=int(input("Ingrese el segundo numero: "))
opciones=int(input("opción 1 suma, opcion 2 resta, opcion 3 multiplicación, opcion 4 división"))
if opciones ==1: 
    resultado=ingrese_numero1 + ingrese_numero2
    print(f"La suma es:{resultado}")
elif opciones==2:
    resultado=ingrese_numero1 - ingrese_numero2
    print(f"La resta da como resultado: {resultado}")
elif opciones==3:
    resultado=ingrese_numero1 * ingrese_numero2
    print(f"La multiplicacion da: {resultado}")
elif opciones==4:
    resultado=ingrese_numero1 /ingrese_numero2
    print(f"La division es: {resultado}")
    
else:
    print("Esa opcion no existe")
