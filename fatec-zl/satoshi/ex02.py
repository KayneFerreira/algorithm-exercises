'''
    02. Receba o salário de um funcionário e mostre o novo salário com reajuste 
    de 15%.
'''

from os import system as sys

def adjustSalary(salary):
    return salary * 1.15


def main():
    sys("clear")
    print("Informe o salário do funcionário: ")
    salary = float(input(">R$ "))
    result = adjustSalary(salary)
    print(f"O salario reajustado é R${format(result, '.2f')}")


if __name__ == "__main__":
    main()