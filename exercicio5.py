from colorama import Fore, Style

# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

def main():
    print(f"{Fore.CYAN}Este e um sistema que imprime a tabuada de um número escolhido por voce, indo de 1 a 10{Style.RESET_ALL}")

    while True:
        try:
            numero = int(input("\nDigite o numero que deseja saber os resultados: "))
            break
        except:
            print(f"{Fore.YELLOW}Valor de intervalo invalido. Tente novamente{Style.RESET_ALL}")

    print(f"{Fore.GREEN}\nResultados:{Style.RESET_ALL}")
    for num_calc in range(1, 11):
        resultado = num_calc * numero
        print(f"{num_calc} * {numero} = {resultado}")

if __name__ == "__main__":
    main()