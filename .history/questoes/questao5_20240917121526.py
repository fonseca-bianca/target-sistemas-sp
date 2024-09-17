"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# função pra verificar se a string contém somente letras
def verificar_entrada(palavra):
    return palavra.isalpha() # verificar se caracteres são letras

# função pra inverter a string
def inverter_string(palavra):
    palavra_invertida = "" 
    for i in range(len(palavra) - 1, -1, -1): # iteração sobre os índices da string em ordem decrescente
        palavra_invertida += palavra[i] # concatenar 'i' à 'palavra_invertida'
    return palavra_invertida

# loop pra receber e validar a entrada do usuário
while True:
    palavra_inserida = input("Insira uma palavra: ")
    
    # verificar se a entrada é válida
    if verificar_entrada(palavra_inserida):
        palavra_invertida = inverter_string(palavra_inserida)
        print(f"A palavra inserida '{palavra_inserida}' ficou invertida para: {palavra_invertida}")
        break  # sair do loop quando a entrada é válida
    else:
        print("Entrada inválida. Por favor, insira apenas letras.")