# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def par_ou_impar(numero):
    return "par" if numero % 2 == 0 else "impar"

while True:
    numero = input("Digite um número: ").replace(",",".")
    try:
        numero = float(numero)
        break
    except:
        print("Valor inválido. Tente novamente.\n")

print(f"O numero {numero} e {par_ou_impar(numero).title()}")