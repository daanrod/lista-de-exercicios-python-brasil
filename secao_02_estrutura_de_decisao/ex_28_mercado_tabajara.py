"""
Exercício 28 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_carne('Filé Duplo', 2, 'dinheiro')
    '2 kg de Filé Duplo a R$ 4.90/kg saem a R$ 9.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Filé Duplo', 4, 'cartão tabajara')
    '4 kg de Filé Duplo a R$ 4.90/kg saem a R$ 19.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 18.62'
    >>> calcular_preco_da_carne('Filé Duplo', 6, 'pix')
    '6 kg de Filé Duplo a R$ 5.80/kg saem a R$ 34.80. Não há desconto, pagamento feito com pix'
    >>> calcular_preco_da_carne('Filé Duplo', 8, 'cartão tabajara')
    '8 kg de Filé Duplo a R$ 5.80/kg saem a R$ 46.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 44.08'
    >>> calcular_preco_da_carne('Alcatra', 2, 'dinheiro')
    '2 kg de Alcatra a R$ 5.90/kg saem a R$ 11.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 4, 'cartão tabajara')
    '4 kg de Alcatra a R$ 5.90/kg saem a R$ 23.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 22.42'
    >>> calcular_preco_da_carne('Alcatra', 6, 'dinheiro')
    '6 kg de Alcatra a R$ 6.80/kg saem a R$ 40.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 8, 'cartão tabajara')
    '8 kg de Alcatra a R$ 6.80/kg saem a R$ 54.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 51.68'
    >>> calcular_preco_da_carne('Picanha', 2, 'dinheiro')
    '2 kg de Picanha a R$ 6.90/kg saem a R$ 13.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 4, 'cartão tabajara')
    '4 kg de Picanha a R$ 6.90/kg saem a R$ 27.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 26.22'
    >>> calcular_preco_da_carne('Picanha', 6, 'dinheiro')
    '6 kg de Picanha a R$ 7.80/kg saem a R$ 46.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 8, 'cartão tabajara')
    '8 kg de Picanha a R$ 7.80/kg saem a R$ 62.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 59.28'
    
"""


def calcular_preco_da_carne(tipo_de_carne: str, kilos_de_carne: int, forma_de_pagamento: str) -> str:
    """Escreva aqui em baixo a sua solução"""

    file_ate_5kg = 4.90
    file_acima_5kg = 5.80
    alcatra_ate_5kg = 5.90
    alcatra_acima_5kg = 6.80
    picanha_ate_5kg = 6.90
    picanha_acima_5kg = 7.80


    lista_compra= []
    """8 kg de Picanha a R$ 7.80/kg saem a R$ 62.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 59.28"""
    """6 kg de Picanha a R$ 7.80/kg saem a R$ 46.80. Não há desconto, pagamento feito com dinheiro"""

    if kilos_de_carne <= 5 and tipo_de_carne == 'Filé Duplo':
        valor_carne = file_ate_5kg
        valor_total_pedido = valor_carne * kilos_de_carne
        lista_compra.append(f'{kilos_de_carne} kg de {tipo_de_carne} a R$ {valor_carne:.2f}/kg saem a R$ {valor_total_pedido:.2f}.')
    elif kilos_de_carne > 5 and tipo_de_carne == 'Filé Duplo':
        valor_carne = file_acima_5kg
        valor_total_pedido = valor_carne * kilos_de_carne
        lista_compra.append(f'{kilos_de_carne} kg de {tipo_de_carne} a R$ {valor_carne:.2f}/kg saem a R$ {valor_total_pedido:.2f}.')
    if kilos_de_carne <= 5 and tipo_de_carne == 'Alcatra':
        valor_carne = alcatra_ate_5kg
        valor_total_pedido = valor_carne * kilos_de_carne
        lista_compra.append(f'{kilos_de_carne} kg de {tipo_de_carne} a R$ {valor_carne:.2f}/kg saem a R$ {valor_total_pedido:.2f}.')
    elif kilos_de_carne > 5 and tipo_de_carne == 'Alcatra':
        valor_carne = alcatra_acima_5kg
        valor_total_pedido = valor_carne * kilos_de_carne
        lista_compra.append(f'{kilos_de_carne} kg de {tipo_de_carne} a R$ {valor_carne:.2f}/kg saem a R$ {valor_total_pedido:.2f}.')
    if kilos_de_carne <= 5 and tipo_de_carne == 'Picanha':
        valor_carne = picanha_ate_5kg
        valor_total_pedido = valor_carne * kilos_de_carne
        lista_compra.append(f'{kilos_de_carne} kg de {tipo_de_carne} a R$ {valor_carne:.2f}/kg saem a R$ {valor_total_pedido:.2f}.')
    elif kilos_de_carne > 5 and tipo_de_carne == 'Picanha':
        valor_carne = picanha_acima_5kg
        valor_total_pedido = valor_carne * kilos_de_carne
        lista_compra.append(f'{kilos_de_carne} kg de {tipo_de_carne} a R$ {valor_carne:.2f}/kg saem a R$ {valor_total_pedido:.2f}.')

    if forma_de_pagamento == 'cartão tabajara':
        desconto = valor_total_pedido * 0.05
        valor_com_desconto = valor_total_pedido - desconto
        lista_compra.append(f'Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_com_desconto:.2f}')
    elif forma_de_pagamento == 'pix':
        lista_compra.append('Não há desconto, pagamento feito com pix')
    else:
        lista_compra.append('Não há desconto, pagamento feito com dinheiro')

    if len(lista_compra) == 2:
        pt1, pt2 = lista_compra
        return f'{pt1} {pt2}'
