# = Pedir al usuario la cantidad de pantalones y el precio unitario
cantidad = int(input("Ingrese la cantidad de pantalones: "))
precioUnitario = float(input("Ingrese el precio unitario: "))

# = Calcular el total sin descuento
totalSinDescuento = cantidad * precioUnitario

# = Calcular el descuento correspondiente según la cantidad de pantalones
if cantidad >= 1 and cantidad <= 5:
    descuento = 0.125
elif cantidad >= 6 and cantidad <= 8:
    descuento = 0.2
else:
    descuento = 0.315

# = Calcular el total con descuento
totalConDescuento = totalSinDescuento * (1 - descuento)

# = Mostrar la información calculada
print("El total sin descuento es de", totalConDescuento, "coloes.")
print("El monto del descuento es de", totalConDescuento * descuento, "colones.")
print("El total con descuento es de", totalConDescuento, "colones.")

# = Codigo programado por: Josué Brenes Hernández
# = Introducción a la programación (SC-115)
# = Profesor Christian Solano Pérez
# = Universidad Fidélitas (IC-2023)