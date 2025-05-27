 # Funções auxiliares
from busca import buscar_por_titulo, buscar_por_genero
from ordenacao import ordenar_catalogo
from listar import listar_filmes_detalhado



def menu_busca(catalogo):
    while True:
        print("\n=== 🔍 MENU DE BUSCA ===")
        print("1. Buscar por Título")
        print("2. Buscar por Gênero")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título para buscar: ")
            resultados = buscar_por_titulo(catalogo, titulo)
        elif opcao == "2":
            genero = input("Digite o gênero para buscar: ")
            resultados = buscar_por_genero(catalogo, genero)
        elif opcao == "3":
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")
            continue

        if resultados:
            print(f"\n🎬 Resultados encontrados ({len(resultados)}):\n")
            for filme in resultados:
                print(f"- {filme['title']} ({filme['release_date']})")
        else:
            print("\n❌ Nenhum resultado encontrado.")



def menu_ordenacao(catalogo):
    while True:
        print("\n=== 📊 MENU DE ORDENAÇÃO ===")
        print("1. Ordenar por Título")
        print("2. Ordenar por Ano")
        print("3. Ordenar por Nota")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ordenar_catalogo(catalogo, "title")
            print("\n📚 Catálogo ordenado por título!\n")
            listar_filmes_detalhado(catalogo)
            break
        elif opcao == '2':
            ordenar_catalogo(catalogo, "ano")
            print("\n📅 Catálogo ordenado por ano de lançamento!\n")
            listar_filmes_detalhado(catalogo)
            break
        elif opcao == '3':
            ordenar_catalogo(catalogo, "nota")
            print("\n⭐ Catálogo ordenado por nota!\n")
            listar_filmes_detalhado(catalogo)
            break
        elif opcao == '4':
            print("🔙 Retornando ao menu principal.")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")
