# Objetivo
Este reposit�rio � um exemplo did�tico do uso de aprendizado de m�quina, desta forma, busca-se a aplica��o fim-a-fim do aprendizado de m�quina, isto �, desde a obten��o dos dados, cria��o de atributos, avalia��o dos modelos de aprendizado e cria��o do modelo final. 

Na sequ�ncia, o objetivo � colocar o modelo em produ��o (deploy) em conjunto com uma interface web para realizar requisi��es HTTP ao servidor que avaliar� a classifica��o dos dados enviados quando analisado pelo modelo de aprendizado.

# Problema escolhido

Para este estudo foi escolhido o problema de detec��o de fake news, assim a partir de um texto de entrada o modelo treinado ir� estimar se esse texto � classificado como texto verdadeiro ou como texto falso.

Trata-se de um problema de processamento de linguagem natual (PLN / NLP).

Exemplo: http://nilc-fakenews.herokuapp.com/

# Reproduzindo este reposit�rio
```
$ git clone https://github.com/gubertoli/fake-check.git
$ cd ml-fake-check
$ pip install -r requirements.txt
$ jupyter notebook
```

# Dataset Utilizado

## Fake.br corpus

Fonte: https://github.com/roneysco/Fake.br-Corpus

