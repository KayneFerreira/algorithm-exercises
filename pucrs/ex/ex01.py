'''
    1. Construa um algoritmo que, tendo como dados de entrada dois pontos 
    quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.
    
    A fórmula que efetua tal cálculo é: 
        d = math.sqrt((x2 - x1)^2 + (y2 - y1)^2)
'''

import math
from os import system as sys

def calcDistPlanos(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    

def main():
    sys("clear")
    print("Insira os valores do primeiro plano: ")
    x1 = int(input("Plano x1: "))
    y1 = int(input("Plano y1: "))
    print("Insira os valores do segundo plano: ")
    x2 = int(input("Plano x2: "))
    y2 = int(input("Plano y2: "))
    distancia = calcDistPlanos(x1, y1, x2, y2)
    print(f"\nDistância entre os planos P(x1, y1) e P(x2, y2):")
    print(f"d = {round(distancia, 2)}")


if __name__ == "__main__":
    main()
