# Obtener desde el teclado los lados de un rectangulo, luego devolver el perímetro y su área

base = int(input("Ingrese la base en metros: "))
altura = int(input("Ingrese la altura en metros: "))

perimetro = (2 * base) + (2 * altura)
area = base * altura

print(f"El perimetro = {perimetro}\nEl area = {area}")