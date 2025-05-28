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
- Menu Interativo: Desenvolvimento de uma interface de linha de comando amigável para interação com o usuário.
---

##  Funcionalidades
O sistema oferece as seguintes funcionalidades principais:
- Listagem de Filmes: Visualização de todos os filmes cadastrados.
- Busca de Filmes: Pesquisa por filmes utilizando critérios como título, diretor ou gênero.
- Ordenação de Filmes: Organização do catálogo por título, ano de lançamento ou nota (ascendente/descendente).
- Menu Interativo no Terminal: Navegação intuitiva entre as opções do sistema através de um menu baseado em texto.

### Listagem
A listagem dos filmes cadastrados se trata de um a parte de um sistema maior de gerenciamento de catálogo de filmes. Este trecho de código em Python é o responsável por listar de forma detalhada e intuitiva, as informações sobre os filmes já cadastrados no sistema.

A estrutura do código se inicia com a importação de alguns elementos importantes para o funcionamento do código, como:

- import csv: embora o módulo csv seja importado, ele não é utilizado diretamente neste trecho, indicando que sua funcionalidade pode estar presente na função carregar_dados.

- carregar_dados: função importada do módulo catalogo, responsável por carregar os dados dos filmes.

- CSV_PATH_LOCAL: constante que define o caminho do arquivo de origem dos dados (não utilizada diretamente no código apresentado).

Já com a função listar_filmes_detalhado temos a principal funcionalidade do código. Essa função recebe uma lista de filmes e imprime as informações recebidas de maneira detalhada e organizada.
Estrutura da função:

- Verificação de lista vazia: caso não haja filmes, uma mensagem é exibida ao usuário.

        ...
      def listar_filmes_detalhado(filmes):
        if not filmes:
            print("Nenhum filme cadastrado para listar.")
            return
              ...

- Dicionário de idiomas: a função utiliza um dicionário idiomas_map para converter siglas de idiomas em nomes completos (por exemplo, 'en' → 'English') com intuito de trazer uma interface mais compreensível para o usuário.

      ...
        idiomas_map = {
            'en': 'English', ...
        }
        ...      
    
Laço de repetição: percorre a lista de filmes e imprime os seguintes dados:
    	
- Título
- Data de lançamento
- Gêneros (formatados como lista separada por vírgulas)
- Média de votos (com uma casa decimal)
- Descrição (sinopse)
-  Duração em minutos
- Linguagem original (convertida com base na sigla)
- Orçamento e receita (formatados com separadores de milhar)

      ...
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
      ...
  
Por fim o trecho if __name__ == "__main__" garante que o código será executado apenas quando o arquivo for executado diretamente (não quando for importado como módulo). Nele:

- Os dados dos filmes são carregados via carregar_dados.
- A função listar_filmes_detalhado é chamada para exibir as informações dos filmes.

        ...
        if __name__ == "__main__":
            catalogo_filmes = carregar_dados()
            listar_filmes_detalhado(catalogo_filmes)
            ... 
### Busca
O módulo busca.py é uma peça fundamental do sistema de gerenciamento de catálogo de filmes, responsável por implementar as funcionalidades de pesquisa. Este módulo oferece métodos eficientes para localizar filmes com base em diferentes critérios, garantindo que o usuário possa encontrar rapidamente as informações desejadas dentro do catálogo.

- Estrutura e Funcionalidades:
       O código do módulo é simples e direto, focando em duas funcionalidades principais de busca: por título e por gênero.
- Função buscar_por_titulo(catalogo, titulo)
      Esta função é projetada para realizar uma busca linear por título no catálogo de filmes.
- Parâmetros:
      catalogo: Uma lista de dicionários, onde cada dicionário representa um filme com suas informações.
      titulo: A string contendo o termo de busca para o título do filme.
- Funcionamento:
  A função inicializa uma lista vazia chamada resultados para armazenar os filmes encontrados.

      ...
      def buscar_por_titulo(catalogo, titulo):
          """Busca linear por título (case insensitive)."""
          resultados = [] ...
  
  Ela itera sobre cada filme presente no catalogo.
  Para cada filme, compara o titulo fornecido (convertido para letras minúsculas) com o título do filme atual (filme['title'], também convertido para minúsculas). Essa conversão para minúsculas garante que a busca seja case insensitive, ou seja, não diferencia maiúsculas de minúsculas (ex: "Avatar" e "avatar" retornam o mesmo resultado).
  Se o termo de busca for encontrado em qualquer parte do título do filme, o filme é adicionado à lista resultados.

      ...
        for filme in catalogo:
            if titulo.lower() in filme['title'].lower():
            resultados.append(filme) ...

  Ao final do loop, a função retorna a lista resultados, que pode estar vazia se nenhum filme corresponder ao critério de busca.

        ...
        return resultados ...

