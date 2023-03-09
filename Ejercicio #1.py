# = Pedir al usuario el salario actual y la antigüedad en años
salarioActual = float(input("Ingrese el salario actual: "))
antiguedad = int(input("Ingrese la antigüedad en años: "))

# = Calcular el aumento según la antigüedad
if antiguedad >= 0 and antiguedad <= 5:
    aumento = salarioActual * 0.1
elif antiguedad >= 6 and antiguedad <= 9:
    aumento = salarioActual * 0.15
elif antiguedad >= 10 and antiguedad <= 15:
    aumento = salarioActual * 0.25
else:
    aumento = salarioActual * 0.3

# = Calcular el nuevo salario
nuevoSalario = salarioActual + aumento

# = Mostrar la información calculada
print("El aumento correspondiente a la antigüedad de", antiguedad, "años es de", aumento, "colones.")
print("El nuevo salario es de", nuevoSalario, "colones.")

# = Codigo programado por: Josué Brenes Hernández
# = Introducción a la programación (SC-115)
# = Profesor Christian Solano Pérez
# = Universidad Fidélitas (IC-2023)