from catalogo import carregar_dados
from listar import listar_filmes_detalhado
from utils import menu_busca
from busca import buscar_por_titulo, buscar_por_genero
from utils import menu_ordenacao
from ordenacao import ordenar_catalogo
from cadastro import cadastrar_filmes



def menu():
    print("===============================")
    print("     CATÁLOGO DE FILMES 🎬")
    print("===============================\n")
    print("1. Listar todos os filmes")
    print("2. Buscar filme")
    print("3. Ordenar filmes")
    print("4. Cadastrar novo filme")
    print("5. Sair")

    opcao = input("\nEscolha uma opção: ")
    return opcao

def main():
    catalogo = carregar_dados()
    while True:
        opcao = menu()
        if opcao == '1':
            print(f"Lista de filmes: ")
            print(listar_filmes_detalhado(catalogo))
            pass
        elif opcao == '2':
            menu_busca(catalogo)

            pass

        elif opcao == '3':
            menu_ordenacao(catalogo)
            pass
        
        elif opcao == '4':
           catalogo = cadastrar_filmes(catalogo)
           pass

        elif opcao == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
