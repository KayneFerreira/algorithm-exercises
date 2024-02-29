'''
    10. Receba 2 números reais. Calcule e mostre a diferença desses valores.
    
    PS: Duplicado (Exercício 18)
'''

from os import system as sys

def calculateDifference(x, y):
    result = 0
    if x > y:
        result = x - y
    else:
        result = y - x
    return result


def main():
    sys("clear")
    print("Insira um número real: "); x = int(input("> "))
    print("Insira outro número real: "); y = int(input("> "))
    result = calculateDifference(x, y)
    print(f"A diferença entre os valores é {result}")


if __name__ == "__main__":
    main()