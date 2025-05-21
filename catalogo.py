import csv

CSV_PATH_LOCAL = "dados/movies_catalog_clean.csv"

def carregar_dados():
    filmes = []
    with open(CSV_PATH_LOCAL, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            # Convertendo campos numéricos para tipos corretos
            linha['vote_average'] = float(linha['vote_average']) if linha['vote_average'] else 0.0
            linha['runtime'] = int(float(linha['runtime'])) if linha['runtime'] else 0
            linha['budget'] = int(float(linha['budget'])) if linha['budget'] else 0
            linha['revenue'] = int(float(linha['revenue'])) if linha['revenue'] else 0

            # Convertendo gêneros para lista
            linha['genres_names'] = [g.strip() for g in linha['genres_names'].split(",")]

            filmes.append(linha)
    return filmes
