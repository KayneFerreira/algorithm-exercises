'''
    05. Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). 
    Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes).
    
    PS: Duplicado (Exercício 20)
'''

from os import system as sys
import math

def calcEquation(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return delta, None, None
    deltaRoot = math.sqrt(delta)
    x1 = (-b + deltaRoot) / (2 * a)
    x2 = (-b - deltaRoot) / (2 * a)
    return delta, deltaRoot, x1, x2


def main():
    sys("clear")
    print("Informe os coeficientes a seguir: ")
    a = int(input("Informe o valor de 'A': "))
    b = int(input("Informe o valor de 'B': "))
    c = int(input("Informe o valor de 'C': "))
    delta, deltaRoot, x1, x2 = calcEquation(a, b, c)
    print(f"\nDELTA: {delta}")
    if delta == 0:
        print(f"Raiz de DELTA: {deltaRoot}")
        print(f"x'  = {x1}")
        print(f"\nA equação possui apenas uma raiz real: {x1}")
    elif delta > 0:
        print(f"Raiz de DELTA: {deltaRoot}")
        print(f"x'  = {x1}")
        print(f"x'' = {x2}")
        print(f"\nA equação possui 2 raizes reais: {{ {x1}, {x2} }}")
    else:
        print(f"\nA equação não possui raizes reais.")


if __name__ == "__main__":
    main()