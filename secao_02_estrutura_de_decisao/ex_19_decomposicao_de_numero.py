"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""

    if numero > 999:
        return 'O número precisa ser menor que 1000'
    elif numero < 0 :
        return 'O número precisa ser positivo'
    else:
        obj_numero = numero
        unidade = int(obj_numero % 10)
        obj_numero = int((obj_numero - unidade) / 10)
        dezena = int(obj_numero % 10)
        centena = int(obj_numero / 10)

        texto = []
        if centena == 1:
            texto.append('1 centena')
        elif centena > 0:
            texto.append(f'{centena} centenas')
        if dezena == 1:
            texto.append('1 dezena')
        elif dezena > 0:
            texto.append(f'{dezena} dezenas')
        if unidade == 1:
            texto.append('1 unidade')
        elif unidade > 0:
            texto.append(f'{unidade} unidades')
        
        if len(texto) == 1:
            decomp = texto.pop()
        elif len(texto) == 2:
            pt1, pt2 = texto
            decomp = f'{pt1} e {pt2}'
        else:
            pt1, pt2, pt3 = texto
            decomp = f'{pt1}, {pt2} e {pt3}'
        return f'{numero} = {decomp}'