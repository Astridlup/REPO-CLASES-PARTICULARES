from db_simulada import *
from datetime import datetime


def opciones_cliente(usuario, contraseña): 
      cliente_obj = diccionario_clientes[usuario]
      if cliente_obj.clave == contraseña:
        print('\n¡Ingreso exitoso! Haz iniciado sesión como cliente')
        while True:
                print('Tus opciones son:')
                print('1. Ver datos personales')
                print('2. Salir')
                respuesta_cliente = input().strip()

                if not respuesta_cliente:
                    print('¡Error! Campo vacío no permitido')
                    continue

                try:
                    opcion = int(respuesta_cliente)
                    if opcion == 1:
                        cliente_obj.mostrar_datos_personales()
                    elif opcion == 2:
                        print('Saliendo...')
                        break
                    else:
                        print('¡Ops! Opción no válida. Pruebe nuevamente...')
                except ValueError:
                    print('\n¡Error! Ingrese un número válido')
                    break

def login(): 
     print("INGRESANDO A ARCHIVO LOGIN DE auth/login...")

     while (True):
        intentos = 0

        usuario = input('Ingrese su usuario (email): ')
        contraseña = input('Ingrese su contraseña: ')

        usuario = usuario.replace(" ", "")
        contraseña = contraseña.replace(" ", "")

        if not usuario or not contraseña:
            print('¡Error! Campo/s vacío/s no permitido/s. Pruebe nuevamente...')
        else: 
            if usuario in diccionario_clientes:
                opciones_cliente(usuario=usuario, contraseña=contraseña)
            elif usuario in diccionario_empleados:
                empleado_obj = diccionario_empleados[usuario]
                if empleado_obj.clave == contraseña:
                    print('\n¡Ingreso exitoso! Haz iniciado sesión como empleado')
                    while True:
                        print('Tus opciones son:')
                        print('1. Ver datos personales')
                        print('2. Salir')
                        respuesta_empleado = input().strip()

                        if not respuesta_empleado:
                            print('¡Error! Campo vacío no permitido')
                            continue

                        try:
                            opcion = int(respuesta_empleado)
                            if opcion == 1:
                                empleado_obj.mostrar_datos_personales()
                            elif opcion == 2:
                                print('Saliendo...')
                                break
                            else:
                                print('¡Ops! Opción no válida. Pruebe nuevamente...')
                        except ValueError:
                            print('\n¡Error! Ingrese un número válido')
                    break
                else:
                    print('Contraseña incorrecta. Intente nuevamente.')
            elif usuario in diccionario_administradores:
                administrador_obj = diccionario_administradores[usuario]
                if administrador_obj.clave == contraseña:
                    print('\n¡Ingreso exitoso! Haz iniciado sesión como administrador')

                    while (True):
                        print('\nTus opciones son:')
                        print('1. Ver datos personales')
                        print('2. Ver clientes')
                        print('3. Ver empleados')
                        print('4. Ver administradores')
                        print('5. Cambiar un rol')
                        print('6. Eliminar un usuario')
                        print('7. Salir\n')
                        respuesta_administrador = input()
                        respuesta_administrador = respuesta_administrador.replace(" ", "")

                        if not respuesta_administrador:
                            print('¡Error! Campo vacío no permitido')
                        else:
                            try:
                                respuesta_administrador = int(respuesta_administrador)
                                match respuesta_administrador:
                                    case 1:
                                        administrador_obj.mostrar_datos_personales()
                                    case 2:
                                        administrador_obj.mostrar_clientes(diccionario_clientes)
                                    case 3:
                                        administrador_obj.mostrar_empleados(diccionario_empleados)
                                    case 4:
                                        administrador_obj.mostrar_administradores(diccionario_administradores)
                                    case 5:
                                        while (True):
                                            print('\nOpciones Disponibles:')
                                            print('1. Ingrese el email del usuario que desea cambiar de rol')
                                            print('2. Salir\n')
                                            opcion_seleccionada = input()
                                            opcion_seleccionada = opcion_seleccionada.replace(" ", "")
                                            if not opcion_seleccionada:
                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                            else:
                                                try:
                                                    opcion_seleccionada = int(opcion_seleccionada)
                                                    match opcion_seleccionada:
                                                        case 1:
                                                            usuario_a_cambiar = input('\nIngrese el email: ')
                                                            usuario_a_cambiar = usuario_a_cambiar.replace(" ", "")

                                                            if not usuario_a_cambiar:
                                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                            else:
                                                                if usuario_a_cambiar in diccionario_clientes.keys():
                                                                    print(f'\nEl usuario con correo "{usuario_a_cambiar}" es un cliente')
                                                                    print('¿Qué rol desea asignarle?')
                                                                    while(True):
                                                                        print('1. Empleado') 
                                                                        print('2. Administrador')
                                                                        print('3. Salir\n')
                                                                        opcion_rol = input()
                                                                        opcion_rol = opcion_rol.replace(" ", "")

                                                                        if not opcion_rol:
                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                        else:
                                                                            try:
                                                                                opcion_rol = int(opcion_rol)
                                                                                match opcion_rol:
                                                                                    case 1:
                                                                                        administrador_obj.cambiar_rol_empleado(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                        break
                                                                                    case 2:
                                                                                        administrador_obj.cambiar_rol_administrador(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                        break
                                                                                    case 3:
                                                                                        print('Saliendo...')
                                                                                        break
                                                                                    case _:
                                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                            except ValueError:
                                                                                print('¡Error! Ingrese un número de opción válida')
                                                                elif usuario_a_cambiar in diccionario_empleados.keys():
                                                                    print(f'\nEl usuario con correo "{usuario_a_cambiar}" es un empleado')
                                                                    print('¿Qué rol desea asignarle?')
                                                                    while(True):
                                                                        print('1. Cliente') 
                                                                        print('2. Administrador')
                                                                        print('3. Salir\n')
                                                                        opcion_rol = input()
                                                                        opcion_rol = opcion_rol.replace(" ", "")

                                                                        if not opcion_rol:
                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                        else:
                                                                            try:
                                                                                opcion_rol = int(opcion_rol)
                                                                                match opcion_rol:
                                                                                    case 1:
                                                                                        administrador_obj.cambiar_rol_cliente(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                        break
                                                                                    case 2:
                                                                                        administrador_obj.cambiar_rol_administrador(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                        break
                                                                                    case 3:
                                                                                        print('Saliendo...')
                                                                                        break
                                                                                    case _:
                                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                            except ValueError:
                                                                                print('¡Error! Ingrese un número de opción válida')
                                                                elif usuario_a_cambiar in diccionario_administradores.keys():
                                                                    print(f'\nEl usuario con correo "{usuario_a_cambiar}" es un administrador')
                                                                    print('¿Qué rol desea asignarle?')
                                                                    while(True):
                                                                        print('1. Cliente') 
                                                                        print('2. Empleado')
                                                                        print('3. Salir\n')
                                                                        opcion_rol = input()
                                                                        opcion_rol = opcion_rol.replace(" ", "")

                                                                        if not opcion_rol:
                                                                            print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                                        else:
                                                                            try:
                                                                                opcion_rol = int(opcion_rol)
                                                                                match opcion_rol:
                                                                                    case 1:
                                                                                        administrador_obj.cambiar_rol_cliente(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                        break
                                                                                    case 2:
                                                                                        administrador_obj.cambiar_rol_empleado(diccionario_clientes, diccionario_empleados, diccionario_administradores, usuario_a_cambiar)
                                                                                        break
                                                                                    case 3:
                                                                                        print('Saliendo...')
                                                                                        break
                                                                                    case _:
                                                                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                                            except ValueError:
                                                                                print('¡Error! Ingrese un número de opción válida')
                                                                else:
                                                                    print('¡Error! El email ingresado no existe')
                                                        case 2:
                                                            print('\nSaliendo...')
                                                            break
                                                        case _:
                                                            print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                except ValueError:
                                                    print('\n¡Error! Ingrese un número de opción válida') 
                                    case 6:
                                        while (True):
                                            print('\nOpciones Disponibles:')
                                            print('1. Ingrese el email del usuario que desea eliminar')
                                            print('2. Salir\n')
                                            opcion_seleccionada = input()
                                            opcion_seleccionada = opcion_seleccionada.replace(" ", "")
                                            if not opcion_seleccionada:
                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...') 
                                            else:
                                                try:
                                                    opcion_seleccionada = int(opcion_seleccionada)
                                                    match opcion_seleccionada:
                                                        case 1:
                                                            usuario_a_eliminar = input('\nIngrese el email: ')
                                                            usuario_a_eliminar = usuario_a_eliminar.replace(" ", "")

                                                            if not usuario_a_eliminar:
                                                                print('¡Error! Campo vacío no permitido. Pruebe nuevamente...')
                                                            else:
                                                                if usuario_a_eliminar in diccionario_clientes.keys():
                                                                    administrador_obj.eliminar_cliente(diccionario_clientes, usuario_a_eliminar)
                                                                    break
                                                                elif usuario_a_eliminar in diccionario_empleados.keys():
                                                                    administrador_obj.eliminar_empleado(diccionario_empleados, usuario_a_eliminar)
                                                                    break
                                                                elif usuario_a_eliminar in diccionario_administradores.keys() and usuario_a_eliminar != administrador_uno:
                                                                    administrador_obj.eliminar_administrador(diccionario_administradores, administrador_obj, usuario_a_eliminar)
                                                                    break
                                                                else:
                                                                    print('¡Error! El usuario que deseas eliminar no existe')
                                                        case 2:
                                                            print('Saliendo...')
                                                            break
                                                        case _:
                                                            print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                                                except ValueError:
                                                    print('\n¡Error! Ingrese un número de opción válida')
                                    case 7:
                                        print('\nSaliendo...')
                                        break
                                    case _:
                                        print('¡Ops! Parece que haz seleccionado una opción no válida. Pruebe nuevamente...')
                            except ValueError:
                                print('\n¡Error! Ingrese un número de opción válida')
                    break
                else:
                    print('\nNo existe ningún usuario registrado con ese usuario y contraseña.')
            else:
                if intentos < 3:
                    print('\nNo se ha encontrado ninguna cuenta asociada a esos datos')
                    intentos = intentos + 1
                else:
                    print('\n¡Error! Vuelve a intentarlo más tarde...')
                    break