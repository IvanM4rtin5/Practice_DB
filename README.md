# 🗃️ Treinamento com PostgreSQL e Python

Pequeno repositório de treino para manipulação de dados em um banco de dados PostgreSQL usando Python com a biblioteca `psycopg2`.

Este projeto tem como objetivo praticar **operações básicas de banco de dados** — criação de tabelas, inserção, atualização, deleção e consultas — utilizando scripts simples com Python.

---

## 📂 Estrutura do Projeto

```bash
└── practice_db/
├── requirements.txt # Dependências do projeto
├── store__sql.py # Script de criação/alteração de tabelas
└── teste_db.py # Script principal de testes no banco
```

---

## 📋 Funcionalidades

- ✅ **Conexão com PostgreSQL**
- ✅ **Criação de tabelas com relacionamentos**
- ✅ **Inserção de dados de exemplo**
- ✅ **Consultas simples e com filtros**
- ✅ **Alterações e exclusões de registros**
- ✅ **Commit e encerramento seguro da conexão**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **PostgreSQL**
- **psycopg2** - Driver de conexão entre Python e PostgreSQL

---

## 📦 Requisitos

- Python instalado na máquina
- PostgreSQL instalado e rodando localmente
- Banco de dados chamado `postgres` (ou edite no script)
- Usuário e senha padrão: `postgres / postgres` (edite se necessário)

---

## 🔌 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/practice_db.git
cd practice_db
```
2. Criar e ativar ambiente virtual (opcional, mas recomendado)
```bash
Copiar código
python -m venv venv
.\venv\Scripts\Activate  # Windows
```
3. Instalar dependências
```bash
Copiar código
pip install -r requirements.txt
```
### ▶️ Como Usar
Rodar o script de teste:
```bash
Copiar código
python teste_db.py
```
Ele executará a consulta definida no final do arquivo e imprimirá os resultados.

**Personalização:**
Você pode descomentar os trechos de código dentro de `teste_db.py` para testar:

Criação de tabelas

Inserção de dados

Atualizações

Exclusões

Consultas com filtros (ILIKE, WHERE, etc.)

### 🧪 Exemplos de Comandos SQL no Script
```bash
CREATE TABLE IF NOT EXISTS

INSERT INTO ... VALUES (...)

SELECT * FROM tabela

UPDATE tabela SET ... WHERE ...

DELETE FROM tabela WHERE ...

ALTER TABLE ADD COLUMN
```

### 💾 Exemplo de Tabelas Criadas

```bash
customers

consumer

id, nome, email, telefone, endereco, cep, cidade

product_type

product_type_id, product_type_name

products

product_id, product_name, product_price, product_type (chave estrangeira)
```
### 📋 Exemplo de Saída Esperada
Ao rodar:

python
```bash
Copiar código
cursor.execute("SELECT * FROM products")
```
Você verá algo como:

```bash
Copiar código
(4, 'Notebook', 2000.0, 1)
(5, 'Celular', 1000.0, 2)
(6, 'Tablet', 1500.0, 1)
```
### 📌 Observações
O projeto não usa ORM, apenas SQL puro via psycopg2

Ideal para quem está começando com bancos relacionais e quer ver a lógica SQL na prática

Edite os comandos conforme sua necessidade ou para explorar novos cenários

### 📞 Contato
*Autor*: Ivan Martins

*Email*: ivanmarti.alves@gmail.com

*GitHub*: https://github.com/IvanM4rtin5