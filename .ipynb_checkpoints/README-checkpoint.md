# Projeto de Engenharia de Dados - Brazilian E-Commerce


## Objetivo do projeto:
Projeto de Engenharia de Dados desenvolvido com foco na construção de uma pipeline em arquitetura medalhão, utilizando dados públicos de e-commerce para ingestão, tratamento e disponibilização analítica na camada Gold.

## Fonte dos dados
Base pública disponível no Kaggle:  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Arquitetura utilizada
Arquitetura Medalhão:
- **Raw:** armazenamento dos arquivos brutos;
- **Bronze:** ingestão dos arquivos com adição de metadados;
- **Silver:** checagem dos arquivos, limpeza, configuração de schema, remoção de nulos e duplicados, criação de colunas derivadas e salvamento em formato Parquet;
- **Gold:** consolidação dos dados em uma OBT para consumo analítico.

## Tecnologias:
- Python 3.13
- Pandas
- NumPy
- Jupyter Notebook
- Parquet

## Estrutura de pastas
```bash
data/
  raw/
  bronze/
  silver/
  gold/
```

## Estruturação das Camadas
- BRONZE: basicamente importamos os arquivos da raw e adicionamos a coluna de 'data_ingestao' em todos os DataFrames;
- SILVER: realização de todo o trabalho de ajustes em cada DataFrame. Em todos os DataFrames realizei conferência do início e do final do DF junto com uma checagem de valores nulos e duplicados, além da configuração de schema. Sempre seguindo a ordem de checar primeiro as chaves PK e FK, seguido de colunas de datas e valores numéricos.
  - df_customer: realização da checagem de estados e municípios;
  - df_pedidos: checagem dos status de pedidos, criação das colunas de tempo de entrega e se os pedidos chegaram atrasados;
  - df_itens_pedidos: criação da coluna 'total_value', que calcula o total do pedido (valor + frete);
  - df_produtos: realizei um join com outra pequena tabela de tradução de alguns nomes;
  - df_vendedores: conferência das cidades e estados dos vendedores;
  - df_ordem_pagamento: sem nenhuma alteração além das básicas;
  - df_geolocalizacao: aqui, consolidei boa parte da base, pois continha muitos dados duplicados. No caso o arquivo não traz o CEP completo, apenas o prefixo, ocasionando muitas duplicações de dados. Por conta desse fato, resolvi consolidar em algumas poucas regiões (para evitar relacionamento N:N).
- GOLD: aqui nos começamos consolidando a tabela de pagamento, criando uma única tabela de registro de pagamento consolidado para evitar a repetição do 'order_id'. Foi construída uma OBT (One Big Table) com grão no nível de item do pedido, consolidando informações de pedidos, clientes, pagamentos, produtos e vendedores para facilitar o consumo analítico.


## Melhorias Futuras:
- geração de relatórios analíticos automáticos
- criação de testes de qualidade de dados
- orquestração da pipeline 
- migração para PySpark




















