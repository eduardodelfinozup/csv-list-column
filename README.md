# csv-list-column
stack para lista coluna de um csv
script em python
deverar ter as entradas:
nome do csv ex: test-123
coluna      ex: 2
delimitador ex: , 

# Índice
* [util/arquivo](#colocar o arquivo csv para leitura aqui)
* [Documentação Auxiliar](#Esse template sera gerado através da stackfiles)

```
csv-list-column-plugin
│   ├── docs
│   │   ├── about.md
│   │   ├── implementation.md
│   │   ├── usage.md
│   │   └── use-case.md
│   ├── plugin.png
│   ├── plugin.yaml
│   └── templates
│       ├── formatador
│       │   └── util
│       │       └── csv_util.py
│       └── README.md
├── csv-list-column-template
│   ├── templates
│   │   ├── formatador
│   │   │   ├── application.py
│   │   │   ├── __init__.py
│   │   │   ├── novo-arquivo
│   │   │   └── util
│   │   │       ├── arquivo
│   │   │       ├── csv_util.py
│   │   │       └── __pycache__
│   │   ├── __init__.py
│   │   └── README.md
│   └── template.yaml
├── docs
│   ├── about.md
│   └── use-case.md
├── index.json
├── README.md
├── stackfiles
│   ├── csv-list-column-stackfiles.yaml
│   └── default.yaml
├── stack.png
└── stack.yaml
```

# Executar Local
* [Exemplo do caminho](#/home/pasta/pasta/csv-list-column/stackfiles/csv-list-column-stackfiles.yaml)
  stk create app csv-python-list --stackfile /home/csv-list-column/stackfiles/csv-list-column-stackfiles.yaml

