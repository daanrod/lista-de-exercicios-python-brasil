"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    ### calculo para separar as casas ###
    obj_numero = valor
    unidade = int(obj_numero % 10)
    obj_numero = int((obj_numero - unidade) / 10)
    dezena = int(obj_numero % 10)
    centena = int(obj_numero / 10)

    ### lista com conteudo de saida ###
    texto = []

    # notas de 100
    if centena == 1:
        texto.append(f'1 nota de R$ 100')
    elif centena > 0:
        texto.append(f'{centena} notas de R$ 100')
    # notas de 50
    if dezena >= 5:
        dezena = dezena -5
        texto.append(f'1 nota de R$ 50')
    # notas de 10
    if dezena == 1:
        texto.append(f'1 nota de R$ 10')
    elif dezena > 0 and dezena < 5:
        texto.append(f'{dezena} notas de R$ 10')
    # notas de 5
    if unidade >= 5:
        unidade = unidade - 5
        texto.append(f'1 nota de R$ 5')
    # notas de 1
    if unidade == 1:
        texto.append(f'1 nota de R$ 1')
    elif unidade > 0  and unidade < 5:
        texto.append(f'{unidade} notas de R$ 1')

    ### formatando saida ###
    if len(texto) == 1:
        saque = texto.pop()
    elif len(texto) == 2:
        pt1, pt2 = texto
        saque = f'{pt1} e {pt2}'
    elif len(texto) == 3:
        pt1, pt2, pt3 = texto
        saque = f'{pt1}, {pt2} e {pt3}'
    elif len(texto) == 4:
        pt1, pt2, pt3, pt4 = texto
        saque = f'{pt1}, {pt2}, {pt3} e {pt4}'
    elif len(texto) == 5:
        pt1, pt2, pt3, pt4, pt5 = texto
        saque = f'{pt1}, {pt2}, {pt3}, {pt4} e {pt5}'
    return f'{saque}'
    