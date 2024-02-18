# English Learning Platform

[![codecov](https://codecov.io/gh/fczanetti/elp/graph/badge.svg?token=u6ss1ECOtY)](https://codecov.io/gh/fczanetti/elp)
[![Static Badge](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Static Badge](https://img.shields.io/badge/Django-5.0.2-green)](https://www.djangoproject.com/)

O projeto em desenvolvimento é uma plataforma de ensino simples para publicação de aulas separadas por módulos. Foi
criado com foco no aprendizado de inglês, porém pode ser adaptado para qualquer assunto que se desejar simplesmente
alterando os títulos onde necessário.

Foi criado um aplicativo chamado Podcasts onde vídeos podem ser inseridos através de URL do Youtube, podendo estes ser
podcasts de fato ou vídeos diversos referentes ao assunto a que a plataforma será destinada.


Algumas orientações:

- criar um ambiente virtual para a instalação das bibliotecas;
- as bibliotecas necessárias para funcionamento se encontram listadas no arquivo Pipfile;
- é necessário instalar o docker e rodar o comando 'docker compose up' para que o banco de dados (PostgreSQL) seja criado;
- as variáveis de ambiente necessárias se encontram no arquivo env-sample, dentro da pasta 'contrib';
- o projeto foi configurado para que seja feito deploy na plataforma Fly.io sempre que um push ou pull request for
feito na branch main. Para que aconteça o repositório deve estar linkado com a plataforma Fly.io através da variável
de ambiente (Action secret) FLY_APY_TOKEN (consultar documentação do da plataforma Fly.io para mais detalhes);
- o projeto foi configurado para que, em ambiente de produção, envie os arquivos estáticos para um bucket na AWS, e
em ambiente local os arquivos serão coletados na pasta 'staticfiles'. Será necessário criar um bucket na AWS e configurar
as variáveis de ambiente em produção para que os arquivos estáticos sejam direcionados no momento do deploy;
- o projeto foi configurado para que, após feito o deploy, os comandos 'python manage.py collectstatic' e 'python manage.py
migrate' sejam executados a fim de coletar os arquivos estáticos e rodar as migrações no ambiente de produção. Estes
comandos se encontram listados no arquivo 'start.sh';
- para testar o sistema de pagamentos deve ser feito um cadastro na plataforma https://stripe.com/br. Os produtos devem
ser criados também na plataforma Stripe e cadastrados neste aplicativo através do modelo Product, e o campo "stripe_id"
deve ser preenchido com o valor do ID do preço do produto disponibilizado pelo Stripe, e não com o ID do produto. Para
que o produto cadastrado apareça na página de produtos este deve estar com o campo "available" configurado para True;


Principais pendências:

- Finalizar sistema de pagamentos e controle através do tempo de acesso disponível ao usuário que adquirir;
- Confirmação através de email por ocasião da criação de novos usuários;
- Criação de um teste de nivelamento composto por perguntas e respostas simples e um resultado final;
- Criação de uma interface para gerenciamento do conteúdo da aplicação.