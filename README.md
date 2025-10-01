# POC SAP Greenfield Backend - README

> **Descrição curta**
>
> API RESTful desenvolvida em **Flask**, estruturada em módulos.

---

## Sumário

* [Sobre](#sobre)
* [Tecnologias](#tecnologias)
* [Pré-requisitos](#pré-requisitos)
* [Passo a passo de startup](#passo-a-passo-de-startup)
* [Monitoramento e Logs](#monitoramento-e-logs)
* [Contribuição](#contribuição)
* [Roadmap / Próximos passos (TODO)](#roadmap--próximos-passos-todo)
* [Resolução de problemas comuns](#resolução-de-problemas-comuns)

---

## Sobre

Este projeto é uma **API RESTful** construída em Flask, organizada em módulos e facilmente extensível. Os endpoints são claros e documentados, fornecendo uma base sólida para integrações com front-ends ou outros serviços.

---

## Tecnologias

* **Linguagem:** Python 3.11
* **Framework:** Flask
* **Dependências:** definidas em `requirements.txt`

---

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado:

* Python 3.11+
* Git
* Virtualenv (opcional, mas recomendado)
* Docker (opcional)

---

## Passo a passo de startup

1. Clone o repositório

```bash
git clone <URL_DO_REPO>
cd <PASTA_DO_PROJETO>
```

2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/MacOS
.venv\Scripts\activate      # Windows
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente

```bash
cp .env.example .env
# editar o arquivo .env conforme necessário
```

5. Rode a aplicação

```bash
python main.py
```

6. Acesse a API

Abra `http://localhost:5000` no navegador ou via ferramentas como **Postman**/**Insomnia**.

---

## Monitoramento e Logs

* Logs são exibidos no console por padrão.
* Recomenda-se configurar ferramentas como Prometheus/Grafana (TODO).
* Endpoint de healthcheck pode ser adicionado em `/health`.

---

## Contribuição

1. Fork este repositório
2. Crie uma branch (`feature/xxx` ou `fix/xxx`)
3. Faça commit das alterações
4. Abra um Pull Request

---

## Roadmap / Próximos passos (TODO)

* [ ] Adicionar testes unitários
* [ ] Adicionar documentação de endpoints (Swagger/OpenAPI)
* [ ] Criar docker-compose
* [ ] Implementar logging estruturado

---

## Resolução de problemas comuns

* **Erro de módulo não encontrado**: verifique se o ambiente virtual está ativado e se as dependências foram instaladas.
