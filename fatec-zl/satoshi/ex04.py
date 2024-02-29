'''
    04. Receba a temperatura em graus Celsius. Calcule e mostre a sua 
    temperatura convertida em fahrenheit F = (9*C+160) /5.
'''

from os import system as sys

def convertToFahrenheit(temp):
    return (9 * temp + 160) / 5


def main():
    sys("clear")
    print("Informe a temperatura em graus Celsius: ")
    temp = int(input("> "))
    result = convertToFahrenheit(temp)
    print(f"Temperatura convertida para Fahrenheit: {format(result, '.0f')}F")


if __name__ == "__main__":
    main()