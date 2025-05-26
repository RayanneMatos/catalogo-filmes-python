# Módulo para ordenação

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
        # Compara usando a chave, para 'release_date' extrair o ano
        if comparar(lista[j], pivot, chave):
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

def comparar(a, b, chave):
    # Extrai valor comparável conforme chave
    va = extrair_valor(a, chave)
    vb = extrair_valor(b, chave)
    return va <= vb

def extrair_valor(filme, chave):
    if chave == "title":
        return filme["title"].lower()
    elif chave == "ano":
        # Extrai ano do formato 'YYYY-MM-DD'
        return int(filme["release_date"][:4])
    elif chave == "nota":
        return float(filme["vote_average"])
    else:
        # Caso chave inválida, ordena por título como padrão
        return filme["title"].lower()

def ordenar_catalogo(catalogo, chave_ordenacao):
    quick_sort(catalogo, chave_ordenacao)
