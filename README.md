# Catálogo de Filmes – Estrutura de Dados

Projeto desenvolvido para a disciplina de **Estrutura de Dados** do curso de **Ciência da Computação**, com foco em aplicação prática de algoritmos e estruturas como listas, buscas e ordenações.

---

## Objetivo
Criar um sistema simples em Python para cadastrar, listar, buscar e ordenar filmes, utilizando conceitos fundamentais de estrutura de dados.

---

##  Conceitos abordados
- Listas e dicionário
- Busca Linear
- Ordenação (Bubble Sort e Quick/Merge Sort)
- Modularização em Python
- Entrada/saída de dados
- Menu interativo

---

##  Funcionalidades
- Cadastro de filmes
- Listagem de todos os filmes cadastrados
- Busca por título, diretor ou gênero
- Ordenação por título, ano de lançamento ou nota
- Menu interativo no terminal

### Cadastro


### Listagem
A listagem dos filmes cadastrados se trata de um a parte de um sistema maior de gerenciamento de catálogo de filmes. Este trecho de código em Python é o responsável por listar de forma detalhada e intuitiva, as informações sobre os filmes já cadastrados no sistema.

A estrutura do código se inicia com a importação de alguns elementos importantes para o funcionamento do código, como:

- import csv: embora o módulo csv seja importado, ele não é utilizado diretamente neste trecho, indicando que sua funcionalidade pode estar presente na função carregar_dados.

- carregar_dados: função importada do módulo catalogo, responsável por carregar os dados dos filmes.

- CSV_PATH_LOCAL: constante que define o caminho do arquivo de origem dos dados (não utilizada diretamente no código apresentado).

Já com a função listar_filmes_detalhado temos a principal funcionalidade do código. Essa função recebe uma lista de filmes e imprime as informações recebidas de maneira detalhada e organizada.
Estrutura da função:

- Verificação de lista vazia: caso não haja filmes, uma mensagem é exibida ao usuário.

      def listar_filmes_detalhado(filmes):
        if not filmes:
            print("Nenhum filme cadastrado para listar.")
            return

- Dicionário de idiomas: a função utiliza um dicionário idiomas_map para converter siglas de idiomas em nomes completos (por exemplo, 'en' → 'English') com intuito de trazer uma interface mais compreensível para o usuário.

        idiomas_map = {
            'en': 'English', ...
        }
    
Laço de repetição: percorre a lista de filmes e imprime os seguintes dados:
    	
- Título
- Data de lançamento
- Gêneros (formatados como lista separada por vírgulas)
- Média de votos (com uma casa decimal)
- Descrição (sinopse)
-  Duração em minutos
- Linguagem original (convertida com base na sigla)
- Orçamento e receita (formatados com separadores de milhar)

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

Por fim o trecho if __name__ == "__main__" garante que o código será executado apenas quando o arquivo for executado diretamente (não quando for importado como módulo). Nele:

- Os dados dos filmes são carregados via carregar_dados.
- A função listar_filmes_detalhado é chamada para exibir as informações dos filmes.
  
        if __name__ == "__main__":
            catalogo_filmes = carregar_dados()
            listar_filmes_detalhado(catalogo_filmes)

### Busca

### Ordenação

### Menu

---

## ▶ Como executar

```bash
python main.py
