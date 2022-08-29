"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


from statistics import mean


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""

    veiculos = []
    acidentes = []
    acidentes_menos_150k = []

    for i in range(len(cidades)):
        veiculos.append(cidades[i][1])
        acidentes.append(cidades[i][2])

    sjc_veiculos = acidentes[0] * 1000 / veiculos[0]
    sp_veiculos = acidentes[1] * 1000 / veiculos[1]
    bh_veiculos = acidentes[2] * 1000 / veiculos[2]
    fz_veiculos = acidentes[3] * 1000 / veiculos[3]
    fl_veiculos = acidentes[4] * 1000 / veiculos[4]

    lista_indice = [sjc_veiculos, sp_veiculos, bh_veiculos, fz_veiculos, fl_veiculos]

    maior_indice = max(lista_indice)
    menor_indice = min(lista_indice)
    media_veiculos = mean(veiculos)
    
    media_acidentes = mean(veiculo[2] for veiculo in cidades if veiculo[1] <= 150000)


    index_cidade_maior_acidente = lista_indice.index(maior_indice)
    nome_cidade_maior_indice = cidades[index_cidade_maior_acidente][0]
    index_cidade_menor_acidente = lista_indice.index(menor_indice)
    nome_cidade_menor_indice = cidades[index_cidade_menor_acidente][0]

    print(f'O maior índice de acidentes é de {nome_cidade_maior_indice}, com {maior_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {nome_cidade_menor_indice}, com {menor_indice:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media_veiculos}.')
    print(
        f'A média de acidentes total nas cidades com menos de 150 mil carros é de '
        f'{media_acidentes:.1f} acidentes.'
    )