### Ordenação
O módulo ordenacao.py é uma parte crucial do sistema de gerenciamento de catálogo de filmes, sendo responsável por implementar a funcionalidade de ordenação. Este módulo se destaca pela utilização do algoritmo Quick Sort, uma escolha eficiente para organizar os filmes do catálogo com base em diferentes critérios.

- Estrutura e Funcionalidades
  O código é estruturado em várias funções auxiliares que, juntas, compõem a lógica do Quick Sort, além de uma função principal para orquestrar a ordenação do catálogo.

- Função quick_sort(lista, chave, inicio=0, fim=None)
  Esta é a função principal que implementa o algoritmo de ordenação Quick Sort de forma recursiva.

        ...
        def quick_sort(lista, chave, inicio=0, fim=None):
          if fim is None:
              fim = len(lista) - 1
      
          if inicio < fim:
              p = particao(lista, chave, inicio, fim)
              quick_sort(lista, chave, inicio, p - 1)
              quick_sort(lista, chave, p + 1, fim)
              ...

#### Parâmetros:
- lista: A lista de dicionários (filmes) a ser ordenada.
- chave: A chave (critério) pela qual a lista será ordenada (ex: "title", "ano", "nota").
- inicio: Índice inicial da sub-lista a ser ordenada (padrão: 0).
- fim: Índice final da sub-lista a ser ordenada (padrão: último elemento da lista).
  
#### Funcionamento:
Define o fim como o último índice da lista se não for fornecido.
A condição if inicio < fim: controla a recursão, garantindo que a ordenação ocorra apenas em sub-listas com mais de um elemento.

      ...
      if inicio < fim:
            p = particao(lista, chave, inicio, fim)
            quick_sort(lista, chave, inicio, p - 1)
            quick_sort(lista, chave, p + 1, fim)
            ...
Chama a função particao para dividir a lista em torno de um pivô e obter a posição final deste pivô (p).
     
      ...
      def particao(lista, chave, inicio, fim):
          pivot = lista[fim]
          i = inicio - 1

          for j in range(inicio, fim):
              if comparar(lista[j], pivot, chave):
                  i += 1
                  lista[i], lista[j] = lista[j], lista[i]
      
          lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
          return i + 1 
          ...
Realiza chamadas recursivas para quick_sort para ordenar as sub-listas à esquerda (inicio até p - 1) e à direita (p + 1 até fim) do pivô, até que toda a lista esteja ordenada.
Função particao(lista, chave, inicio, fim)
Esta função auxiliar é o coração do Quick Sort, responsável por rearranjar os elementos de uma sub-lista em torno de um elemento pivô.

#### Parâmetros:
- lista: A sub-lista de filmes a ser particionada.
- chave: O critério de ordenação.
- inicio: Índice inicial da sub-lista.
- fim: Índice final da sub-lista (o elemento nesse índice é escolhido como pivô).

#### Funcionamento:
- O pivot é definido como o último elemento da sub-lista (lista[fim]).
  i é inicializado como inicio - 1 e serve para rastrear o índice do último elemento menor que o pivô.

      ...
      def particao(lista, chave, inicio, fim):
          pivot = lista[fim]
          i = inicio - 1
              ...

- O laço for j in range(inicio, fim) percorre os elementos da sub-lista, do inicio até o elemento antes do fim.
  Dentro do laço, a função comparar é utilizada para verificar se o elemento atual (lista[j]) é menor ou igual ao pivot com base na chave de ordenação.
  Se for menor ou igual, i é incrementado e os elementos lista[i] e lista[j] são trocados, movendo elementos menores para a parte esquerda.

      ...
         for j in range(inicio, fim):
              if comparar(lista[j], pivot, chave):
                  i += 1
                  lista[i], lista[j] = lista[j], lista[i]
                    ...

- Após o laço, o pivot (que estava em lista[fim]) é colocado na sua posição correta na lista (entre os elementos menores e maiores), trocando-o com lista[i + 1].
  A função retorna i + 1, que é a posição final do pivô.

      ...
      lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
          return i + 1
            ...

