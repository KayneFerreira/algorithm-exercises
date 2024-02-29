'''
    6. Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica 
    expressa em segundos e mostre-o expresso em horas, minutos e segundos.
'''

from os import system as sys

def calculaTempoMaquina(segundos):
    horas = 0
    minutos = 0
    while segundos >= 60:
        if segundos >= 3600:
            horas += 1
            segundos -= 3600
        elif segundos >= 60:
            minutos += 1
            segundos -= 60
    return horas, minutos, segundos


def main():
    sys("clear")
    print("Qual o tempo de duração do evento? (em segdunos)")
    tempo = int(input("> "))
    horas, minutos, segundos = calculaTempoMaquina(tempo)
    print("Tempo do evento de maquina: ")
    print(f"{horas} hora(s) : {minutos} minuto(s) : {segundos} segundo(s)")


if __name__ == "__main__":
    main()