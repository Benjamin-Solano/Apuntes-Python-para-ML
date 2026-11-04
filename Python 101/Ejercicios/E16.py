# Hacer que el usuario ingrese dos catetos de un triangulo rectangulo y mostrar la hipotenusa.
import math

cateto1 = int(input("Ingrese el primer cateto: "))
cateto2 = int(input("Ingrese el segundo cateto: "))

hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2)) 

print(f"Calculo de Hipotenusa = {hipotenusa}")


