# # ----- Condicionales -----

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# Este tipo de funciones, los condicionales, se encuentran dentro de lo que se llama 
# "Control de flujo". 

# Se trata de funciones que van operando sobre los casos posibles de nuestro programa

# Utilizamos el if para establecer una condicion sobre el valor recibido. 
# Lo que queremos es que, si el valor cumple la regla que le hemos aplicado (edad >=18)
# ejecutara el bloque de codigo que se encuentra identado en su interior

# if edad >= 18: 
#     print(f"Hola {nombre} veo que tenes {edad} años")

# Para ejecutar un bloque de codigo si no se cumple la condicion inicial, se usa else 
# else tambien sirve para controlar errores o ingresos no deseados 
# else: 
#     print("No sos mayor de edad, no podes ingresar")



# El if en si es un bloque de 3: 

# if 

# elif 

# else 


# Ejemplo de calculadora 
numero_1 = int(input("Ingrese el numero 1: "))
numero_2 = int(input("Ingrese el numero 2: "))

opcion = int(input("Ingrese la operacion deseada: \n 1. Suma \n 2. Resta \n 3.Multiplicacion \n 4. Division"))



if opcion == 1: 
    resultado = numero_1 + numero_2
    print(f"El resultado es {resultado}")
elif opcion == 2:
    resultado = numero_1 - numero_2
    print(f"El resultado es {resultado}")
elif opcion == 3: 
    resultado = numero_1 * numero_2
    print(f"El resultado es {resultado}")
elif opcion == 4: 
    resultado = numero_1 / numero_2
    print(f"El resultado es {resultado}")
else: 
    print("La opcion seleccionada no existe")

