"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""

    p1 = 80000
    p2 = 200000
    anos = 0

    crescimento_p1 = 0.03
    crescimento_p2 = 0.015

    while True:
        if p1 > p2:
            return f"População de A, depois de {anos} ano(s) será de {int(p1)} pessoas, superando a de B, que será de {int(p2)} pessoas"
        p1 = p1 + (p1 * crescimento_p1)
        p2 = p2 + (p2 * crescimento_p2)
        anos += 1
