# AquaMóvil - Sistema de Gestión de Servicios

## Descripción del Proyecto
AquaMóvil es un sistema de gestión de servicios que permite la administración de usuarios (clientes, empleados y administradores), pedidos y servicios. El proyecto está diseñado como un ejercicio educativo para estudiantes que deben entender y mejorar su arquitectura.

## Arquitectura Actual

### Estructura de Directorios
```
├── auth/                    # Módulo de autenticación
│   ├── login.py            # Gestión de inicio de sesión
│   └── register.py         # Gestión de registro de usuarios
├── clases/                 # Modelos de datos
│   ├── usuarios/          # Clases de usuarios
│   │   ├── cliente.py
│   │   ├── empleado.py
│   │   └── administrador.py
│   ├── direccion.py       # Modelo de direcciones
│   ├── pedido.py          # Modelo de pedidos
│   └── servicio.py        # Modelo de servicios
├── db_simulada.py         # Base de datos simulada en memoria
└── main.py               # Punto de entrada de la aplicación
```

### Diseño de Clases
El sistema implementa un modelo orientado a objetos con las siguientes clases principales:

1. **Usuarios** (Jerarquía de clases):
   - `Cliente`: Usuario básico del sistema
   - `Empleado`: Extiende Cliente con funcionalidades de servicio
   - `Administrador`: Gestiona usuarios y roles del sistema

2. **Modelos de Datos**:
   - `Direcciones_empleado`: Gestiona la información de ubicación
   - `Pedidos`: Maneja las solicitudes de servicio
   - `Servicio`: Define los tipos de servicios disponibles



## Áreas de Mejora y Oportunidades de Modularización

## Decisiones de Diseño Actuales

1. **Uso de Diccionarios como Base de Datos**:
   - Decisión tomada para simplificar el desarrollo inicial
   - Facilita la comprensión del flujo de datos
   - Permite enfocarse en la lógica de negocio sin complejidad de base de datos

2. **Estructura de Clases**:
   - Jerarquía de usuarios clara y extensible
   - Separación de responsabilidades entre diferentes tipos de usuarios
   - Uso de herencia para compartir funcionalidad común

3. **Validación de Datos**:
   - Implementación de validaciones básicas en el registro
   - Manejo de errores con mensajes descriptivos
   - Limitación de intentos para operaciones sensibles


## Conclusión
Este proyecto sirve como base para que se comprenda: 
- La importancia de la modularización en el desarrollo de software
- La aplicación de patrones de diseño
- La separación de responsabilidades