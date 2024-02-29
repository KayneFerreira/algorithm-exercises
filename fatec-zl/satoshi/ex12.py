'''
    12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade 
    e quantos anos terá daqui a 17 anos.
'''

from os import system as sys

def func(anoNascimento, anoAtual):
    return anoAtual - anoNascimento


def main():
    sys("clear")
    print("Qual o ano de nascimento da pessoa? "); 
    anoNascimento = int(input("> "))
    print("Qual o ano atual? ")
    anoAtual = int(input("> "))
    idade = func(anoNascimento, anoAtual)
    print(f"A pessoa tem {idade} anos de idade.")
    print(f"Ela terá {idade + 17} daqui a 17 anos.")


if __name__ == "__main__":
    main()