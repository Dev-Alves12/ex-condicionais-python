diaA = int(input('Informe os dias para a atividade A: '))
diaB = int(input('Informe os dias para a atividade B: '))
diaC = int(input('Informe os dias para a atividade C: '))

if (diaA >= 0 and diaB >= 0 and diaC >= 0):
    tempo_real = diaA + diaB + diaC
    print(f'O tempo total do projeto é de {tempo_real} dias. ')
else:
    print('Erro: Os dias não podem ser negativos.')