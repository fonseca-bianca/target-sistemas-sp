"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# Função para verificar se a string contém apenas letras
def verificar_entrada(palavra):
    return palavra.isalpha()

# Função para inverter a string
def inverter_string(palavra):
    palavra_invertida = ""
    for i in range(len(palavra) - 1, -1, -1):
        palavra_invertida += palavra[i]
    return palavra_invertida

# Loop para receber e validar a entrada do usuário
while True:
    palavra_inserida = input("Insira uma palavra: ")
    
    # Verificando se a entrada é válida
    if verificar_entrada(palavra_inserida):
        palavra_invertida = inverter_string(palavra_inserida)
        print(f"A palavra inserida '{palavra_inserida}' ficou invertida para: {palavra_invertida}")
        break  # Sai do loop quando a entrada é válida
    else:
        print("Entrada inválida. Por favor, insira apenas letras.")