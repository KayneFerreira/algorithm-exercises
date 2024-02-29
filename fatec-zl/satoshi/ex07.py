'''
    07. Receba os valores do comprimento, largura e altura de um paralelepípedo. 
    Calcule e mostre seu volume.
'''

from os import system as sys

def calcCobblestoneValume(length, width, height):
    return length * width * height


def main():
    sys("clear")
    print("Cálculo de volume de um paralelepípedo.")
    print("Insira o comprimento: "); length = int(input("> "))
    print("Insira a largura: "); width = int(input("> "))
    print("Insira a altura: "); height = int(input("> "))
    volume = calcCobblestoneValume(length, width, height)
    print(f"O volume total é: {volume}")


if __name__ == "__main__":
    main()