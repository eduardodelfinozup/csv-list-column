
## Jinja

You can use jinja to make a template-data folder more dynamic.

complete documentation of jinja: https://jinja.palletsprojects.com/en/3.0.x/templates/

# Índice
* [util/csv_util.py](#script plugin para leitura e geração de colunas)
* [Documentação Auxiliar](#Esse template sera gerado através da stackfiles)

```
├── docs
│   ├── about.md
│   ├── implementation.md
│   ├── usage.md
│   └── use-case.md
├── plugin.png
├── plugin.yaml
└── templates
    ├── formatador
    │   └── util
    │       └── csv_util.py
    └── README.md

```

# Executar Local
* [Exemplo do caminho](#/home/pasta/pasta/csv-list-column/stackfiles/csv-list-column-stackfiles.yaml)
stk create app csv-python-list --stackfile /home/csv-list-column/stackfiles/csv-list-column-stackfiles.yaml