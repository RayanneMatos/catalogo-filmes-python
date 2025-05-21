import pandas as pd

# Caminho do arquivo CSV (pode usar URL RAW ou caminho local)
CSV_PATH = "https://raw.githubusercontent.com/RayanneMatos/catalogo-filmes-python/refs/heads/main/dados/movies_catalog_clean.csv"

# Colunas que você quer manter
colunas_uteis = [
    'title',
    'release_date',
    'genres_names',
    'vote_average',
    'overview',
    'runtime',
    'original_language',
    'budget',
    'revenue'
]

def carregar_dados():
    df = pd.read_csv(CSV_PATH)

    # Filtra colunas úteis
    df = df[colunas_uteis]

    # Remove valores ausentes
    df = df.dropna(subset=['title', 'release_date'])

    # Converte para lista de dicionários
    catalogo = df.to_dict(orient='records')

    return catalogo
