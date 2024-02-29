'''
    06. Receba os valores em x e y. Efetua a troca de seus valores e mostre 
    seus conteúdos.
'''

from os import system as sys

def main():
    sys("clear")
    x = int(input("Insira o valor de 'X': "))
    y = int(input("Insira o valor de 'Y': "))
    temp = x
    x = y
    y = temp
    print(f"Valor de 'X': {x}")
    print(f"Valor de 'Y': {y}")


if __name__ == "__main__":
    main()