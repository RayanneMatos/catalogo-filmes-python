from catalogo import carregar_dados
from listar import listar_filmes_detalhado
from utils import menu_busca, menu_ordenacao


def menu():
    print("===============================")
    print("     CATÁLOGO DE FILMES 🎬")
    print("===============================\n")
    print("1. Listar todos os filmes")
    print("2. Buscar filme")
    print("3. Ordenar filmes")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")
    return opcao


def main():
    catalogo = carregar_dados()

    while True:
        opcao = menu()

        if opcao == '1':
            print("Lista de filmes:")
            print(listar_filmes_detalhado(catalogo))

        elif opcao == '2':
            menu_busca(catalogo)

        elif opcao == '3':
            menu_ordenacao(catalogo)

        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
