'''
    2. Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) 
    e calcule a seguinte expressão:
    
    D = R + S/2, onde R = (A + B)²
                      S = (B + C)²
'''

from os import system as sys

def calculaExpressao(a, b, c):
    r = (a + b)**2
    s = (b + c)**2
    return (r + s) / 2
    

def main():
    sys("clear")
    print("Insira os valores de A, B e C em sequência: ")
    print("(apenas valore inteiros positivos)\n")
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))
    resultado = calculaExpressao(a, b, c)
    print("Resultado da erxpressão 'D = R + S/2 onde R = (A + B)² e S = (B + C)²")
    print(f"D = {round(resultado, 2)}")


if __name__ == "__main__":
    main()
