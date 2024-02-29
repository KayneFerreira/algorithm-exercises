'''
    03. Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
'''

from os import system as sys

def calcTriangleArea(base, height):
    return (base * height) / 2


def main():
    sys("clear")
    print("Informe a base do triângulo: "); base = int(input("> "))
    print("Informe a altura do triângulo: "); height = int(input("> "))
    result = calcTriangleArea(base, height)
    print(f"A área do triangulo é {result}m²")


if __name__ == "__main__":
    main()