faturamentoPorEstado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

totalMensal = sum(faturamentoPorEstado.values())

percentuaisPorEstado = {}
for estado, faturamento in faturamentoPorEstado.items():
    percentual = (faturamento / totalMensal) * 100
    percentuaisPorEstado[estado] = percentual

print("Percentual de representação de cada estado no valor total mensal da distribuidora:")
for estado, percentual in percentuaisPorEstado.items():
    print("{}: {:.2f}%".format(estado, percentual))
