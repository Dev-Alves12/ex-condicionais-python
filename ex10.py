renda = float(input('Digite o vaolr da sua renda mensal: '))
parcela = float(input('Digite a parcela desejada: '))

if renda > 2000 and parcela <= 0.3 * renda:
    print('Empréstimo aprovado!')
elif renda <= 2000:
    print('Empréstimo Negado: renda insufuciente.')
else:
    print('Empréstimo negado: parcela asima de 30% da renda')
