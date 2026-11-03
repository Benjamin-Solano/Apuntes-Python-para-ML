#  Objetivo: Funciones... la mejor forma de reutilizar código, nació con el paradigma
#            funcional, el objetivo de encapsular codigo que se repite varias
#            veces en el código con el fin de alcanzar un objetivo y termina simplificando
#            su lectura. La estructura tipica de una funcion es tipo de dato + nombre + argumentos
#===============================================================================


# Funciones de Conversión 
# Utiles cuando se va a realizar un input.
mensaje = str(input("Ingrese una palabra: "))
numero = int(input("Ingrese un dígito: "))
decimal = float(input("Ingrese un numero decimal: "))

print(f"Outputs \n mensaje = {mensaje} \n numero = {numero} \n decimal = {decimal} ")
