'''
    11. Receba o raio de uma circunferência. Calcule e mostre o comprimento da 
    circunferência.
'''

from os import system as sys
from math import pi

def calculateCircleLength(d):
    return d * pi


def main():
    sys("clear")
    print("Insira o diâmetro do círculo: ")
    d = float(input("> "))
    c = calculateCircleLength(d)
    print(f"O comprimento da circunferência é aproximadamente {format(c, '.2f')}")


if __name__ == "__main__":
    main()