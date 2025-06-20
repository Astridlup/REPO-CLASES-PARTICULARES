# ------ Tipos de datos y variables -------

# Una variable es un espacio en memoria que nosotros reservamos para guardar un dato 

# En python, las variables se escriben en minuscula.

# En caso de ser palabras largas, se alterna con snake case, que es el uso de guion bajo entre terminos. 

# Para asignar un valor a una variale, utilizamos el =. 

# En programacion, el = se usa para asignar valor. 

# Si necesitamos hacer comparacion de igualdad, usamos == 

# La estructura de la variable es la siguiente: 

# variable = "dato"

# Los datos tienen diversos tipos. Algunos son numeros enternos, otros son decimales, otros cadenas de caracteres 

# int (entero) -> 0 
# float (decimal) -> 0.5
# string (cadena de caracteres) -> "hola"

# No es lo mismo "0" que 0. 


variable_string = "hola"

variable_entero = 0

variable_float = 0.5


# Las variables pasan a ser la referencia del dato. Entonces cuando tenemos que operar con el dato, lo hacemos con el nombre de la variable que almacena el dato 


# ------ TAREA: Anotar los resultados de cada uno 
numero_1 = 17
numero_2 = 25

suma = numero_1 + numero_2 # 42

numero_1 = suma #42
numero_2 = suma + 2 #44

suma = numero_1 + numero_2 # 86

# -------- Funcion print -----------

# La funcion print sirve para mostrar por pantalla el resultado de las operaciones o los valores que queramos visualizar 

print("hola")
print(2)
print(suma)

# Las funciones son bloques de código que reutilizamos. 

# Las podemos declarar nosotros así como podemos utilizar funciones nativas del lenguaje de programación
# Las fucniones nativas de python, como print, son funciones que no hemos de crear 
# Las podemos utilizar 

# Las funciones def, por otro lado, son las funciones que nosotros creamos a lo largo del programa
# Sirven para ahorrar codigo, reutilizarlo y modularizar. Además de que son dinamicas

# Que sean dinamicas significa que le podemos pasar datos, llamados argumentos, entre sus parentesis. 

# Esos datos seran datos sueltos o variables que permitiran a la funcion operar 


# La estructura de una funcion def es su declaracion (def) su nombre de funcion (saludar) y, pegado al nombre
# parentesis, donde iran los parametros/argumentos que le serán propios

# Estos parametros son los nombres de variables que utilizaremos

# Este es el ambito donde la declaramos 
def saludar(nombre, edad, altura):
    año_actual = 2025
    año_nacimiento = año_actual - edad
    # Esto es una f-string en un print, 
    # escribimos una f antes de las comillas para ingresar variables dentro del texto 
    print(f"Hola {nombre}, ¿Cómo andas?. Se que tenes {edad} años y medis {altura}m. Naciste en el {año_nacimiento}")

saludar("German", 18, 1.73)

# Esto es un ambito de aplicacion, donde usaremos la funcion 
nombre = "Ruben"
edad = 23
altura = 1.8

saludar(nombre, edad, altura)


# ---- Combinar funciones nativas de python con nuestra funcion saludar 

# Vamos a usar la funcion input() y la funcion int()

# La funcion input permite el ingreso, por parte del usuario del programa, de datos a través de la consola 

# La particularidad de input es que, cómo parametro, va a tener el mensaje que le mostraremos al usuario 

# El dato que el usuario ingrese, quedará almacenado en la variable donde se guarda el input 
nombre = input("Ingrese su nombre: ")

# nombre va a pasar a ser igual a "Cristian"
# nombre = input("Ingrese su nombre: ")

# El usuario escribe "Cristian"

# Entonces: 
# nombre = "Cristian"

# La funcion int() convierte a numero entero el dato que se le pase.
# El problema reside en que la funcion input interpreta todo como palabra, así que con la funcion int 
# se convierte esa palabra a numero, para operar en base a él

# Esto es necesario si necesitamos hacer, por ejemplo, operaciones matematicas con los numeros que se ingresan 
# o comparaciones 
edad = input("Ingrese su edad: ") # "29"

print(type(edad))

edad = int(edad) # 29

print(type(edad))

print("Nacio en el año", 2025 - edad)

# Vamos a usar la funcion de saludar con datos ingresados a traves de input 

nombre_ingresado = input("Ingrese su nombre para el saludo: ")
edad_ingresada = int(input("Ingrese su edad para el saludo: "))
altura_ingresada = float(input("Ingrese su altura: "))

saludar(nombre_ingresado, edad_ingresada, altura_ingresada)



# Crear 
# una funcion que haga un saludo personalizado 

# pida los datos a traves de inputs. 


# El saludo ha de mostrar cuantos años tendrá la persona en el 2030.


