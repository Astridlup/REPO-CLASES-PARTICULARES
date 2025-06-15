from clases.usuarios.cliente import Cliente

# Con el asterisco en la importacion, declaramos que vamos a tomar todo lo que haya en ese archivo 
from db_simulada import *

from datetime import datetime

def register(): 
        intentos = 0
        max_intentos = 9

        while intentos < max_intentos:
            print('\nComplete el siguiente formulario para registrarse en el sistema:')

            dni_usuario = input('DNI (sin guiones ni puntos): ').replace(" ", "")
            nombre_usuario = input('Nombre: ').replace(" ", "")
            apellido_usuario = input('Apellido: ').replace(" ", "")
            email_usuario = input('Email: ').replace(" ", "")
            telefono_usuario = input('Teléfono (sin símbolos ni espacios): ').replace(" ", "")
            clave_usuario = input('Genere una clave: ').replace(" ", "")

            if not all([dni_usuario, nombre_usuario, apellido_usuario, email_usuario, telefono_usuario, clave_usuario]):
                print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
                intentos += 1
                continue

            if len(dni_usuario) < 7:
                print('¡Error! El DNI debe contener al menos 7 dígitos.')
                intentos += 1
                continue

            if len(telefono_usuario) < 10 or len(telefono_usuario) > 15:
                print('¡Error! El teléfono debe contener entre 10 y 15 caracteres.')
                intentos += 1
                continue

            if len(clave_usuario) < 8:
                print('¡Error! La clave debe contener 8 o más caracteres.')
                intentos += 1
                continue

            try:
                dni_usuario = int(dni_usuario)
                telefono_usuario = int(telefono_usuario)

                cliente = Cliente(
                    dni_cliente=dni_usuario,
                    nombre=nombre_usuario,
                    apellido=apellido_usuario,
                    email=email_usuario,
                    telefono=telefono_usuario,
                    clave=clave_usuario,
                    fecha_registro=datetime.now()
                )

                diccionario_clientes[cliente.email] = cliente
                print(f'\n¡Éxito! El usuario "{cliente.nombre} {cliente.apellido}" ha sido registrado correctamente.')
                break

            except ValueError:
                print('¡Error! DNI y teléfono deben contener solo números.')
                intentos += 1

            if intentos >= max_intentos:
                print('\n¡Error! Has alcanzado el límite máximo de intentos. Vuelve a intentarlo más tarde.')
                break