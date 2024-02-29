'''
    3. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses 
    e dias e mostre-a expressa apenas em dias.
'''

# dias do ano
meses_ano = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31, 
    13: 31, 14: 28, 15: 31, 16: 30, 17: 31, 18: 30, 
    19: 31, 20: 31, 21: 30, 22: 31, 23: 30, 24: 31
}

from os import system as sys
from datetime import date

def converteDataEmDias(anos, meses, dias):
    ano_atual = date.today().year
    mes_atual = date.today().month
    for ano in range((ano_atual - anos), ano_atual):
        if ano % 4 != 0:
            dias += 365
        else:
            dias += 366
    for mes in range(mes_atual, mes_atual + meses):
        dias += meses_ano[mes+1]
    if ano_atual & 4 == 0:
        dias += 1
    return dias
    

def main():
    sys("clear")
    print("Quanto anos você tem?"); anos = int(input("> "))
    print("Quantos meses?"); meses = int(input("> "))
    print("Quantos dias?"); dias = int(input("> "))
    resultado = converteDataEmDias(anos, meses, dias)
    print(f"Você tem aproximadamente {resultado} dias de vida.")


if __name__ == "__main__":
    main()
