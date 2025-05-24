from catalogo import carregar_dados
from cadastro import cadastrar_filmes  
from listar import listar_fimes_detalhado

def menu():
    print("===============================")
    print("     CATÁLOGO DE FILMES 🎬")
    print("===============================\n")
    print("1. Listar todos os filmes")
    print("2. Buscar filme por título")
    print("3. Ordenar filmes")
    print("4. Ver detalhes de um filme")
    print("5. Cadastrar novo filme")
    print("6. Sair")

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
            # buscar_filme(catalogo)
            pass
        elif opcao == '3':
            # ordenar_filmes(catalogo)
            pass
        elif opcao == '4':
            # ver_detalhes(catalogo)
            pass
        elif opcao == '5':
            catalogo = cadastrar_filmes(catalogo)
        elif opcao == '6':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
