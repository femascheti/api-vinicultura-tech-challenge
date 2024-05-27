# Documentação API de Vinicultura da EMBRAPA 
Esta API foi desenvolvida para facilitar o acesso e a análise de dados de vitivinicultura provenientes da Embrapa. A API oferece endpoints para consultar dados das seguintes categorias:

**Produção**: Obter informações sobre a produção de uva em diferentes regiões do Brasil, incluindo ano, quantidade, variedade e controle.
**Processamento**: Acessar dados sobre o processamento de uva, como tipo de processamento, ano, quantidade, controle e data de processamento.
**Comercializaçã**o: Consultar informações sobre a comercialização de uva, incluindo ano, tipo de comercialização, quantidade, valor, país de destino e data de comercialização.
**Importação**: Obter dados sobre a importação de uva, como ano, país de origem, tipo de uva, quantidade, valor e data de importação.
**Exportação**: Acessar informações sobre a exportação de uva, incluindo ano, país de destino, tipo de uva, quantidade, valor e data de exportação.

**Objetivos da API:**
Facilitar o acesso à informação: A API torna os dados da Embrapa facilmente acessíveis para pesquisadores, estudantes, profissionais do setor e qualquer pessoa interessada em vitivinicultura.
Promover a análise de dados: A API permite que usuários filtrem, agreguem e explorem os dados de forma personalizada, possibilitando a realização de análises aprofundadas e a geração de insights valiosos.
Fomentar o desenvolvimento de soluções inovadoras: Os dados disponibilizados pela API podem ser utilizados para o desenvolvimento de aplicativos, ferramentas e modelos de Machine Learning que contribuam para o aprimoramento da vitivinicultura brasileira.

**Links Úteis:**
* Site da Embrapa: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01
* Flask: https://flask.palletsprojects.com/en/3.0.x/

**Exemplo de Uso:**

Para obter dados de produção de uva no ano de 2023, utilize o seguinte endpoint:

```
Bash
GET /api/v1/producao?ano=2023
```

A resposta da API conterá uma lista de objetos JSON com as seguintes informações:

`id`: Identificador único da produção
`ano`: Ano da produção
`quantidade_litros`: Quantidade total de uva em litros
`quantidade_kg`: Quantidade total de uva em kg
`pais`: País de origem da uva
`data_importacao`: Data de importação do dado

## Endpoint produção

**Objetivo:**

O endpoint `/api/v1/producao` fornece acesso a dados de produção de uva, permitindo filtragem por ano, controle, país, quantidade em litros e quantidade em kg.

**Requisição:**

* **Método:** GET
* **URL:** `/api/v1/producao`
* **Autenticação:** Basic Auth (requer usuário e senha válidos)
* **Parâmetros:**
    * `ano` (opcional): Ano da produção (tipo: inteiro)
    * `control` (opcional): Controle da produção (tipo: string)
    * `pais` (opcional): País de origem da produção (tipo: string)
    * `litros_min` (opcional): Valor mínimo da quantidade em litros (tipo: float)
    * `litros_max` (opcional): Valor máximo da quantidade em litros (tipo: float)
    * `kg_min` (opcional): Valor mínimo da quantidade em kg (tipo: float)
    * `kg_max` (opcional): Valor máximo da quantidade em kg (tipo: float)

**Resposta:**

* **Formato:** JSON
* **Campos:**
    * `id`: Identificador único da produção
    * `ano`: Ano da produção
    * `control`: Controle da produção
    * `pais`: País de origem da produção
    * `quantidade_litros`: Quantidade em litros
    * `quantidade_kg`: Quantidade em kg
    * `data_importacao`: Data de importação do dado

**Exemplos de Uso:**

* **Obter dados de produção de todos os anos:**

```bash
GET /api/v1/producao
```

* **Obter dados de produção do ano 2023:**

```bash
GET /api/v1/producao?ano=2023
```

