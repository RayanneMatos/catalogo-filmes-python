# Catálogo de Filmes – Estrutura de Dados

Projeto desenvolvido para a disciplina de **Estrutura de Dados** do curso de **Ciência da Computação**, com foco em aplicação prática de algoritmos e estruturas como listas, buscas e ordenações.

---

## Objetivo
O principal objetivo deste projeto é desenvolver um sistema de controle de catálogo de filmes utilizando a linguagem Python, com um foco didático e prático na aplicação de Estruturas de Dados e Algoritmos fundamentais. Mais do que apenas criar um gerenciador de filmes, o sistema serve como um laboratório para:

- Consolidar o aprendizado: Aplicar e aprofundar os conhecimentos teóricos adquiridos na disciplina de Estrutura de Dados, transformando conceitos abstratos como listas, dicionários, buscas e ordenações em funcionalidades tangíveis.
- Desenvolver habilidades de programação: Praticar a escrita de código limpo, modularizado e eficiente em Python, explorando boas práticas de organização e design de software.
- Demonstrar a relevância de algoritmos: Ilustrar como diferentes algoritmos de busca (e.g., linear) e ordenação (e.g., Bubble Sort, Quick/Merge Sort) impactam o desempenho e a organização de grandes volumes de dados, permitindo a comparação e análise de suas complexidades.
- Criar uma ferramenta funcional: Construir um sistema interativo e útil que permite ao usuário cadastrar, visualizar, buscar e organizar informações sobre filmes de maneira eficiente, evidenciando a aplicabilidade dos conceitos em cenários reais.
- Em suma, este projeto busca ser uma ponte entre a teoria e a prática, oferecendo uma experiência valiosa na construção de um sistema funcional que evidencia a importância da escolha e implementação correta de estruturas de dados e algoritmos para a otimização de operações em um catálogo de informações.

---

##  Conceitos abordados
- Listas e Dicionários: Utilização de estruturas de dados básicas para armazenar e organizar as informações dos filmes.
- Busca Linear: Implementação de algoritmos de busca para localizar filmes específicos dentro do catálogo.
- Algoritmos de Ordenação (Bubble Sort e Quick/Merge Sort): Aplicação e comparação de diferentes métodos de ordenação para organizar o catálogo de filmes de diversas maneiras.
- Modularização em Python: Organização do código em módulos separados para melhor manutenibilidade e reusabilidade.
- Entrada/Saída de Dados: Manipulação de dados inseridos pelo usuário e exibição de resultados.
- Menu Interativo: Desenvolvimento de uma interface de linha de comando amigável para interação com o usuário.
---

##  Funcionalidades
O sistema oferece as seguintes funcionalidades principais:
- Cadastro de Filmes: Adição de novos filmes ao catálogo, com informações como título, diretor, ano de lançamento, gênero e nota.
- Listagem de Filmes: Visualização de todos os filmes cadastrados.
- Busca de Filmes: Pesquisa por filmes utilizando critérios como título, diretor ou gênero.
- Ordenação de Filmes: Organização do catálogo por título, ano de lançamento ou nota (ascendente/descendente).
- Menu Interativo no Terminal: Navegação intuitiva entre as opções do sistema através de um menu baseado em texto.

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

## Como executar
Para executar este projeto em sua máquina, siga os passos abaixo:

- Pré-requisitos: Certifique-se de ter o Python 3 instalado em seu ambiente.
- Clone o Repositório:
  git clone https://github.com/RayanneMatos/catalogo-filmes-python.git
  cd catalogo-filmes-python
```bash
python main.py 
