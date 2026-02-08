from colorama import Fore, Style

# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10

def impar_par(numero):
    return "par" if numero % 2 == 0 else "impar"

def soma_type():
    while True:
        tipo = input("\nVoce deseja somar os pares ou imapares?[I/P] ").strip()
        if tipo.lower() == "i" or tipo.lower() == "impar" or tipo.lower() == "imapares":
            tipo = "impar"
            break
        elif tipo.lower() == "p" or tipo.lower() == "par" or tipo.lower() == "pares":
            tipo = "par"
            break
        else:
            print(f"{Fore.YELLOW}Opcao invalida. Tente novamente{Style.RESET_ALL}")

    return tipo

def validar_intervalo(intervalo):
    if len(intervalo) != 2:
        return False

    try:
        inicio = int(intervalo[0])
        final = int(intervalo[1])
        return inicio, final
    except:
        return False

def soma_intervalo():
    while True:
        intervalo = input("\nQual intervalo voce deseja somar?(Divida a resposta com ';' Ex: 1;10) ").split(";")

        intervalo_valido = validar_intervalo(intervalo)
        if not intervalo_valido:
            print(f"{Fore.YELLOW}Valor de intervalo invalido, o valor deve ter o seguinte formato: 'Valor Inicio;Valor Final'. Tente novamente{Style.RESET_ALL}")
        else:
            break

    return intervalo_valido

def main():
    print("Este e um sistema que soma numeros imapares ou pares entre um determinado intervalo")

    inicio, final = soma_intervalo()
    tipo = soma_type()

    soma = 0
    for num in range(int(inicio), int(final)):
        if impar_par(num) == tipo:
            soma += num

    print(f"\nA soma dos numeros {tipo.title()} no intervalo {inicio}-{final} e {soma}")

if __name__ == "__main__":
    main()