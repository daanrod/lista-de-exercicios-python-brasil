"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(0)
    1
    >>> calcular_fatorial(1)
    1
    >>> calcular_fatorial(2)
    2
    >>> calcular_fatorial(3)
    6
    >>> calcular_fatorial(4)
    24
    >>> calcular_fatorial(5)
    120

"""


def calcular_fatorial(n: int) -> int:
    """Escreva aqui em baixo a sua solução"""

    fat = 1
    result = 1
    if n != 0 or n != 1:
        for i in range(n):
            result *= fat
            fat += 1
        print(result)
    else:
        print(1)
