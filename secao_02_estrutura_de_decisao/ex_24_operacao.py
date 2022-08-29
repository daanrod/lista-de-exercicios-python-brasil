"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


import math


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""

    # calculo baseado na operação
    if operacao == '+':
      resultado = float(n_1 + n_2)
    elif operacao == '-':
      resultado = float(n_1 - n_2)
    elif operacao == '*':
      resultado = float(n_1 * n_2)
    elif operacao == '/':
      resultado = float(n_1 / n_2)

    texto = []
    
    arr = math.ceil(resultado)
    if arr == resultado:
      calc_par = resultado % 2
      if calc_par == 0:
        texto.append('par')
      else:
        texto.append('impar')
      
    if resultado == 0:
      texto.append('neutro')
    elif resultado > 0:
      texto.append('positivo')
    else:
      texto.append('negativo')
    
    if arr == resultado:
      texto.append('inteiro')
    else:
      texto.append('decimal')

    if len(texto) == 2:
      pt1, pt2 = texto
      saida_texto = f'{pt1} e {pt2}'
    if len(texto) == 3:
      pt1, pt2, pt3 = texto
      saida_texto = f'{pt1}, {pt2} e {pt3}'
    

    print(f'Resultado: {resultado:.2f}')
    print(f'Número é {saida_texto}.')

fazer_operacao_e_classificar(20, 12, '+')
    