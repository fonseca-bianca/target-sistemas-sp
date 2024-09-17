"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""


def obter_palavra():
    while True:
        entrada = input("Insira uma palavra: ")
        if somente_letras(entrada):
            def somente_letras(entrada):
    # Verifica manualmente se todos os caracteres são letras
                for caractere in entrada:
                    if not ('a' <= caractere <= 'z' or 'A' <= caractere <= 'Z'):
                        return False
                return True
            return entrada
        else:
            print("Erro: A entrada deve conter somente letras.")

# Obtém uma palavra válida do usuário
palavra_inserida = obter_palavra()

# Inverte a palavra
palavra_invertida = palavra_inserida[::-1]

# Exibe o resultado
print(f"A palavra inserida '{palavra_inserida}' ficou invertida para: {palavra_invertida}")