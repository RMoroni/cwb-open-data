# cwb-open-data

Ferramentas para navegação nos Dados Abertos de Curitiba (https://www.curitiba.pr.gov.br/dadosabertos/)

# ETL
## Como executar
```
docker build .
docker run -it -p 8080:8080 IMAGE_ID bash
```
Para rodar o último build para substituir IMAGE_ID por:
```
docker run -it -p 8080:8080 $(docker images | awk '{print $3}' | awk 'NR==2') bash
```

Como o container em execução rode (no container) o seguinte comando para inciar o airflow:
```
airflow scheduler -D
```
Após isso o airflow estará acessível via: localhost:8080

## Módulos
Os módulos estão organizados como layer/feature, cada feature representa uma base dos Dados Abertos de Curitiba.

### Guarda Municipal

É uma base com dados das ocorrências atendidas pela Guarda Municipal de Curitiba. A base é atualizada de forma
incremental e possui dados que começam em 2009.
