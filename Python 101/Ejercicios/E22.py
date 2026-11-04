# Objetivo: Sistema de parqueos... si una persona usa el parqueo 3 horas o menos se le cobra 500 colones
#.          si la persona va a usar más tiempo, entonces por cada media hora se le agregan 150 colones
#           en caso de confirmar 20 a 24 horas, entonces se le cobran 5700 colones
#.          Hay que obtener la cantidad de horas parqueado y la cantidad de carros que va a parquear, se cobra
#           por carro y hay que obtener el total final.

def calculo_horas_x_carro(horas, cantidad_Carros):
    if horas > 0 and cantidad_Carros > 0:
        for i in range(cantidad_Carros): 
            if horas < 3.0:
                total = 500 * cantidad_Carros
            else:
                total = ((((horas - 3) * 2) * 150) + 500) * cantidad_Carros
        return total
    else:
        return 0

horas = float(input("Ingrese la cantidad de horas: "))
carros = int(input("Ingrese la cantidad de carros: "))

print(f"Por la cantidad de {carros} carros en {horas} horas, se le cobrará {calculo_horas_x_carro(horas, carros)} colones")
