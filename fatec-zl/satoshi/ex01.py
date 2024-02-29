'''
    01. Coletar o valor do lado de um quadrado, calcular sua área e apresentar o 
    resultado.
'''

from os import system as sys

def calculateSquareArea(side):
    return side**2


def main():
    sys("clear")
    print("Insira o valor de um lado do quadrado: ")
    side = int(input("> "))
    area = calculateSquareArea(side)
    print(f"A área do quadrado é: {area}m²")


if __name__ == "__main__":
    main()