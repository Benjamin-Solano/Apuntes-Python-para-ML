#  Objetivo: Funciones... la mejor forma de reutilizar código, nació con el paradigma
#            funcional, el objetivo de encapsular codigo que se repite varias
#            veces en el código con el fin de alcanzar un objetivo y termina simplificando
#            su lectura. La estructura tipica de una funcion es tipo de dato + nombre + argumentos
#.           pero python parece salirse del canasto del orden y simplemente es:
#            def + nombre + argumentos
#            se retorna la ultima línea o se utiliza el estatuto return...
#===============================================================================
# Imports
import math

# Funciones de Conversión 
# Utiles cuando se va a realizar un input.
mensaje = str(input("Ingrese una palabra: "))
numero = int(input("Ingrese un dígito: "))
decimal = float(input("Ingrese un numero decimal: "))

print(f"\nOutputs\nmensaje = {mensaje}\nnumero = {numero}\ndecimal = {decimal}")

# Funciones Matemáticas
# Existe un modulo que empaqueta varias funciones utiles, para esto hay que importar dicho modulo
# linea 7
# raíz cuadrada
print(math.sqrt(9))

# Potencia
print(pow(4,4)) 

# Funciones Creadas por el programador
def imprimir_doble(var):
    for i in range(2):
        print(f"{var}")

imprimir_doble("Hola")


# Estatuto Return
# Sirve para definir explicitamente el valor a retornar, incluso
# sirve para detener un loop en determinado punto que uno desee.
def numero_al_cubo(numero):
    return numero*numero*numero

print(numero_al_cubo(5))