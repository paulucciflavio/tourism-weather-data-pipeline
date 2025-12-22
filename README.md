# Tourism & Weather Data Pipeline

## O que é este projeto?
Este projeto é um pipeline de engenharia de dados que coleta dados de clima
e turismo, processa essas informações e armazena em um banco de dados
para análise de sazonalidade no setor turístico.
## Objetivo
Demonstrar a construção de um pipeline de engenharia de dados
end-to-end, aplicando boas práticas de ingestão, transformação,
armazenamento e organização de dados.

---

## Quais dados são utilizados?
- Dados de clima (API OpenWeather)
- Dados públicos de turismo (IBGE)
- Dados de eventos turísticos (CSV simulado)

---

## Como o pipeline funciona? (bem simples)
1. Os dados são coletados de APIs e arquivos CSV
2. Os dados crus são salvos sem alteração
3. Os dados são limpos e transformados
4. Os dados são armazenados em um banco PostgreSQL

---

## Tecnologias utilizadas
- Python
- Pandas
- PostgreSQL
- Docker (em breve)
- Airflow (em breve)

## Estrutura do projeto
```text
tourism-weather-data-pipeline/
├── config/ # Configurações do projeto (APIs, caminhos, variáveis)
├── data/
│ ├── raw/ # Dados brutos coletados das fontes (sem transformação)
│ ├── processed/ # Dados limpos e transformados
│ └── curated/ # Dados prontos para análise
├── docker/ # Arquivos relacionados à containerização
├── extract/ # Scripts de extração de dados (APIs e CSVs)
├── transform/ # Scripts de limpeza e transformação dos dados
├── load/ # Scripts de carga dos dados em banco
├── notebooks/ # Exploração e testes (não faz parte do pipeline final)
└── README.md

## Status do projeto
🚧 Em desenvolvimento — atualmente na fase de ingestão de dados (extract)

## Próximos passos
- Implementar carga de dados em PostgreSQL
- Criar modelagem analítica (star schema)
- Orquestrar o pipeline com Airflow
- Adicionar validações de qualidade de dados
