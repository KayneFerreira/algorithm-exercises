'''
    4. Faça um algoritmo que leia a idade de uma pessoa expressa em dias e 
    mostre-a expressa em anos, meses e dias.
'''

from os import system as sys
from datetime import date

def converteDiasEmData(dias):
    anos = 0
    meses = 0
    ano_atual = int(date.today().year)
    while dias > 30:
        if dias >= 366 and ano_atual % 4 == 0:
            anos += 1
            dias -= 366
            ano_atual -= 1
        elif dias >= 365:
            anos += 1
            dias -= 365
            ano_atual -= 1
        elif dias < 365 and dias >= 30:
            meses += 1
            dias -= 30
    return dias, meses, anos


def main():
    sys("clear")
    print("Quantos dias de vida tem a pessoa? ")
    dias = int(input("> "))
    dias, meses, anos = converteDiasEmData(dias)
    print(f"A pessoa tem aproximadamente {anos} ano(s), {meses} mes(es) e {dias} dia(s).")


if __name__ == "__main__":
    main()