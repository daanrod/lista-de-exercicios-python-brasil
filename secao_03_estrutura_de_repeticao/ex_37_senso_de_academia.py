"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""

from statistics import mean


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""

    clientes = []
    cliente_peso = []
    cliente_altura = []
    cliente_maior = 0
    cliente_menor = 0
    cliente_mais_magro = 0
    cliente_mais_gordo = 0
    media_altura = 0
    media_peso = 0

    # Informa as opçoes de entrada ao usuario, caso deseje prosseguir o adiciona em uma lista para canditatos ao senso.
    while True:
        nome = input(
            "Digite 0 para encerrar o programa ou o seu nome ser adicionado a lista: "
        )
        if nome == "0":
            break
        altura = int(input("Digite sua altura: "))
        peso = int(input("Digite seu peso: "))
        clientes.append([nome, altura, peso])

    # Separa os pesos e alturas conform a ordem do indice original
    for i in range(len(clientes)):
        cliente_altura.append(clientes[i][1])
        cliente_peso.append(clientes[i][2])

    # Define os valores necessarios para a saida
    cliente_maior = max(cliente_altura)
    cliente_menor = min(cliente_altura)
    cliente_mais_magro = min(cliente_peso)
    cliente_mais_gordo = max(cliente_peso)
    media_altura = mean(cliente_altura)
    media_peso = mean(cliente_peso)

    # Define o nome a quem pertence o dado na saida, conforme a ordem do indice
    cliente_maior_index = cliente_altura.index(cliente_maior)
    nome_maior = clientes[cliente_maior_index][0]
    cliente_menor_index = cliente_altura.index(cliente_menor)
    nome_menor = clientes[cliente_menor_index][0]
    cliente_magro_index = cliente_peso.index(cliente_mais_magro)
    nome_magro = clientes[cliente_magro_index][0]
    cliente_gordo_index = cliente_peso.index(cliente_mais_gordo)
    nome_gordo = clientes[cliente_gordo_index][0]

    print(f"Cliente mais alto: {nome_maior}, com {cliente_maior} centímetros")
    print(f"Cliente mais baixo: {nome_menor}, com {cliente_menor} centímetros")
    print(f"Cliente mais magro: {nome_magro}, com {cliente_mais_magro} kilos")
    print(f"Cliente mais gordo: {nome_gordo}, com {cliente_mais_gordo} kilos")
    print("--------------------------------------------------")
    print(f"Media de altura dos clientes: {media_altura:.1f} centímetros")
    print(f"Media de peso dos clientes: {media_peso:.1f} kilos")
