import csv
from catalogo import carregar_dados
CSV_PATH_LOCAL = "dados/movies_catalog_clean.csv"

def listar_filmes_detalhado(filmes):
    if not filmes:
        print("Nenhum filme cadastrado para listar.")
        return

    # Dicionário de mapeamento de siglas para nomes de idiomas
    idiomas_map = {
        'en': 'English',
        'fr': 'French',
        'es': 'Spanish',
        'de': 'German',
        'it': 'Italian',
        'ja': 'Japanese',
        'ko': 'Korean',
        'zh': 'Chinese',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'hi': 'Hindi',
        'ar': 'Arabic',
        '' : 'Desconhecida'
    }

    print("--- Filmes Cadastrados ---")
    for i, filme in enumerate(filmes):
        print(f"\n--- Filme {i+1}: {filme['title']} ---")
        print(f"Título: {filme.get('title', 'Título Desconhecido')}")
        print(f"Ano de Lançamento: {filme.get('release_date', 'N/A')}")
        print(f"Gêneros: {', '.join(filme.get('genres_names', ['N/A']))}")
        print(f"Média de Votos: {filme.get('vote_average', 0.0):.1f}")
        print(f"Descrição: {filme.get('overview', 'N/A')}")
        print(f"Duração: {filme.get('runtime', 0)} minutos")

        sigla_idioma = filme.get('original_language', 'N/A')
        nome_idioma = idiomas_map.get(sigla_idioma, sigla_idioma.upper())
        print(f"Linguagem Original: {nome_idioma}")

        print(f"Orçamento: ${filme.get('budget', 0):,}")
        print(f"Receita: ${filme.get('revenue', 0):,}")


if __name__ == "__main__":
    catalogo_filmes = carregar_dados()
    listar_filmes_detalhado(catalogo_filmes)