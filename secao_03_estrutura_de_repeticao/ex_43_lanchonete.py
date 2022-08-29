"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""

    # Cachorro Quente 100     R$ 1,20
    cod_100_status = False
    especificacao_cod_100 = "Cachorro Quente"
    cod_100 = 100
    vl_un_cod_100 = 1.20
    quantidade_cod_100 = 0
    vl_total_cod_100 = 0
    # Bauru Simples   101     R$ 1,30
    cod_101_status = False
    especificacao_cod_101 = "Bauru Simples"
    cod_101 = 101
    vl_un_cod_101 = 1.30
    quantidade_cod_101 = 0
    vl_total_cod_101 = vl_un_cod_101 * quantidade_cod_101
    # Bauru com ovo   102     R$ 1,50
    cod_102_status = False
    especificacao_cod_102 = "Bauru com Ovo"
    cod_102 = 102
    vl_un_cod_102 = 1.50
    quantidade_cod_102 = 0
    vl_total_cod_102 = vl_un_cod_102 * quantidade_cod_102
    # Hambúrguer      103     R$ 1,20
    cod_103_status = False
    especificacao_cod_103 = "Hamburger"
    cod_103 = 103
    vl_un_cod_103 = 1.20
    quantidade_cod_103 = 0
    vl_total_cod_103 = vl_un_cod_103 * quantidade_cod_103
    # Cheeseburguer   104     R$ 1,30
    cod_104_status = False
    especificacao_cod_104 = "Cheeseburger "
    cod_104 = 104
    vl_un_cod_104 = 1.30
    quantidade_cod_104 = 0
    vl_total_cod_104 = vl_un_cod_104 * quantidade_cod_104
    # Refrigerante    105     R$ 1,00
    cod_105_status = False
    especificacao_cod_105 = "Refrigerante"
    cod_105 = 105
    vl_un_cod_105 = 1.00
    quantidade_cod_105 = 0
    vl_total_cod_105 = vl_un_cod_105 * quantidade_cod_105

    quantidade_total = 0
    valor_total = 0

    print(
        "_____________________________________________________________________________"
    )
    print(
        "|                              RESUMO DA CONTA                              |"
    )
    print(
        "|---------------------------------------------------------------------------|"
    )
    print(
        "| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |"
    )

    lista_pedido = []

    for codigo, quantidade in itens:
        if codigo == "100":
            cod_100_status = True
            quantidade_cod_100 += quantidade
            vl_total_cod_100 = vl_un_cod_100 * quantidade_cod_100
        elif codigo == "101":
            cod_101_status = True
            quantidade_cod_101 += quantidade
            vl_total_cod_101 = vl_un_cod_101 * quantidade_cod_101
        elif codigo == "102":
            cod_102_status = True
            quantidade_cod_102 += quantidade
            vl_total_cod_102 = vl_un_cod_102 * quantidade_cod_102
        elif codigo == "103":
            cod_103_status = True
            quantidade_cod_103 += quantidade
            vl_total_cod_103 = vl_un_cod_103 * quantidade_cod_103
        elif codigo == "104":
            cod_104_status = True
            quantidade_cod_104 += quantidade
            vl_total_cod_104 = vl_un_cod_104 * quantidade_cod_104
        elif codigo == "105":
            cod_105_status = True
            quantidade_cod_105 += quantidade
            vl_total_cod_105 = vl_un_cod_105 * quantidade_cod_105

    if cod_100_status:
        quantidade_total += quantidade_cod_100
        valor_total += vl_total_cod_100
        lista_pedido.append(especificacao_cod_100)
        lista_pedido.append(cod_100)
        lista_pedido.append(vl_un_cod_100)
        lista_pedido.append(quantidade_cod_100)
        lista_pedido.append(vl_total_cod_100)
        pt1, pt2, pt3, pt4, pt5 = lista_pedido
        print(
            f"| {pt1:16} | {pt2}    | {pt3:<19.2f} | {pt4:10} | {pt5:10.2f} |"
        )
        lista_pedido.clear()
    if cod_101_status:
        quantidade_total += quantidade_cod_101
        valor_total += vl_total_cod_101
        lista_pedido.append(especificacao_cod_101)
        lista_pedido.append(cod_101)
        lista_pedido.append(vl_un_cod_101)
        lista_pedido.append(quantidade_cod_101)
        lista_pedido.append(vl_total_cod_101)
        pt1, pt2, pt3, pt4, pt5 = lista_pedido
        print(
            f"| {pt1:16} | {pt2}    | {pt3:<19.2f} | {pt4:10} | {pt5:10.2f} |"
        )
        lista_pedido.clear()
    if cod_102_status:
        quantidade_total += quantidade_cod_102
        valor_total += vl_total_cod_102
        lista_pedido.append(especificacao_cod_102)
        lista_pedido.append(cod_102)
        lista_pedido.append(vl_un_cod_102)
        lista_pedido.append(quantidade_cod_102)
        lista_pedido.append(vl_total_cod_102)
        pt1, pt2, pt3, pt4, pt5 = lista_pedido
        print(
            f"| {pt1:16} | {pt2}    | {pt3:<19.2f} | {pt4:10} | {pt5:10.2f} |"
        )
        lista_pedido.clear()
    if cod_103_status:
        quantidade_total += quantidade_cod_103
        valor_total += vl_total_cod_103
        lista_pedido.append(especificacao_cod_103)
        lista_pedido.append(cod_103)
        lista_pedido.append(vl_un_cod_103)
        lista_pedido.append(quantidade_cod_103)
        lista_pedido.append(vl_total_cod_103)
        pt1, pt2, pt3, pt4, pt5 = lista_pedido
        print(
            f"| {pt1:16} | {pt2}    | {pt3:<19.2f} | {pt4:10} | {pt5:10.2f} |"
        )
        lista_pedido.clear()
    if cod_104_status:
        quantidade_total += quantidade_cod_104
        valor_total += vl_total_cod_104
        lista_pedido.append(especificacao_cod_104)
        lista_pedido.append(cod_104)
        lista_pedido.append(vl_un_cod_104)
        lista_pedido.append(quantidade_cod_104)
        lista_pedido.append(vl_total_cod_104)
        pt1, pt2, pt3, pt4, pt5 = lista_pedido
        print(
            f"| {pt1:16} | {pt2}    | {pt3:<19.2f} | {pt4:10} | {pt5:10.2f} |"
        )
        lista_pedido.clear()
    if cod_105_status:
        quantidade_total += quantidade_cod_105
        valor_total += vl_total_cod_105
        lista_pedido.append(especificacao_cod_105)
        lista_pedido.append(cod_105)
        lista_pedido.append(vl_un_cod_105)
        lista_pedido.append(quantidade_cod_105)
        lista_pedido.append(vl_total_cod_105)
        pt1, pt2, pt3, pt4, pt5 = lista_pedido
        print(
            f"| {pt1:16} | {pt2}    | {pt3:<19.2f} | {pt4:10} | {pt5:10.2f} |"
        )
        lista_pedido.clear()






    print(
        "|---------------------------------------------------------------------------|"
    )
    print(
        f"| Total Geral:                                    | {quantidade_total:10} | {valor_total:10.2f} |"
    )
    print(
        "-----------------------------------------------------------------------------"
    )
