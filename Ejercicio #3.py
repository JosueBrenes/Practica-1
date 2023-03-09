precioPorNoche = 100 # = El precio por noche equivale a 100 dolares

# = Solicitamos al usuario el numero de noches que se va quedar a dormir
noches = int(input("Digite las noches que se va quedar a dormir en el hotel: "))

# = Se calcula el precio de las noches con la cantidad digitada
montoTotal = precioPorNoche * noches

# = Calculamos el descuento y aplicar el descuento del 5% si se queda más de 3 noches
if noches >= 3:
    descuento = 0.5
    montoConDescuento = montoTotal * descuento 

elif noches < 3:
    descuento = 0

# Calcular el monto total con descuento
montoTotalConDescuento = montoTotal - montoConDescuento

print("El monto a pagar es de", montoTotal, "dolares")
print("El monto aplicado del descuento es de", montoConDescuento, "dolares")
print("El monto total a pagar con descuento es de", montoTotalConDescuento, "dolares")

# = Codigo programado por: Josué Brenes Hernández
# = Introducción a la programación (SC-115)
# = Profesor Christian Solano Pérez
# = Universidad Fidélitas (IC-2023)