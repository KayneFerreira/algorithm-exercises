'''
    16. Receba a quantidade de horas trabalhadas, o valor por hora, o 
    percentual de desconto e o número de dependentes. Calcule o salário que 
    serão as horas trabalhadas x o valor por hora. Calcule o salário líquido 
    (= Salário Bruto - desconto). A cada dependente será acrescido R$ 100 no 
    Salário Líquido. Exiba o salário a receber.
'''

from os import system as sys

def calculateSalary(
    workingHours,
    payPerHour,
    discountPercentage,
    dependents
):
    grossSalary = workingHours * payPerHour
    discount = (grossSalary / 100) * discountPercentage
    netSalary = grossSalary - discount
    total = netSalary + (dependents * 100)
    return total


def main():
    sys("clear")
    print("Horas trabalhadas: "); workingHours = int(input("> "))
    print("Valor por hora: "); payPerHour = float(input("R$ "))
    print("Percentual de desconto: "); discountPercentage = float(input("% "))
    print("Número de dependentes: "); dependents = int(input("> "))
    netSalary = calculateSalary(
        workingHours,
        payPerHour,
        discountPercentage,
        dependents
    )
    print(f"\nLíquido a receber: R${format(netSalary, '.2f')}")


if __name__ == "__main__":
    main()