* **Obter dados de produção do ano 2023 do controle BR:**

```bash
GET /api/v1/producao?ano=2023&control=BR
```

* **Obter dados de produção do ano 2023 do controle BR, originados da Argentina, com quantidade em litros entre 1000 e 2000:**

```bash
GET /api/v1/producao?ano=2023&control=BR&pais=Argentina&litros_min=1000&litros_max=2000
```

**Observações:**

* A autenticação básica é necessária para acessar este endpoint.
* Os dados de produção são obtidos de arquivos CSV na pasta `data`.
* O endpoint utiliza a biblioteca `pandas` para filtrar e processar os dados.
* O endpoint utiliza a biblioteca `flask_basicauth` para autenticação básica.
* O endpoint utiliza a biblioteca `json` para converter os dados em formato JSON.

**Códigos de Status HTTP:**

* 200 OK: A requisição foi bem sucedida.
* 400 Bad Request: A requisição está incorreta.
* 401 Unauthorized: O usuário não está autorizado a acessar o endpoint.
* 500 Internal Server Error: Ocorreu um erro interno no servidor.

**Importante:**

* Este endpoint é apenas um exemplo. Adapte as informações de acordo com sua API específica.
* Inclua outros endpoints no README.md da mesma forma, seguindo uma estrutura consistente.
* Utilize seções e títulos claros para organizar o conteúdo.
* Considere adicionar exemplos de código para ilustrar o uso da API.

Ao seguir estas sugestões, você cria uma documentação completa e informativa do seu endpoint de produção no README.md, facilitando o acesso e a utilização da API por seus usuários.

## Endpoint comercial



## Endpoint importação

**Objetivo:**

O endpoint `/api/v1/importacao/<tipo>` fornece acesso a dados de importação de uva, categorizados por tipo (espumante, frescas, passas, suco e vinho). Os dados podem ser filtrados por ano, país, valor em dólar e quantidade em kg.

**Requisição:**

* **Método:** GET
* **URL:** `/api/v1/importacao/<tipo>`
* **Autenticação:** Basic Auth (requer usuário e senha válidos)
* **Parâmetros:**
    * `tipo` (obrigatório): Tipo da importação. Deve ser um dos seguintes:
        * espumante
        * frescas
        * passas
        * suco
        * vinho
    * `ano` (opcional): Ano da importação (tipo: inteiro)
    * `pais` (opcional): País de origem da importação (tipo: string)
    * `dolar_min` (opcional): Valor mínimo em dólar (tipo: float)
    * `dolar_max` (opcional): Valor máximo em dólar (tipo: float)
    * `kg_min` (opcional): Quantidade mínima em kg (tipo: float)
    * `kg_max` (opcional): Quantidade máxima em kg (tipo: float)

**Resposta:**

* **Formato:** JSON
* **Campos:**
    * `id`: Identificador único da importação
    * `tipo`: Tipo da importação
    * `ano`: Ano da importação
    * `pais`: País de origem da importação
    * `valor_dolar`: Valor total da importação em dólar
    * `quantidade_kg`: Quantidade total importada em kg
    * `data_importacao`: Data da importação

**Exemplos de Uso:**

* **Obter dados de importação de espumante de todos os anos:**

```bash
GET /api/v1/importacao/espumante
```

* **Obter dados de importação de espumante do ano 2023:**

```bash
GET /api/v1/importacao/espumante?ano=2023
```

* **Obter dados de importação de espumante do ano 2023 originados da Argentina, com valor entre 1000 e 2000 dólares e quantidade entre 1000 e 2000 kg:**

```bash
GET /api/v1/importacao/espumante?ano=2023&pais=Argentina&dolar_min=1000&dolar_max=2000&kg_min=1000&kg_max=2000
```

**Observações:**

