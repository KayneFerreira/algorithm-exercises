'''
    5. Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final 
    deste aluno. Considerar que a média é ponderada e que o peso das notas é: 
    2,3 e 5, respectivamente.
'''

from os import system as sys

def calculaMediaPonderada(n1, n2, n3):
    nota1 = (n1 / 10)*2
    nota2 = (n2 / 10)*3
    nota3 = (n3 / 10)*5
    nota_final = nota1 + nota2 + nota3
    return nota_final


def main():
    sys("clear")
    print("Insira a primeira nota do aluno: "); n1 = int(input("> "))
    print("Insira a segunda nota do aluno: "); n2 = int(input("> "))
    print("Insira a terceira nota do aluno: "); n3 = int(input("> "))
    nf = calculaMediaPonderada(n1, n2, n3)
    print(f"A nota final do aluno é: {round(nf, 2)}")


if __name__ == "__main__":
    main()