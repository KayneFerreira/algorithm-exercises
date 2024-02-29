'''
    15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e 
    mostre a hipotenusa.
'''

from os import system as sys
import math

def calculateHypotenuse(c1, c2):
    return math.sqrt(c1**2 + c2**2)


def main():
    sys("clear")
    print("Insira o valor do primeiro cateto: "); 
    c1 = float(input("> "))
    print("Insira o valor do segundo cateto: "); 
    c2 = float(input("> "))
    h = calculateHypotenuse(c1, c2)
    print(f"O valor da hipotenusa é {h}")


if __name__ == "__main__":
    main()