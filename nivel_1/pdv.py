compras = {}
print("=== PDV - Ponto de Venda ===")
while True:
    valor = float(input("\nValor da compra em R$ (0 para encerrar): "))
    if valor < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.")
        continue
    if valor == 0:
        break
    idade = int(input("Idade do Cliente:"))
    while idade<0:
        print("Aviso: a idade não pode ser negativa. Tente novamente.")
        idade = int(input("Idade do Cliente: "))
        final = valor

    if idade >= 65:
        final = rund(final * 0.80, 2)

    if final > 100:
        final=round(final * 0.90, 2)

    compras.append([valor, final])
    print(f"Valor final: R$
    {final:.2f}")

total_bruto = 0
total_final = 0
for compra in compras:
    total_bruto += compras[0]
    total_final += compras[1]
total_descontos = total_bruto-total_final
"
print("\n=== RESUMO DO DIA ===")
print(f"Quantidade de compras: {len(compras)}")



