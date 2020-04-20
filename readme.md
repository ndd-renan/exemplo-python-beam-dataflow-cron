# Google DataFlow python - App Engine Deployment
Este projeto foi criado com base no seguinte artigo:
http://zablo.net/blog/post/python-apache-beam-google-dataflow-cron

As alterações feitas foram necessárias para o funcionamento com um ambientes `python 3`

---
Este repositório contém um projeto básico, que pode ser usado como exemplo de como deployar um pipeline do Google Dataflow dentro do Google App Engine, para que seja possível rodar o projeto como um um job CRON.

*SÓ É POSSÍVEL RODAR ESSE PROJETO EM UM AMBIENTE FLEXÍVEL DO APP ENGINE*, porque há problemas de compatibilidade de I/O entre o Apache Beam e Ambientes Fixos.

## Descrição
1. **setup.py** Arquivo responsável por distribuir dinamicamente os pacotes dentro dos workers do Dataflow (workers = instâncias do Docker). 
1. **app.yaml** Contém as definições da aplicação do App Engine, o qual é responsável por rodar o pipeline do Dataflow.
1. **cron.yaml** Contém a definição do CRON do App Engine, o qual "pinga" um dos endpoints da Aplicação. 
1. **appengine_config.py** Adiciona as dependências para os pacotes instalados localmente (que estão na pasta **lib**).

## Como rodar:
1. Instale todos os pacotes necessários da sua aplicação na pasta **lib** através do comando: ```pip install -r requirements.txt -t lib```
1. Faça o Deploy do App Engine app: ```gcloud app deploy app.yaml```
1. Faça o Deploy do App Engine CRON: ```gcloud app deploy cron.yaml```
