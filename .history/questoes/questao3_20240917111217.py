"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média 
mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
Estes dias devem ser ignorados no cálculo da média;
"""

import json
import questoes

# Função para carregar dados do JSON
def carregar_faturamento():

    with open('questoes/faturamento.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

# Função para processar o faturamento
def processar_faturamento(dados):
    # Filtrar dias com faturamento maior que 0
    faturamento_validos = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

    if not faturamento_validos:
        print("Não há dados de faturamento válidos.")
        return

    # Cálculos
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

    # Contar os dias com faturamento superior à média
    dias_acima_da_media = sum(1 for dia in faturamento_validos if dia > media_faturamento)

    # Exibir resultados
    print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

# Caminho para o arquivo JSON
caminho_arquivo = 'questoes/faturamento.json'

# Carregar e processar os dados
dados_faturamento = carregar_faturamento(caminho_arquivo)
processar_faturamento(dados_faturamento)