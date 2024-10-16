# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
raio = int(input("receber o raio de um circulo: "))
altura = int(input("digite a altura: "))
import math
def calcular_area_base ():
    raio = 2 * 3.14 * raio
    return math.pi * (raio * 2)

def calcular_volume_cilindro ():
    volume = area * altura
    return area_base * altura 