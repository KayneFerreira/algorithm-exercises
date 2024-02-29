'''
    Calcule a quantidade de litros gastos em uma viagem, sabendo que o 
    automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
'''

from os import system as sys

def calculateTrip(time, speed):
    return (speed / 12) * (time / 60)


def main():
    sys("clear")
    print("Qual o tempo de percurso da viagem? (em minutos)"); 
    time = int(input("> "))
    print("Qual a velocidade média do veículo durante o percurso?")
    speed = int(input("km "))
    gas = calculateTrip(time, speed)
    print(f"A viagem gastou aproximadamente {format(gas, '.1f')} "
          + "litros de combustível.")


if __name__ == "__main__":
    main()