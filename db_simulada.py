
# Al ser funciones nuestras, debemos aclarar el origen de carpetas/archivos del cual tomaremos la funcion o clase
from clases.usuarios.cliente import Cliente
from clases.usuarios.empleado import Empleado
from clases.usuarios.administrador import Administrador
from clases.direccion import Direcciones_empleado

# Al ser una función propia de python, no hay que comentarle de que carpeta viene 
from datetime import datetime 

# Definimos una instancia para cada clase
cliente_uno = Cliente(
    dni_cliente='47255789',
    nombre='Magdalena',
    apellido='Cruz',
    email='magdalenacruz@gmail.com',
    telefono='549351667788',
    clave='MAgda11??',
    fecha_registro=datetime.now()
)

direccion_empleado_uno = Direcciones_empleado(
    id_direccion=1,
    provincia='Córdoba',
    localidad='Villa Animi',
    barrio='Los Palomares',
    calle='Independencia',
    altura=1504
)

empleado_uno = Empleado(
    dni_empleado='45897256',
    direccion=direccion_empleado_uno,
    nombre='Ernesto',
    apellido='Videla',
    email='ernestovidela@gmail.com',
    clave='ERnesto11??',
    telefono='549351664422',
    fecha_ingreso=datetime.now(),
    cvu_empleado='123456789101112879215',
    alias_empleado='espia.batea.cruz.mp'
)

administrador_uno = Administrador(
    id_administrador=1,
    nombre='Rafael',
    apellido='Caceres',
    email='rafaelcaceres@gmail.com',
    clave='RAfael11??',
    cvu_administrador='123456789101112878879',
    alias_administrador='monitor.cable.webcam.nx'
)

# Diccionarios
diccionario_clientes = {
    cliente_uno.email: cliente_uno
}

diccionario_empleados = {
    empleado_uno.email: empleado_uno
}

diccionario_administradores = {
    administrador_uno.email: administrador_uno
}