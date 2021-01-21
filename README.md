# Objetivo
Este repositório é um exemplo didático do uso de aprendizado de máquina, desta forma, busca-se a aplicação fim-a-fim do aprendizado de máquina, isto é, desde a obtenção dos dados, criação de atributos, avaliação dos modelos de aprendizado e criação do modelo final. 

Na sequência, o objetivo é colocar o modelo em produção (deploy) em conjunto com uma interface web para realizar requisições HTTP ao servidor que avaliará a classificação dos dados enviados quando analisado pelo modelo de aprendizado.

# Problema escolhido

Para este estudo foi escolhido o problema de detecção de fake news, assim a partir de um texto de entrada o modelo treinado irá estimar se esse texto é classificado como texto verdadeiro ou como texto falso.

Trata-se de um problema de processamento de linguagem natual (PLN / NLP).

Exemplo: http://nilc-fakenews.herokuapp.com/

# Reproduzindo este repositório
```
$ git clone https://github.com/gubertoli/ml-fake-check.git
$ cd ml-fake-check
$ pip install -r requirements.txt
$ jupyter notebook
```

# Dataset Utilizado

## Fake.br corpus

Fonte: https://github.com/roneysco/Fake.br-Corpus

