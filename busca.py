 # Módulo para buscas

# busca.py

def buscar_por_titulo(catalogo, titulo):
    """Busca linear por título (case insensitive)."""
    resultados = []
    for filme in catalogo:
        if titulo.lower() in filme['title'].lower():
            resultados.append(filme)
    return resultados


def buscar_por_genero(catalogo, genero):
    genero = genero.lower()
    return [
        filme for filme in catalogo
        if any(genero in g.lower() for g in filme['genres_names'])
    ]

