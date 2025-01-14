import json

# Carregar os dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Filtrar os dias com faturamento
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular o menor e o maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamentos) / len(faturamentos)

# Calcular o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")