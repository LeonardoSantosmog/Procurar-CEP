<div align="center">

# 📮 API CEP

API simples e rápida para consulta de CEPs brasileiros 🇧🇷

<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white">
<img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white">
<img src="https://img.shields.io/badge/API-REST-blue?style=for-the-badge">

</div>

---

# 📌 Sobre

Esta API foi desenvolvida para realizar consultas de CEPs brasileiros de forma prática e eficiente.

Com ela, você pode obter:

- 📍 Rua
- 🏘️ Bairro
- 🌆 Cidade
- 🗺️ Estado
- ☎️ DDD

Os dados são retornados em formato JSON.

---

# 🚀 Tecnologias

- Node.js
- Express
- Axios
- JavaScript

---

# 📂 Estrutura do Projeto

```bash
📦 api-cep
 ┣ 📂 src
 ┃ ┣ 📂 controllers
 ┃ ┣ 📂 routes
 ┃ ┣ 📂 services
 ┃ ┗ server.js
 ┣ package.json
 ┗ README.md
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-cep.git
```

Entre na pasta do projeto:

```bash
cd api-cep
```

Instale as dependências:

```bash
npm install
```

---

# ▶️ Executando o Projeto

Inicie o servidor:

```bash
npm start
```

Servidor rodando em:

```bash
http://localhost:3000
```

---

# 🔎 Rotas da API

## Buscar CEP

### Endpoint

```http
GET /cep/:cep
```

### Exemplo de Requisição

```http
GET /cep/01001000
```

### Resposta

```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ddd": "11"
}
```

---

# ❌ Tratamento de Erros

## CEP inválido

```json
{
  "erro": "CEP inválido"
}
```

## CEP não encontrado

```json
{
  "erro": "CEP não encontrado"
}
```

---

# 📡 API Utilizada

Dados fornecidos por:

https://viacep.com.br

---

# 🛠️ Melhorias Futuras

- ✅ Cache de consultas
- ✅ Rate Limit
- ✅ Documentação Swagger
- ✅ Deploy na nuvem

---

# 📄 Licença

Este projeto está sob a licença MIT.

---

<div align="center">

### 👨‍💻 Desenvolvido por Leo

⭐ Se gostou do projeto, deixe uma estrela no repositório!

</div>
