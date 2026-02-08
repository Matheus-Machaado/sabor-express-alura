from colorama import Fore, Style

# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

def selecionar_ordem():
    while True:
        tipo = input("\nEm qual sequencia voce deseja imprimir os valores desse intervalo decrescente ou crescente?[D/C] ").strip()
        if tipo.lower() == "d" or tipo.lower() == "decrescente":
            return "decrescente"
        elif tipo.lower() == "c" or tipo.lower() == "crescente":
            return "crescente"
        else:
            print(f"{Fore.YELLOW}Opcao invalida. Tente novamente{Style.RESET_ALL}")

def validar_intervalo(intervalo):
    if len(intervalo) != 2:
        return None

    try:
        inicio = int(intervalo[0].strip())
        final = int(intervalo[1].strip())
        if inicio >= final:
            return None

        return inicio, final
    except:
        return None

def selecionar_intervalo():
    while True:
        intervalo = input("\nQual intervalo voce deseja apresentar?(Divida a resposta com ';' Ex: 1;10) ").split(";")

        intervalo_valido = validar_intervalo(intervalo)
        if not intervalo_valido:
            print(f"{Fore.YELLOW}Valor de intervalo invalido, o valor deve ter o seguinte formato: 'Valor Inicio;Valor Final'. Tente novamente{Style.RESET_ALL}")
        else:
            return intervalo_valido

def main():
    print(f"{Fore.CYAN}Este e um sistema onde voce seleciona um intervalo e a foram como quer que os numeros sejam apresentados{Style.RESET_ALL}")

    inicial, final = selecionar_intervalo()
    ordem = selecionar_ordem()

    print(f"\n{Fore.GREEN}Resultado:{Style.RESET_ALL}")
    if ordem == "crescente":
        for numero in range(inicial, final + 1):
            print(numero)
    else:
        for numero in range(final, inicial - 1, -1):
            print(numero)

if __name__ == "__main__":
    main()