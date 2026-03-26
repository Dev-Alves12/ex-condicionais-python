quantidade_maça = int(input('Digite a quantidade de maçãs vendidas: '))
quantidade_bananas = int(input('Digite a quantidade de bananas vendidas: '))
if quantidade_bananas > quantidade_maça:
    print('As bananas tiveram maior venda!')
elif quantidade_maça > quantidade_bananas:
    print('As maçãs tiveram melhor venda!')
else:
    print('As vendas foram Iguais.')