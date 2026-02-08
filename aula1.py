import time
from colorama import Fore, Style

restaurantes = []

def alert(mensagem):
    """Funcao de confirmacao com padrao de valores sim ou nao"""
    while True:
        confirmacao = input(f"{mensagem}")
        if confirmacao.lower() == "s" or confirmacao.lower() == "sim":
            return True
        elif confirmacao.lower() == "n" or confirmacao.lower() == "nao":
            return False
        else:
            print(f"{Fore.YELLOW}Opcao invalida. Tente novamente{Style.RESET_ALL}")

def verificar_registros():
    """Verifica se existem registros"""
    if not restaurantes:
        print(f"{Fore.YELLOW}\nNenhum restaurante cadastrado{Style.RESET_ALL}")
        input("\nPress enter para voltar ao menu de opcoes")
        main()

def sair():
    """Finaliza o programa"""

    print("\nEncerrando programa...")
    exit()

def alterar_status():
    """Permite ativar o restaurante ou desativar"""

    verificar_registros()

    print(f"{Fore.CYAN}\nAlterar status restaurante{Style.RESET_ALL}")
    while True:
        restaurante_nome = input("Digite o nome do restaurante que deseja alterar o status: ").strip()
        for restaurante in restaurantes:
            if restaurante_nome.lower() == restaurante["nome"].lower():
                status = "Ativo" if restaurante["ativo"] else "Desativo"
                status_acao = "Desativar" if restaurante["ativo"] else "Ativar"

                if not alert(f"\nO restaurante {restaurante["nome"]} esta com o status de {status} deseja {status_acao}?[S/N] "):
                    main()

                status_registro = False if restaurante["ativo"] else True
                restaurante["ativo"] = status_registro
                print(f"{Fore.GREEN}\nStatus alterado com sucesso!{Style.RESET_ALL}")
                break
        else:
            print(f"{Fore.YELLOW}\nNenhum restaurante encontrado de acordo os parametros passados{Style.RESET_ALL}")

        if alert(f"\nDeseja alterar o status de mais um restaurante?[S/N] "):
            break
        else:
            main()

def listar_restaurante():
    """Lista todos os registros com nome, categoria e statuss"""

    verificar_registros()

    print(f"{Fore.CYAN}\nListando restaurantes...{Style.RESET_ALL}")
    for restaurante in restaurantes:
        status = " - Ativo" if restaurante["ativo"] else ""
        print(f". {restaurante["nome"]} - {restaurante["categoria"]}{status}")
        time.sleep(.1)

    input("\nPress enter para voltar ao menu de opcoes")
    main()

def cadastrar_restaurante():
    """Cadastra restaurante com nome e categoria"""

    print(f"{Fore.CYAN}\nCadastro de novos restaurantes{Style.RESET_ALL}")
    while True:
        nome_restaurante = input("Digite o nome do novo restaurante: ").strip()
        categoria = input("Digite a cetegoria do novo restaurante: ").strip()

        if not alert("\nCorfimar cadastro?[S/N] "):
            main()

        if nome_restaurante == "" or categoria == "":
            print(f"{Fore.YELLOW}\nDados invalidos para registro. Tente novamente\n{Style.RESET_ALL}")
            continue

        for restaurante in restaurantes:
            if restaurante["nome"].lower() == nome_restaurante.lower() and restaurante["categoria"].lower() == categoria.lower():
                print(f"{Fore.YELLOW}\nO restaurante {nome_restaurante} ja esta cadastrado!{Style.RESET_ALL}")
                break
        else:
            registro = {
                "nome": nome_restaurante,
                "categoria": categoria,
                "ativo": False
            }

            restaurantes.append(registro)
            print(f"{Fore.GREEN}\nO restaurante {nome_restaurante} foi cadastrado com sucesso!{Style.RESET_ALL}")

        if not alert("\nDeseja cadastrar mais um restaurante?[S/N] "):
            main()

opcoes = {
    "1": {"opcao": "Cadastrar restaurante", "funcao": cadastrar_restaurante},
    "2": {"opcao": "Listar restaurante", "funcao": listar_restaurante},
    "3": {"opcao": "Alterar status restaurante", "funcao": alterar_status},
    "4": {"opcao": "Sair", "funcao": sair},
}

def escolher_opcao():
    """Apresenta as opcoes do sistema e valida a opcao escolhida"""

    for opcao_num, opcao in opcoes.items():
        print(f"{opcao_num}. {opcao["opcao"]}")

    opcao_valida = False
    while True:
        opcao_escolhida = input("\nEscolha uma opção: ")
        if opcao_escolhida in opcoes:
            break
        for opcao in opcoes.values():
            if opcao_escolhida in opcao["opcao"]:
                opcao_valida = True
                break

        if opcao_valida:
            break
        else:
            print(f"{Fore.YELLOW}Opcao invalida. Tente novamente...{Style.RESET_ALL}")

    return opcao_escolhida

def main():
    print(f"\n{Fore.CYAN}Sabor Express{Style.RESET_ALL}")

    opcao_escolhida = escolher_opcao()
    if opcao_escolhida in opcoes.keys():
        opcao_text = opcoes[opcao_escolhida]["opcao"]
        opcao_num = opcao_escolhida
    else:
        for chave, opcao in opcoes.items():
            if opcao_escolhida in opcao["opcao"]:
                opcao_text = opcao_escolhida
                opcao_num = chave
                break

    print(f"Você escolheu a opção {opcao_text}")

    funcao = opcoes[opcao_num]["funcao"]
    funcao()

if __name__ == "__main__":
    main()