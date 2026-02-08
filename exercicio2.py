import re

# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições

def classe_idade(idade):
    if idade >= 0 and idade <= 12:
        classe = "Criança"
    elif idade >= 13 and idade <= 18:
        classe = "Adolescente"
    elif idade >= 18 and idade <= 60:
        classe = "Adulto"
    elif idade >= 60 and idade <= 100:
        classe = "Idoso"
    else:
        classe = "Fossil"

    return classe

while True:
    idade = input("\nDigite a sua idade: ")
    try:
        idade_limpa = int(re.sub(r"\D", "", idade))
        break
    except:
        print("Idade inválida. Tente novamente.")

print(f"De acordo com a idade {idade_limpa} voce se enquadra como {classe_idade(idade_limpa)}")