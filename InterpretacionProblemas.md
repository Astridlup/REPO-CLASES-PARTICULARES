# Guía práctica para resolver problemas en Python

## 1. Enfoque inicial

- **Ir por los aspectos visuales**: Separar las oraciones del enunciado para identificar cada parte del problema.
- **Analizar cada parte**: Observar qué se está pidiendo realizar.
- **Detectar palabras clave**: Estas nos indicarán qué funciones utilizar.

---

## 2. Palabras clave comunes y su interpretación

- **"Pedir al usuario" / "Ingresar" / "Solicitar"**  
  → Utilizamos `input()`, que permite al usuario ingresar datos.

- **"Describir" / "Mostrar por pantalla" / "Imprimir" / "Enviar un mensaje"**  
  → Utilizamos `print()`, que nos permite mostrar información en pantalla.

- **"Opciones" / "Si...entonces..." / "Seleccionar" / "Elegir"**  
  → Utilizamos estructuras condicionales `if`, `elif` y `else`.  
    - `if`: primera condición.  
    - `elif`: condiciones adicionales.  
    - `else`: cuando no se cumple ninguna condición anterior.

- **`.lower()`**  
  → Convierte el texto ingresado en minúsculas para evitar errores por mayúsculas.

---

## 3. Ejemplo práctico 1: Datos personales

**Enunciado**: Escribir un programa que pida al usuario que ingrese (por separado) nombre, apellido y edad. Luego, mostrar una descripción de la persona, el año en que nació y su edad en 2030.

```python
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

print("La persona se llama", nombre, apellido, "y tiene", edad, "años.")
print("Nació en el año", 2023 - edad, "y en el 2030 tendrá", 2030 - (2023 - edad))
