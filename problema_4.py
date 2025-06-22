# 🧮 Problema 4: Calculadora básica

#**Temas:** `float`, `string`, `input`, `print`, `if/elif/else`

#Pedile al usuario que ingrese dos números y una operación (`+`, `-`, `*`, `/`).  
#Mostrá el resultado según la operación ingresada. Si la operación no es válida, mostrá un mensaje de error.

### Ejemplo 1:

#📥 Ingrese el primer número: 10
#📥 Ingrese el segundo número: 5
#📥 Ingrese la operación (+, -, *, /): *
#📤 El resultado es: 50.0

numero1=int(input ("ingrese el primer numero:  "))
numero2=int(input ("ingrese el segundo numero:  "))

suma=(numero1+numero2)
resta=(numero1-numero2)
multiplicacion=(numero1*numero2)
division=(numero1/numero2)

opcion= input ("ingrese la operacion: +,-,*,/")

if opcion=="+":
    print(f"{suma}")
elif opcion=="-":
    print(f"{resta}")
elif opcion=="*":
    print(f"{multiplicacion}")
elif opcion=="/":
    print(f"{division}")
else:
    print("La opcion no existe")

