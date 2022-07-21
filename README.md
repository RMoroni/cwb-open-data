# cwb-open-data

Ferramentas para navegação nos Dados Abertos de Curitiba (https://www.curitiba.pr.gov.br/dadosabertos/)

# ETL

As funções estão prontas para serem utilizadas de forma isolada (exemplo: para uma execução local), porém o objetivo
final é automatizar as etapas via Apache Airflow.

## Como executar
```
// TODO
```

## Módulos
Os módulos estão organizados como layer/feature, cada feature representa uma base dos Dados Abertos de Curitiba.

### Guarda Municipal

É uma base com dados das ocorrências atendidas pela Guarda Municipal de Curitiba. A base é atualizada de forma
incremental e possui dados que começam em 2009.
