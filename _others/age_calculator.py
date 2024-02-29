'''
    Algorítmo baseado na ferramenta 'Age Calculator' do site 'calculator.net'.
    
    Problema: Calcular idadade de uma pessoa, baseado no ano, mês e dia de 
    nascimento e mostrar o resultado em dias. 
    
    Regras:
        - Ferramentas e bibliotecas como o 'datetime' só devem ser utilizadas
        com o propósito de coletar a data atual, já que a mesma já possui 
        internamente funções que calculam a diferença entre as datas.
    
    Informações utilitárias:
    
        Mês mais curto do ano:
            Fevereiro: 28 ou 29 Dias

        Meses intermediários:
            Abril: 30 dias
            Junho: 30 dias
            Setembro: 30 dias
            Novembro: 30 dias

        Meses mais longos do ano:
            Janeiro: 31 Dias
            Março: 31 Dias
            Maio: 31 Dias
            Julho: 31 Dias
            Agosto: 31 Dias
            Outubro: 31 Dias
            Dezembro: 31 Dias
'''

from os import system as sys
from datetime import date

# dias do ano
year_months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# converte dias
def convertDays(day, this_day, this_month):
    days = 0
    if this_day > day:
        days += this_day - day
    elif this_day < day:
        days -= year_months[this_month] - (year_months[this_month] - (day - this_day))
        pass
    return days

# converte meses em dias
def convertMonths(month, this_month, this_year):
    days = 0
    start = month
    finish = this_month
    if this_month > month:
        for month_l in range(start, finish):
            days += year_months[month_l]
    elif this_month < month:
        start = this_month
        finish = 12 - (month - this_month)
        for month_l in range(start, finish):
            days -= year_months[month_l]
    return days

# converte anos em dias
def convertYears(year, this_year):
    days = 0
    for year_l in range(year, this_year):
        if year_l % 4 != 0:
            for month in year_months:
                days += year_months[month]
        else:
            for month in year_months:
                days += year_months[month]
            days += 1
    return days

# converte data em dias
def convertDateToDays(year, month, day):
    days = 0
    this_year = int(date.today().year)
    this_month = int(date.today().month)
    this_day = int(date.today().day)
    days += convertYears(year, this_year)
    days += convertMonths(month, this_month, this_year)
    days += convertDays(day, this_day, this_month)
    return days

# exibe resultados
def showResults(result, year, month, day):
    this_year = int(date.today().year)
    this_month = int(date.today().month)
    this_day = int(date.today().day)
    years = this_year - year
    months = this_month - month
    if this_month < month:
        months = 12 - (month - this_month)
        years -= 1
    days = this_day - day
    if this_day < day:
        days = year_months[this_month-1] - (day - this_day)
        months -= 1
    print(f"\nResultado: ")
    print(f"{years} anos; {months} meses; {days} dias.")
    print(f"{'{:,}'.format((years * 12) + months)} meses; {days} dias.")
    print(f"{'{:,}'.format(result)} days")
    print(f"{'{:,}'.format(result * 24)} horas")
    print(f"{'{:,}'.format(result * 24 * 60)} minutos")
    print(f"{'{:,}'.format(result * 24 * 60 * 60)} segundos")


def main():
    sys("clear")
    print("Qual seu ano de nascimento?"); year = int(input("> "))
    print("Qual o mês?"); month = int(input("> "))
    print("Qual o dia?"); day = int(input("> "))
    result = convertDateToDays(year, month, day)
    showResults(result, year, month, day)
    

if __name__ == "__main__":
    main()
