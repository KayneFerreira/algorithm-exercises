'''
    09. Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.
'''

from os import system as sys

def sumOfSquares(x, y):
    return x**2 + y**2


def main():
    sys("clear")
    print("Insira o primeiro valor: "); x = int(input("> "))
    print("Insira o segundo valor: "); y = int(input("> "))
    result = sumOfSquares(x, y)
    print(f"O resultado da soma dos quadrados é {result}")


if __name__ == "__main__":
    main()