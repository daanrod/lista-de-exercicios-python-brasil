"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""

from statistics import mean


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""

    gabarito = ("A", "B", "C", "D", "E", "E", "D", "C", "B", "A")

    notas = []

    print(f'Aluno                 Nota')

    for prova in provas:
        nome_aluno = prova[0]
        nota = 0
        respostas = []

        for i in prova[1:]:
            respostas.append(i)

        for questao, correta in zip(gabarito, respostas):
            if questao == correta:
                nota += 1
        print(f'{nome_aluno:21s} {nota:2d}')
        notas.append(nota)

    menor_nota = min(notas)
    maior_nota = max(notas)
    media_geral = mean(notas)
    total_alunos = len(provas)

    print(f'---------------------------')
    print(f'Média geral: {media_geral:.1f}')
    print(f'Maior nota: {maior_nota}')
    print(f'Menor nota: {menor_nota}')
    print(f'Total de Alunos: {total_alunos}')
