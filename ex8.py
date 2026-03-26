distancia = float(input('Digite a distância percorrida (em km): '))

if distancia <= 100:
    print('O valor do pedágio é de R$ 10,00')
elif 100 < distancia <= 200:
    print('O valor do pedágio é de R$ 20,00')
else:
    print('O valor do pedágio é de R$ 30,00')