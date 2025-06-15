# Importamos los módulos necesarios. 
# Antes de inicializar el programa, debe tenr declaradas las funciones de dónde va a obtener todo
from auth.login import login
from auth.register import register

# Mensaje bienvenida
print('\n¡Bienvenido a AquaMóvil!')

# Esta lógica inicial, donde: 
# - Un bucle itera sobre opciones 
# - Se toma el input del usuario con respecto a las opciones 
# - Se hace match en base a cada caso y se arroja la función deseada 
# - Se hace un break del bucle para la opción "Salir"

# Se ve repetido a lo largo de todo el programa y sus modulos, se observa su aplicacion en: 
# - main.py 
# - auth/login -> en la funcion login y sus sub-funciones 
# - auth/register -> en la funcion register y sus sub-funciones

# Bucle general que ejecuta el programa, itera sobre las opciones que tendremos para elegir
while (True):
    # A traves de prints, muestra las opciones de manera visual 
    print('1. Iniciar Sesión')
    print('2. Registrarse')
    print('3. Salir\n')
    
    # Utiliza la funcion input() para que el usuario ingrese un numero, que matcheara con las opciones propuestas 
    respuesta = input('Por favor, seleccione una opción: ')

    # Elimina espacios innecesarios en la respuesta, para evitar errores que vengan por parte del usuario, ya que los espacios
    # a nivel computacional, son considerados como caracteres. No esl o mismo "1" que "1 ".
    respuesta = respuesta.replace(" ", "")

    # Si no hay una respuesta, marca un error, así el usuario se da cuenta de que no puede enviar espacios vacios 
    if not respuesta:
        print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')

    # Si hay una respuesta, comienza a matchear la respuesta (1, 2 o 3) con los casos dependiendo cada funcion 
    else:
        try:
            # Convierte la respuesta en numero entero, porque la declaracion "match respuesta" necesita de numeros
            respuesta = int(respuesta)
            match respuesta:
                # Si la respuesta del usuario fue 1, sabe que deberá entrar el bloque de login 
                case 1:
                 login()
                # Si la respuesta del usuario fue 2, sabe que deberá entrar al bloque de register 
                case 2:
                 register()
                #  Si la respuesta fue 3, deberá salir del programa. Por eso tiene la declaración "break", que rompe el bucle de ejecución
                case 3:
                    print('\nSaliendo del sistema... ¡Hasta luego!\n')
                    break
                # Si ingresa un numero que está por fuera de los establecidos (1, 2 o 3), arroja un error de opcion invalida 
                case _:
                    print('¡Ops! Opción no válida. Pruebe nuevamente...')
        # Si comete algun otro error, como ingresar una palabra, arrojará un error 
        except ValueError:
            print('¡Error! Ingrese un número válido')