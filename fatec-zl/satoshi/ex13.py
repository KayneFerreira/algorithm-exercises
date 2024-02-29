'''
    13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos 
    dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
'''

from os import system as sys

def func(foodKg):
    return (foodKg * 1000) / 50


def main():
    sys("clear")
    print("Insira a quantidade de alimentos a receber em quilos(kg):"); 
    foodKg = float(input("> "))
    days = func(foodKg)
    print(f"Considerando que a pessoa consuma 50g por dia, {foodKg}Kg de " 
          + f"alimento, irá durar aproximadamente {format(days, '.1f')} dias.")


if __name__ == "__main__":
    main()