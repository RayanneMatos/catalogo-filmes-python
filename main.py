from catalogo import carregar_dados

def menu():
    print("===============================")
    print("     CATÁLOGO DE FILMES 🎬")
    print("===============================\n")
    print("1. Listar todos os filmes")
    print("2. Buscar filme por título")
    print("3. Ordenar filmes")
    print("4. Ver detalhes de um filme")
    print("5. Sair")

    opcao = input("\nEscolha uma opção: ")
    return opcao

def main():
    catalogo = carregar_dados()
    while True:
        opcao = menu()
        if opcao == '1':
            # listar_filmes(catalogo)
            pass
        elif opcao == '2':
            # buscar_filme()
            pass
        elif opcao == '3':
            # ordenar_filmes()
            pass
        elif opcao == '4':
            # ver_detalhes()
            pass
        elif opcao == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
