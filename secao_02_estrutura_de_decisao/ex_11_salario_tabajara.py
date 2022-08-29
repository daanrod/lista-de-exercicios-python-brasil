"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00

"""


def calcular_aumento(salario: float):
    """Escreva aqui em baixo a sua solução"""
    salary = salario
    percent = 0
    salary_increase = 0
    new_salary = 0

    if salary <= 280:
        new_salary = salary * 1.2
        percent = ((new_salary - salary) / salary) * 100
        salary_increase = new_salary - salary
    elif salary > 280 and salary <= 700:
        new_salary = salary * 1.15
        percent = ((new_salary - salary) / salary) * 100
        salary_increase = new_salary - salary
    elif salary > 700 and salary <= 1500:
        new_salary = salary * 1.1
        percent = ((new_salary - salary) / salary) * 100
        salary_increase = new_salary - salary
    elif salary >= 1500:
        new_salary = salary * 1.05
        percent = ((new_salary - salary) / salary) * 100
        salary_increase = new_salary - salary


    print(f'Salário atual: R$ {salary:.2f}')
    print(f'Aumento porcentual: {percent:.0f}%')
    print(f'Valor do aumento: R$ {salary_increase:.2f}')
    print(f'Novo salário: R$ {new_salary:.2f}')
