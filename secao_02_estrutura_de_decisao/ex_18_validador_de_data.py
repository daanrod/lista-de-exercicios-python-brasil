"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""

    try:
        # separa dia, mês e ano em inteiro
        dd, mm, aaaa = map(int, data.split('/'))

        if mm < 1 or mm > 12 or aaaa < 0:
            return 'Data inválida'

        # ultimo dia do mês
        if mm in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mm == 2:
            if mm % 400 == 0 or (mm % 100 != 0 and mm % 4 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30
        if dd < 1 or dd > ultimo_dia:
            return 'Data inválida'
        # retorna data válida
        return 'Data válida'
    except ValueError:
        return 'Data inválida'
