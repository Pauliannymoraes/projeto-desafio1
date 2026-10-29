# projeto-desafio1
# O que o código faz?
Simula um Ponto de Venda que calcula o valor final de cada compra aplicando descontos progressivos: um por idade do cliente e outro por valor da compra. O programa aceita várias compras seguidas, guarda todas em uma lista, e, ao encerrar, mostra um resumo do dia.
# Como ele faz?
Primeiro, pede o valor da compra, se for negativo, avisa e pede de novo. Se for 0, encerra o loop;
Pede a idade docliente, se for negativa, avisa e pede de novo. Se a idade for maior ou igual a 65, aplica 20% de desconto. Se o valor já descontado pela idade for maio que 100, aplica mais 10% sobre esse valor.
Arrendoda para duas casas decimais, mostra o valor final (ex.:R$144,00) e guarda [valor_original, valor_final] na lista com .append().
Ao digitar 0. percorre a lista com for e mostra: quantidade de compras, total bruto, total de descontos e total final.
# Como rodas?
python pdv.py
# Tabela de exemplos

