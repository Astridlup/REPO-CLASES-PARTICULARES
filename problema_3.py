#Problema 3: Validador de nombre y edad

#**Temas:** `string`, `int`, `input`, `print`, `if/else`

#Pedile al usuario que ingrese su nombre y su edad.  
#Si la edad es mayor o igual a 18, imprimí un mensaje de bienvenida.  
#Si no, indicá que debe ser mayor de edad para continuar.

### Ejemplo 1:
# Ingrese su nombre: Cristian
#📥 Ingrese su edad: 17
#📤 Cristian, aún no sos mayor de edad. No podés continuar.

nombre=input ("Ingrese su nombre:   ")
edad= int(input ("Igrese su edad:  "))
if edad >=18: 
    print(f"Bienvenido,{nombre}, eres mayor de edad")
else:
    print(f"{nombre} aún no sos mayor de edad. No puedes continuar")