* A autenticação básica é necessária para acessar este endpoint.
* Os dados de importação são obtidos de arquivos CSV armazenados na pasta `data`.
* O endpoint utiliza a biblioteca `pandas` para filtrar e processar os dados.
* O endpoint utiliza a biblioteca `flask_basicauth` para autenticação básica.
* O endpoint utiliza a biblioteca `json` para converter os dados em formato JSON.

**Códigos de Status HTTP:**

* 200 OK: A requisição foi bem sucedida.
* 400 Bad Request: A requisição está incorreta.
* 401 Unauthorized: O usuário não está autorizado a acessar o endpoint.
* 404 Not Found: O tipo de importação especificado não foi encontrado.
* 500 Internal Server Error: Ocorreu um erro interno no servidor.

**Importante:**

* Este endpoint é apenas um exemplo. Adapte as informações de acordo com sua API específica.
* Inclua outros endpoints no README.md da mesma forma, seguindo uma estrutura consistente.
* Utilize seções e títulos claros para organizar o conteúdo.
* Considere adicionar exemplos de código para ilustrar o uso da API.

Ao seguir estas sugestões, você cria uma documentação completa e informativa do seu endpoint de importação no README.md, facilitando o acesso e a utilização da API por seus usuários.


## Endpoint exportação

**Objetivo:**

O endpoint `/api/v1/exportacao/<tipo>` fornece acesso a dados de exportação de uva, categorizados por tipo (espumante, suco, uva e vinho). Os dados podem ser filtrados por ano, país, valor em dólar e quantidade em kg.

**Requisição:**

* **Método:** GET
* **URL:** `/api/v1/exportacao/<tipo>`
* **Autenticação:** Basic Auth (requer usuário e senha válidos)
* **Parâmetros:**
    * `tipo` (obrigatório): Tipo da exportação. Deve ser um dos seguintes:
        * espumante
        * suco
        * uva
        * vinho
    * `ano` (opcional): Ano da exportação (tipo: inteiro)
    * `pais` (opcional): País de destino da exportação (tipo: string)
    * `dolar_min` (opcional): Valor mínimo em dólar (tipo: float)
    * `dolar_max` (opcional): Valor máximo em dólar (tipo: float)
    * `kg_min` (opcional): Quantidade mínima em kg (tipo: float)
    * `kg_max` (opcional): Quantidade máxima em kg (tipo: float)

**Resposta:**

* **Formato:** JSON
* **Campos:**
    * `id`: Identificador único da exportação
    * `tipo`: Tipo da exportação
    * `ano`: Ano da exportação
    * `pais`: País de destino da exportação
    * `valor_dolar`: Valor total da exportação em dólar
    * `quantidade_kg`: Quantidade total exportada em kg
    * `data_exportacao`: Data da exportação

**Exemplos de Uso:**

* **Obter dados de exportação de vinho de todos os anos:**

```bash
GET /api/v1/exportacao/vinho
```

* **Obter dados de exportação de vinho do ano 2023:**

```bash
GET /api/v1/exportacao/vinho?ano=2023
```

* **Obter dados de exportação de vinho do ano 2023 com destino para a Alemanha, com valor entre 1000 e 2000 dólares e quantidade entre 1000 e 2000 kg:**

```bash
GET /api/v1/exportacao/vinho?ano=2023&pais=Alemanha&dolar_min=1000&dolar_max=2000&kg_min=1000&kg_max=2000
```

**Observações:**

* A autenticação básica é necessária para acessar este endpoint.
* Os dados de exportação são obtidos de arquivos CSV armazenados na pasta `data`.
* O endpoint utiliza a biblioteca `pandas` para filtrar e processar os dados.
* O endpoint utiliza a biblioteca `flask_basicauth` para autenticação básica.
* O endpoint utiliza a biblioteca `json` para converter os dados em formato JSON.

**Códigos de Status HTTP:**