- Função comparar(a, b, chave)
- Uma função utilitária que compara dois filmes (a e b) com base em uma chave específica, determinando a ordem relativa entre eles.

#### Parâmetros:
- a, b: Os dois dicionários de filmes a serem comparados.
- chave: O critério de comparação (ex: "title", "ano", "nota").
  
#### Funcionamento:
- Utiliza a função extrair_valor para obter os valores comparáveis dos filmes a e b com base na chave.
- Retorna True se o valor de a for menor ou igual ao valor de b, e False caso contrário, seguindo a lógica de ordenação crescente.
- Função extrair_valor(filme, chave)
- Função auxiliar crucial para normalizar e extrair o valor correto de um filme para comparação, dependendo da chave de ordenação.

       ...
              def comparar(a, b, chave):
                va = extrair_valor(a, chave)
                vb = extrair_valor(b, chave)
                return va <= vb
                    ...
#### Parâmetros:
- filme: O dicionário representando o filme.
- chave: O critério de ordenação.

#### Funcionamento:
- "title": Retorna o título do filme em letras minúsculas (.lower()) para garantir uma ordenação de texto case-insensitive.
- "ano": Tenta extrair o ano da data de lançamento (release_date). Em caso de erro na conversão ou valor ausente, retorna 0.
- "nota": Tenta converter a média de votos (vote_average) para um tipo float. Em caso de erro, retorna 0.0.
- Chave Inválida: Se a chave não corresponder a nenhuma das opções válidas, a função retorna o título em minúsculas como um fallback, garantindo que a ordenação ainda ocorra por um critério padrão.
- Função ordenar_catalogo(catalogo, chave_ordenacao)
- Esta é a interface principal para a ordenação do catálogo, responsável por validar a entrada e chamar o Quick Sort.

      ...
        def extrair_valor(filme, chave):
          if chave == "title":
              return filme.get("title", "").lower()
      
          elif chave == "ano":
              data = filme.get("release_date", "")
              try:
                  return int(data[:4]) if data else 0
              except ValueError:
                  return 0  # ou algum valor que represente "sem data"
                    ...
#### Parâmetros:
- catalogo: A lista de filmes a ser ordenada.
- chave_ordenacao: A string que indica o critério de ordenação desejado ("title", "ano", "nota").

#### Funcionamento:
- Verifica se o catalogo está vazio e exibe uma mensagem apropriada.
- Valida se a chave_ordenacao fornecida é uma das opções permitidas. Se for inválida, uma mensagem de aviso é exibida e a chave é automaticamente alterada para "title" (ordenar por título).
- Finalmente, chama a função quick_sort com o catálogo e a chave de ordenação validada, realizando a ordenação in-place.
- Conceitos de Estrutura de Dados e Algoritmos
- Este módulo demonstra a implementação do algoritmo de ordenação Quick Sort, conhecido por sua eficiência (O(n log n)) em casos médios, tornando-o uma escolha popular para grandes conjuntos de dados.

      ...
        def ordenar_catalogo(catalogo, chave_ordenacao):
          if not catalogo:
              print("⚠️ Catálogo vazio. Nada a ordenar.")
              return
      
          if chave_ordenacao not in ["title", "ano", "nota"]:
              print(f"⚠️ Chave de ordenação '{chave_ordenacao}' inválida. Ordenando por título.")
              chave_ordenacao = "title"
      
          quick_sort(catalogo, chave_ordenacao)
              ...
  
- Recursão: O quick_sort utiliza recursão para dividir o problema em subproblemas menores e resolvê-los independentemente.
- Divisão e Conquista: O Quick Sort segue o paradigma de "Dividir e Conquistar":
- Dividir: Particiona a lista em torno de um pivô.
- Conquistar: Ordena recursivamente as duas sub-listas.
- Combinar: Não há uma etapa de combinação explícita, pois a lista já está ordenada in-place após as partições.
- Manipulação de Listas In-place: A ordenação é realizada diretamente na lista fornecida, sem a criação de cópias adicionais para a lista inteira, o que otimiza o uso de memória.
- Flexibilidade de Chaves: A função extrair_valor permite que o mesmo algoritmo de ordenação seja aplicado a diferentes tipos de dados (strings para títulos, inteiros para ano, floats para nota), mostrando a adaptabilidade do algoritmo.


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
