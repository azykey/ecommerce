

# Documentação do Projeto ETL de E-commerce

## Visão Geral do Projeto

### Objetivo
Desenvolver um pipeline de Extração, Transformação e Carregamento (ETL) para análise de dados de vendas de e-commerce, permitindo insights precisos sobre performance de vendas.

### Escopo
- Extração de dados de vendas de uma API
- Transformação e limpeza dos dados
- Carregamento em um data warehouse
- Monitoramento e log do processo

## 🛠 Tecnologias Utilizadas

### Linguagens e Bibliotecas
- **Linguagem Principal:** Python 3.9+
- **Bibliotecas de Dados:** 
  - Pandas
  - SQLAlchemy
  - Requests
- **Banco de Dados:** PostgreSQL
- **Infraestrutura:** Docker, Docker Compose

## 📂 Estrutura do Projeto

```
ecommerce-etl-project/
│
├── src/                  # Código-fonte principal
│   ├── __init__.py
│   ├── extract.py        # Módulo de extração de dados
│   ├── transform.py      # Módulo de transformação
│   ├── load.py           # Módulo de carregamento
│   └── main.py           # Orquestração do pipeline
│
├── tests/                # Testes unitários
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── configs/              # Configurações
│   └── config.yaml
│
├── logs/                 # Logs de execução
│   └── etl_pipeline.log
│
├── data/                 # Diretórios de dados
│   ├── raw/
│   ├── processed/
│   └── temp/
│
└── ... (outros arquivos)
```

## 🔍 Componentes Principais

### 1. Extração de Dados (`extract.py`)
- **Responsabilidade:** Buscar dados de uma API de vendas
- **Funcionalidades:**
  - Conexão flexível com API
  - Tratamento de erros
  - Logging de operações
  - Metadados de extração

#### Exemplo de Uso
```python
extractor = DataExtractor(api_config)
raw_data = extractor.extract_sales_data('sales')
```

### 2. Transformação de Dados (`transform.py`)
- **Responsabilidade:** Limpar, normalizar e enriquecer dados
- **Transformações Realizadas:**
  - Conversão de tipos
  - Tratamento de valores nulos
  - Criação de colunas derivadas
  - Categorização de vendas

#### Exemplo de Processamento
```python
transformed_data = DataTransformer.clean_sales_data(raw_data)
```

### 3. Carregamento de Dados (`load.py`)
- **Responsabilidade:** Carregar dados no banco PostgreSQL
- **Funcionalidades:**
  - Mapeamento ORM
  - Gerenciamento de sessões
  - Tratamento de erros
  - Logging de inserções

#### Exemplo de Carregamento
```python
loader = DataLoader(connection_string)
loader.load_to_database(transformed_data)
```

## 🚀 Configuração e Execução

### Pré-requisitos
- Docker
- Docker Compose
- Python 3.9+

### Passos de Instalação

1. **Clonar Repositório**
```bash
git clone https://github.com/seu-usuario/ecommerce-etl-project.git
cd ecommerce-etl-project
```

2. **Configurar Variáveis de Ambiente**
- Crie um arquivo `.env` com as configurações:
```
API_BASE_URL=https://api.exemplo.com/ecommerce
API_KEY=seu_token_secreto
DATABASE_URL=postgresql://usuario:senha@localhost:5432/ecommerce
```

3. **Construir e Executar**
```bash
docker-compose up --build
```

## 📊 Modelo de Dados

### Tabela de Vendas
| Coluna             | Tipo      | Descrição                       |
|--------------------|-----------|----------------------------------|
| sale_id            | String    | Identificador único da venda     |
| customer_id        | String    | Identificador do cliente         |
| product_id         | String    | Identificador do produto         |
| sale_value         | Float     | Valor total da venda             |
| sale_date          | DateTime  | Data e hora da venda             |
| month              | Integer   | Mês da venda                     |
| year               | Integer   | Ano da venda                     |
| quarter            | Integer   | Trimestre da venda               |
| sale_category      | String    | Categoria de valor da venda      |

## 🧪 Testes

### Estratégia de Testes
- Testes unitários para cada módulo
- Cobertura de casos de sucesso e erro
- Validação de transformações

### Executar Testes
```bash
python -m pytest tests/
```

## 🔒 Segurança e Boas Práticas
- Variáveis sensíveis no `.env`
- Logging de todas as operações
- Tratamento de exceções
- Validação de dados

## 📈 Monitoramento
- Logs detalhados em `logs/etl_pipeline.log`
- Rastreamento de erros
- Métricas de execução

## 🔄 Próximos Passos
- Implementar monitoramento avançado
- Adicionar mais transformações
- Criar dashboards de análise

## 👥 Contribuição
1. Faça um fork do projeto
2. Crie sua feature branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

---

**Licença de Uso Personalizada**  

Copyright (c) 2024 adilson oliveira ky

Por este meio, **não é concedida permissão automática** para o uso, modificação, distribuição ou comercialização deste software e dos arquivos de documentação associados (a "Obra").  

Qualquer pessoa que deseje lidar com a Obra, incluindo, mas não se limitando a, usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias da Obra, **deverá obter permissão expressa, por escrito**, do proprietário dos direitos autorais.  

**Condições para uso autorizado:**  
1. O aviso de copyright acima deverá ser incluído em todas as cópias ou partes substanciais da Obra.  
2. O uso da Obra deverá seguir estritamente os termos acordados com o proprietário.  

**Isenção de Garantia:**  
O SOFTWARE É FORNECIDO "NO ESTADO EM QUE SE ENCONTRA", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO, ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM FIM ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUM CASO OS AUTORES OU DETENTORES DOS DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER REIVINDICAÇÃO, DANO OU OUTRA RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, DELITO OU DE OUTRA FORMA, DECORRENTE DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.  

**Contato para Permissão:**  
Para solicitar autorização ou obter mais informações sobre o uso da Obra, entre em contato com:  
adilsonoliveira.2788@gmail.com  

---



---

## 📞 Contato
- **Autor:** Adilson Oliveira
- **Email:** adilsonoliveiera.2788@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/aadiilson-oliveira/

### Observações Finais
- Projeto em constante evolução
- Feedback e contribuições são bem-vindos
- Documentação atualizada regularmente

---