* 200 OK: A requisição foi bem sucedida.
* 400 Bad Request: A requisição está incorreta.
* 401 Unauthorized: O usuário não está autorizado a acessar o endpoint.
* 404 Not Found: O tipo de exportação especificado não foi encontrado.
* 500 Internal Server Error: Ocorreu um erro interno no servidor.

**Importante:**

* Este endpoint é apenas um exemplo. Adapte as informações de acordo com sua API específica.
* Inclua outros endpoints no README.md da mesma forma, seguindo uma estrutura consistente.
* Utilize seções e títulos claros para organizar o conteúdo.
* Considere adicionar exemplos de código para ilustrar o uso da API.

Ao seguir estas sugestões, você cria uma documentação completa e informativa do seu endpoint de exportação no README.md, facilitando o acesso e a utilização da API por seus usuários.


## Endpoint processamento

**Objetivo:**

O endpoint `/api/v1/processa/<tipo>` fornece acesso a dados processados de uva, categorizados por tipo (americanas_hibridas, sem_classificacao, uvas_mesa e viniferas). Os dados podem ser filtrados por ano, controle e quantidade em kg.

**Requisição:**

* **Método:** GET
* **URL:** `/api/v1/processa/<tipo>`
* **Autenticação:** Basic Auth (requer usuário e senha válidos)
* **Parâmetros:**
    * `tipo` (obrigatório): Tipo do processamento. Deve ser um dos seguintes:
        * americanas_hibridas
        * sem_classificacao
        * uvas_mesa
        * viniferas
    * `ano` (opcional): Ano do processamento (tipo: inteiro)
    * `control` (opcional): Controle do processamento (tipo: string)
    * `kg_min` (opcional): Quantidade mínima em kg (tipo: float)
    * `kg_max` (opcional): Quantidade máxima em kg (tipo: float)

**Resposta:**

* **Formato:** JSON
* **Campos:**
    * `id`: Identificador único do processamento
    * `tipo`: Tipo do processamento
    * `ano`: Ano do processamento
    * `control`: Controle do processamento
    * `quantidade_kg`: Quantidade total processada em kg
    * `data_processamento`: Data do processamento

**Exemplos de Uso:**

* **Obter dados de processamento de uvas americanas híbridas de todos os anos:**

```bash
GET /api/v1/processa/americanas_hibridas
```

* **Obter dados de processamento de uvas americanas híbridas do ano 2023:**

```bash
GET /api/v1/processa/americanas_hibridas?ano=2023
```

* **Obter dados de processamento de uvas americanas híbridas do ano 2023 do controle BR, com quantidade entre 1000 e 2000 kg:**

```bash
GET /api/v1/processa/americanas_hibridas?ano=2023&control=BR&kg_min=1000&kg_max=2000
```

**Observações:**

* A autenticação básica é necessária para acessar este endpoint.
* Os dados de processamento são obtidos de arquivos CSV armazenados na pasta `data`.
* O endpoint utiliza a biblioteca `pandas` para filtrar e processar os dados.
* O endpoint utiliza a biblioteca `flask_basicauth` para autenticação básica.
* O endpoint utiliza a biblioteca `json` para converter os dados em formato JSON.

**Códigos de Status HTTP:**

* 200 OK: A requisição foi bem sucedida.
* 400 Bad Request: A requisição está incorreta.
* 401 Unauthorized: O usuário não está autorizado a acessar o endpoint.
* 404 Not Found: O tipo de processamento especificado não foi encontrado.
* 500 Internal Server Error: Ocorreu um erro interno no servidor.

**Importante:**

* Este endpoint é apenas um exemplo. Adapte as informações de acordo com sua API específica.
* Inclua outros endpoints no README.md da mesma forma, seguindo uma estrutura consistente.
* Utilize seções e títulos claros para organizar o conteúdo.
* Considere adicionar exemplos de código para ilustrar o uso da API.

Ao seguir estas sugestões, você cria uma documentação completa e informativa do seu endpoint de processamento no README.md, facilitando o acesso e a utilização da API por seus usuários.
