
## Jinja

You can use jinja to make a template-data folder more dynamic.

complete documentation of jinja: https://jinja.palletsprojects.com/en/3.0.x/templates/

# Índice
* [util/arquivo](#colocar o arquivo csv para leitura aqui)
* [Documentação Auxiliar](#Esse template sera gerado através da stackfiles)

* [util/csv_util.py](#script plugin para leitura e geração de colunas)
* [Documentação Auxiliar](#Esse template sera gerado através da stackfiles)

```
csv-list-column-template
│   ├── templates
│   │   ├── formatador
│   │   │   ├── application.py
│   │   │   ├── __init__.py
│   │   │   ├── novo-arquivo
│   │   │   └── util
│   │   │       ├── arquivo
│   │   │       │   └── teste-137.csv
│   │   │       ├── csv_util.py
│   │   │       └── __pycache__
│   │   ├── __init__.py
│   │   └── README.md
│   └── template.yaml
```

# Executar Local
* [Exemplo do caminho](#/home/pasta/pasta/csv-list-column/stackfiles/csv-list-column-stackfiles.yaml)
  stk create app csv-python-list --stackfile /home/csv-list-column/stackfiles/csv-list-column-stackfiles.yaml
