# API de Reservas de Salas de Aula

Este projeto é uma API RESTful desenvolvida em Python com Flask, responsável pelo gerenciamento de reservas de salas de aula. A API permite que usuários realizem operações como criação, consulta, atualização e exclusão de reservas, integrando-se com um sistema de gerenciamento escolar para garantir a consistência das informações.

---

## 🧰 Tecnologias Utilizadas

- Python 3.x  
- Flask  
- SQLite (banco local)  
- Docker  
- Docker Compose  

---

## 🚀 Como Executar o Projeto com Docker

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/api-reservas.git
   cd api-reservas

2. **Execute os containers com Docker Compose:**

    docker-compose up --build

## 🏗️ Arquitetura do Projeto

api_reservas/
│
├── app/                  # Configurações e inicialização do app Flask
│   ├── config.py         # Configurações globais
│   └── database.py       # Conexão com banco de dados
│
├── controllers/          # Camada de controle (lógica das requisições)
│   └── reserva_controller.py
│
├── models/               # Modelos (estrutura das tabelas e lógica de dados)
│   └── reserva_model.py
│
├── routes/               # Definições das rotas da API
│   └── reserva_route.py
│
├── instance/             # Arquivos de instância (ex: banco SQLite local)
│   └── reservas.db
│
├── main.py               # Ponto de entrada da aplicação
├── Dockerfile            # Configuração da imagem Docker
├── docker-compose.yml    # Orquestração de serviços com Docker Compose
└── requirements.txt      # Dependências da aplicação


## 🔗 Integração com o Ecossistema de Microsserviços

A API de Reservas faz parte de um ecossistema maior composto por microsserviços independentes que se comunicam entre si via requisições HTTP. Um dos principais serviços integrados é a API de Gerenciamento Escolar , responsável pelo cadastro e gerenciamento de usuários, turmas e disciplinas.

Integração com API de Gerenciamento Escolar
Objetivo: Validar se o usuário solicitante da reserva está cadastrado e autorizado.

Fluxo de Comunicação:

Ao receber uma solicitação de reserva, API de Reservasrealize uma requisição para um API de Gerenciamento Escolar.

A resposta válida se o usuário pode reservar uma sala para o horário desejado.

Protocolo: RESTful (HTTP)

Formato de dados: JSON 

## 📚 Funcionalidades da API

    Criar reserva

    Listar todas as reservas

    Pesquisar reserva por ID

    Atualizar dados de uma reserva

    Excluir reserva

    Verifique conflitos de local

## 📌 Observações
Para fins de desenvolvimento e testes locais, está sendo utilizado o SQLite.

Em ambiente de produção, recomendamos usar PostgreSQL ou outro banco mais robusto.
