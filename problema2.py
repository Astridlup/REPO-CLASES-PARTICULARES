#temas: float, input, print, operaciones

#Pedile al usuario que ingrese el precio de un producto. Mostrá por pantalla el precio final con un IVA del 21%.

precio=float(input ("Ingrese el precio del producto:  "))
iva= float(precio*0.21)
precio_con_iva= float(precio + iva)
print(f"El iva es: {iva}:  ")
print(f"El precio con IVA es: {precio_con_iva}")


