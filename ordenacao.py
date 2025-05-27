# Módulo para ordenação usando Quick Sort
from listar import listar_filmes_detalhado


def quick_sort(lista, chave, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        p = particao(lista, chave, inicio, fim)
        quick_sort(lista, chave, inicio, p - 1)
        quick_sort(lista, chave, p + 1, fim)

def particao(lista, chave, inicio, fim):
    pivot = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if comparar(lista[j], pivot, chave):
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

def comparar(a, b, chave):
    va = extrair_valor(a, chave)
    vb = extrair_valor(b, chave)
    return va <= vb

def extrair_valor(filme, chave):
    if chave == "title":
        return filme.get("title", "").lower()

    elif chave == "ano":
        data = filme.get("release_date", "")
        try:
            return int(data[:4]) if data else 0
        except ValueError:
            return 0

    elif chave == "nota":
        try:
            return float(filme.get("vote_average", 0.0))
        except ValueError:
            return 0.0

    # Chave inválida: ordena por título como fallback
    return filme.get("title", "").lower()

def ordenar_catalogo(catalogo, chave_ordenacao):
    if not catalogo:
        print("⚠️ Catálogo vazio. Nada a ordenar.")
        return

    if chave_ordenacao not in ["title", "ano", "nota"]:
        print(f"⚠️ Chave de ordenação '{chave_ordenacao}' inválida. Ordenando por título.")
        chave_ordenacao = "title"

    quick_sort(catalogo, chave_ordenacao)
