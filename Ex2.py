import json

def menorFaturamento(faturamentoDiario):
    valores = [dia["valor"] for dia in faturamentoDiario]
    return min(valores)

def maiorFaturamento(faturamentoDiario):
    valores = [dia["valor"] for dia in faturamentoDiario]
    return max(valores)

def mediaMensal(faturamentoDiario):
    diasComFaturamento = [dia["valor"] for dia in faturamentoDiario if dia["valor"] > 0]
    return sum(diasComFaturamento) / len(diasComFaturamento)

def contarDiasAcimaDaMedia(faturamentoDiario, media):
    return sum(1 for dia in faturamentoDiario if dia["valor"] > media)

with open('dados.json', 'r') as file:
    faturamentoDiario = json.load(file)

menorValor = menorFaturamento(faturamentoDiario)
maiorValor = maiorFaturamento(faturamentoDiario)

media = mediaMensal(faturamentoDiario)

diasAcimaMedia = contarDiasAcimaDaMedia(faturamentoDiario, media)

print("Menor valor de faturamento diário:", menorValor)
print("Maior valor de faturamento diário:", maiorValor)
print("Número de dias com faturamento diário superior à média mensal:", diasAcimaMedia)
