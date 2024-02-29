'''
    21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média 
    aritmética. Mostre a mensagem de acordo com a média:
    
        a. Se a média for >= 6,0 exibir “APROVADO”;
        b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
        c. Se a média for < 3,0 exibir “RETIDO”.
'''

from os import system as sys

def calculateAverageGrade(grades):
    totalGrade = 0
    for grade in grades:
        totalGrade += grade
    return totalGrade / 4


def main():
    sys("clear")
    grades = []
    print("Notas avaliativas do semestre: ")
    for i in range(1, 5):
        grades.append(int(input(f"{i}a nota: ")))
    averageGrade = calculateAverageGrade(grades)
    print(f"\nMédia do aluno: {averageGrade}")
    
    if averageGrade >= 6:
        print("APROVADO")
    elif averageGrade < 3:
        print("RETIDO")
    else:
        print("EXAME")


if __name__ == "__main__":
    main()