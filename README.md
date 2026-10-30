# projeto-desafio1
# O que o código faz?
Simula um Ponto de Venda que calcula o valor final de cada compra aplicando descontos progressivos: um por idade do cliente e outro por valor da compra. O programa aceita várias compras seguidas, guarda todas em uma lista, e, ao encerrar, mostra um resumo do dia.
# Como ele faz?
Primeiro, pede o valor da compra, se for negativo, avisa e pede de novo. Se for 0, encerra o loop;
Pede a idade do cliente, se for negativa, avisa e pede de novo. Se a idade for maior ou igual a 65 anos, aplica 20% de desconto. Se o valor já descontado pela idade for maior que 100, aplica mais 10% sobre esse valor.
Arrendoda para duas casas decimais, mostra o valor final (ex.:R$144,00) e guarda [valor_original, valor_final] na lista com .append().
Ao digitar 0. percorre a lista com for e mostra: quantidade de compras, total bruto, total de descontos e total final.
# Como rodar?
python pdv.py
# Tabela de exemplos
Valor (R$)	Idade	Desconto idade	Desconto valor	Valor final esperado
1	50,00	30	0%	0%	50,00
2	100,00	30	0%	0%	100,00
3	80,00	65	20%	0%	64,00
4	100,00	70	20%	0%	80,00
5	125,00	70	20%	0%	100,00
6	200,00	30	0%	10%	180,00
7	101,00	30	0%	10%	90,90
8	200,00	65	20%	10%	144,00
9	1000,00	80	20%	10%	720,00
10	200,00	64	0%	10%	180,00

