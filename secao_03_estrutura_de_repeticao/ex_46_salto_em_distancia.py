"""
Exercício 46 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados.

Mostre os valores com uma casa decimal sem arredondar.

    >>> calcular_estatiscas_do_salto('Rodrigo Curvêllo', 6.5, 6.1, 6.2, 5.4, 5.3)
    Atleta: Rodrigo Curvêllo
    ---------------------------------
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    ---------------------------------
    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m
    ---------------------------------
    Resultado final:
    Rodrigo Curvêllo: 5.9 m
    >>> calcular_estatiscas_do_salto('João do Pulo', 6.8, 6.5, 6.1, 6.2, 5.4)
    Atleta: João do Pulo
    ---------------------------------
    Primeiro Salto: 6.8 m
    Segundo Salto: 6.5 m
    Terceiro Salto: 6.1 m
    Quarto Salto: 6.2 m
    Quinto Salto: 5.4 m
    ---------------------------------
    Melhor salto:  6.8 m
    Pior salto: 5.4 m
    Média dos demais saltos: 6.3 m
    ---------------------------------
    Resultado final:
    João do Pulo: 6.3 m

"""


from statistics import mean


def calcular_estatiscas_do_salto(nome, *saltos):
    """Escreva aqui em baixo a sua solução"""

    print(f"Atleta: {nome}")
    print("---------------------------------")

    melhor_salto = max(saltos)
    pior_salto = min(saltos)

    saltos_restantes = []

    for salto in saltos:
        saltos_restantes.append(salto)

    print(f"Primeiro Salto: {saltos[0]} m")
    print(f"Segundo Salto: {saltos_restantes[1]} m")
    print(f"Terceiro Salto: {saltos_restantes[2]} m")
    print(f"Quarto Salto: {saltos_restantes[3]} m")
    print(f"Quinto Salto: {saltos_restantes[4]} m")
    ("---------------------------------")

    saltos_restantes.remove(melhor_salto)
    saltos_restantes.remove(pior_salto)
    media_demais_saltos = mean(saltos_restantes)
    print("---------------------------------")
    print(f"Melhor salto:  {melhor_salto:.1f} m")
    print(f"Pior salto: {pior_salto:.1f} m")
    print(f"Média dos demais saltos: {media_demais_saltos:.1f} m")
    print("---------------------------------")
    print("Resultado final:")
    print(f"{nome}: {media_demais_saltos:.1f} m")
