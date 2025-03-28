valor = int(input("Diga o valor das compras:"))

if valor > 500:
    taxa = (valor - 500) * 1.5
    valor_taxado = taxa + 500
    print(f"Valor acima de R$500. Valor com taxa de 50%: {valor_taxado}")

else:
    print("Livre de taxa")
