'''
    08. Receba o valor de um depósito em poupança. Calcule e mostre o valor 
    após 1 mês de aplicação sabendo que rende 1,3% a. m.
'''

from os import system as sys

def calculateYield(deposit):
    deposit += deposit * 0.013
    return deposit


def main():
    sys("clear")
    print("Insira o valor para depósito: ")
    deposit = float(input("R$ "))
    yields = calculateYield(deposit)
    print(f"Valor de rendimento: R${format(yields, '.2f')}")


if __name__ == "__main__":
    main()