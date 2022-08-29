"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior (ex_04_crescimento_populacional) permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada (crescimento do país A precisa ser maior que a do país B. Pense na razão dessa
restrição).

    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.03, 200_000, 0.015)
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'
    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.03, 200_000, 0.04)
    'A taxa de crescimento do país B (4.0%) deve ser menor do que a do país A (3.0%)'
    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.05, 200_000, 0.015)
    'População de A, depois de 28 ano(s) será de 313610 pessoas, superando a de B, que será de 303444 pessoas'
    >>> calcular_ano_ultrapassagem_populacional(800_000, 0.05, 200_000, 0.015)
    'População de A, depois de 0 ano(s) será de 800000 pessoas, superando a de B, que será de 200000 pessoas'


"""


def calcular_ano_ultrapassagem_populacional(
        populacao_menor: int, taxa_crescimento_populacao_menor: float, populacao_maior,
        taxa_crescimento_populacao_maior:float ) -> str:
    """Escreva aqui em baixo a sua solução"""

    p1 = int(populacao_menor)
    p2 = int(populacao_maior)
    anos = 0

    crescimento_p1 = taxa_crescimento_populacao_menor
    p1_porcentagem = crescimento_p1 * 100
    crescimento_p2 = taxa_crescimento_populacao_maior
    p2_porcentagem = crescimento_p2 * 100

    while True:
        p1 = p1 + (p1 * crescimento_p1)
        p2 = p2 + (p2 * crescimento_p2)
        anos += 1
        if p1 < p2:
            return f'A taxa de crescimento do país B ({p2_porcentagem:.1f}%) deve ser menor do que a do país A ({p1_porcentagem:.1f}%)'
        if p1 > p2:
            return f'População de A, depois de {anos} ano(s) será de {int(p1)} pessoas, superando a de B, que será de {int(p2)} pessoas'
