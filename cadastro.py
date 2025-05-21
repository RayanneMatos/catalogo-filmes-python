# Módulo para cadastrar filmes

import csv

CSV_PATH_LOCAL = "dados/movies_catalog_clean.csv"

def input_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor != "":
            return valor
        print("⚠️ Campo obrigatório. Tente novamente.")

def input_float(mensagem):
    while True:
        valor = input_obrigatorio(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("⚠️ Digite um número válido (use ponto, não vírgula).")

def input_int(mensagem):
    while True:
        valor = input_obrigatorio(mensagem)
        try:
            return int(valor)
        except ValueError:
            print("⚠️ Digite um número inteiro válido.")

def cadastrar_filmes(catalogo):
    print("\n=== Cadastrar Novo Filme ===")

    while True:
        title = input_obrigatorio("Título do filme: ")
        release_date = input_obrigatorio("Data de lançamento (AAAA-MM-DD): ")
        genres = input_obrigatorio("Gêneros (separados por vírgula): ")
        vote_average = input_float("Nota média (ex: 7.5): ")
        overview = input_obrigatorio("Descrição do filme: ")
        runtime = input_int("Duração (em minutos): ")
        original_language = input_obrigatorio("Idioma original (ex: en, pt, es): ")
        budget = input_int("Orçamento (em dólares): ")
        revenue = input_int("Receita (em dólares): ")

        filme = {
            "title": title,
            "release_date": release_date,
            "genres_names": ", ".join([g.strip() for g in genres.split(",")]),
            "vote_average": vote_average,
            "overview": overview,
            "runtime": runtime,
            "original_language": original_language,
            "budget": budget,
            "revenue": revenue
        }

        catalogo.append(filme)

        # Append filme no CSV
        with open(CSV_PATH_LOCAL, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            fieldnames = [
                "title", "release_date", "genres_names", "vote_average", "overview",
                "runtime", "original_language", "budget", "revenue"
            ]
            escritor = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)
            escritor.writerow(filme)

        print(f"\n✅ Filme '{title}' cadastrado com sucesso!\n")

        continuar = input("Deseja cadastrar outro filme? (s/n): ").strip().lower()
        if continuar != 's':
            break
