"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por 
estado:
• SP - R$67.836,43
• RJ - R$36.678,66
• MG - R$29.229,88
• ES - R$27.165,48
• Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora. 
"""

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

percentual_estado = 0

total_faturamento = SP + RJ + MG + ES + Outros

for estado, faturamento in [('SP', SP), ('RJ', RJ), ('MG', MG), ('ES', ES), ('Outros', Outros)]:
    percentual = (faturamento / total_faturamento) * 100
    percentual_estado += percentual 

print(percentual_estado)