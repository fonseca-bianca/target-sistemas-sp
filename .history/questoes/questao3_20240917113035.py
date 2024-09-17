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

import json # pra ler o arquivo json 
import os

# caminho pro arquivo json (script e arq estão na mesma pasta 'questoes')
caminho_arquivo = os.path.join(os.path.dirname(__file__), 'faturamento.json')

# função pra carregar dados do arq json
def carregar_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)

# função pra processar o faturamento
def processar_faturamento(dados): # recebe 'dados'
    # faturamenrto > 0
    faturamento_dias = [dia['faturamento'] # adc valor faturamento.json à lista 'faturamento_dias'
        for dia in dados 
            if dia['faturamento'] > 0]

    if not faturamento_dias:
        print("Não há dados de faturamento válidos.")
        return

    # calcular: menor fat, maior fat, media
    menor_faturamento = min(faturamento_dias)
    print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
    maior_faturamento = max(faturamento_dias)
    print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
    media_faturamento = sum(faturamento_dias) / len(faturamento_dias)
    

    # dias faturamento diário foi superior à média mensal
    dias_acima_da_media = sum(1 for dia in faturamento_dias if dia > media_faturamento)
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
    
# carregamento e processamento dos dados
dados_faturamento = carregar_faturamento(caminho_arquivo)
processar_faturamento(dados_faturamento)