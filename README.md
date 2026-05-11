# Projeto Integrador 1 — PIJ110

Sistema de Gerenciamento de Estoque desenvolvido como projeto integrador da disciplina PIJ110 da UNIVESP.

**Empresa:** Mauricio Henrique Camargo | CNPJ: 11.458.173/0001-74 | Fundada em 2009
**Especialidade:** Suporte Técnico e Manutenção em TI

---

## Sumário

- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Banco de Dados](#banco-de-dados)
- [Módulos e Funções](#módulos-e-funções)
- [Fluxos da Aplicação](#fluxos-da-aplicação)
- [Como Executar](#como-executar)
- [Autenticação e Segurança](#autenticação-e-segurança)

---

## Tecnologias

| Tecnologia | Versão     | Finalidade                     |
| ---------- | ---------- | ------------------------------ |
| Python     | 3.12.12    | Linguagem principal            |
| Streamlit  | 1.55.0     | Interface web                  |
| SQLite3    | (built-in) | Banco de dados                 |
| pandas     | 2.3.3      | Manipulação de dados tabulares |
| hashlib    | (built-in) | Hashing de senhas (SHA-256)    |
| Pillow     | 12.1.1     | Processamento de imagens       |

---

## Estrutura do Projeto

```
univesp_pij110/
├── app.py                        # Ponto de entrada da aplicação Streamlit
├── criar_admin.py                # Script utilitário para criar o usuário admin
├── requirements.txt              # Dependências Python
├── ruff.toml                     # Configuração de linting (Ruff)
├── .python-version               # Versão do Python (3.12.12)
│
├── app/                          # Módulos de interface (páginas Streamlit)
│   ├── __init__.py
│   ├── app_home.py               # Página inicial com informações institucionais
│   └── app_estoque.py            # Páginas de gerenciamento de estoque
│
├── utils/                        # Módulos utilitários (lógica de negócio)
│   ├── __init__.py
│   ├── configuracao_db.py        # Configuração do banco e autenticação
│   └── estoque.py                # Operações CRUD do estoque
│
└── db/                           # Banco de dados
    ├── database.db               # Arquivo SQLite
    └── scripts/
        └── criacao_tabelas.sql   # DDL de criação das tabelas
```

---

## Banco de Dados

**Tipo:** SQLite
**Arquivo:** `db/database.db`
**DDL:** `db/scripts/criacao_tabelas.sql`

### Tabela `estoque`

Armazena os componentes de hardware gerenciados pelo sistema.

```sql
CREATE TABLE IF NOT EXISTS estoque (
    id_item          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome             TEXT,
    qtd_estoque      INTEGER,
    preco            REAL,
    descricao        TEXT,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

| Coluna             | Tipo      | Descrição                                                    |
| ------------------ | --------- | ------------------------------------------------------------ |
| `id_item`          | INTEGER   | Chave primária, autoincremento                               |
| `nome`             | TEXT      | Nome do componente                                           |
| `qtd_estoque`      | INTEGER   | Quantidade disponível em estoque                             |
| `preco`            | REAL      | Preço unitário em reais (R$)                                 |
| `descricao`        | TEXT      | Descrição técnica ou ficha do componente                     |
| `data_atualizacao` | TIMESTAMP | Data/hora da última modificação (atualizada automaticamente) |

### Tabela `usuarios`

Armazena os usuários com acesso ao sistema.

```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    username   TEXT UNIQUE,
    senha_hash TEXT
);
```

| Coluna       | Tipo    | Descrição                                 |
| ------------ | ------- | ----------------------------------------- |
| `id_usuario` | INTEGER | Chave primária, autoincremento            |
| `username`   | TEXT    | Nome de usuário único (constraint UNIQUE) |
| `senha_hash` | TEXT    | Hash SHA-256 da senha                     |

---

## Módulos e Funções

### `app.py` — Ponto de entrada

Inicializa a aplicação Streamlit, gerencia a sessão de autenticação e renderiza o menu de navegação.

#### `login(username, password) -> bool`

Verifica as credenciais do usuário contra o banco de dados.

| Parâmetro  | Tipo | Descrição                                    |
| ---------- | ---- | -------------------------------------------- |
| `username` | str  | Nome de usuário informado no formulário      |
| `password` | str  | Senha em texto plano informada no formulário |

**Retorno:** `True` se as credenciais forem válidas, `False` caso contrário.

**Fluxo:**
1. Chama `buscar_usuario(username)` para buscar o registro no banco.
2. Se encontrado, chama `verificar_senha(password, usuario_db[1])` para comparar o hash.
3. Armazena o estado na sessão Streamlit (`st.session_state.logged_in`).

---

### `app/app_home.py` — Página inicial

#### `st_home() -> None`

Exibe as informações institucionais da empresa na página inicial.

- Renderiza nome, CNPJ, ano de fundação e área de atuação.
- Utiliza `st.container()` com markdown e caption do Streamlit.

---

### `app/app_estoque.py` — Páginas de estoque

#### `st_verificar_estoque() -> None`

Página de consulta e atualização de estoque.

**Funcionalidades:**
- Exibe todos os componentes em uma tabela (`st.dataframe`).
- Campo de busca por nome (filtragem case-insensitive).
- Seletor de componente por ID e nome.
- Três painéis de ação rápida em colunas:

| Painel                 | Ação                                   | Função chamada           |
| ---------------------- | -------------------------------------- | ------------------------ |
| Adicionar Unidades     | Incrementa `qtd_estoque`               | `adicionar_quantidade()` |
| Dar Baixa (Retirada)   | Decrementa `qtd_estoque` com validação | `remover_quantidade()`   |
| Alterar Preço Unitário | Atualiza `preco`                       | `alterar_preco()`        |

---

#### `st_cadastrar_componente() -> None`

Página de cadastro de novos componentes.

**Campos do formulário:**

| Campo               | Obrigatório | Validação          |
| ------------------- | ----------- | ------------------ |
| Nome do Componente  | Sim         | Não pode ser vazio |
| Quantidade Inicial  | Sim         | Deve ser > 0       |
| Preço Unitário (R$) | Sim         | Deve ser > 0       |
| Descrição           | Não         | Campo livre        |

Ao submeter com dados válidos, chama `cadastrar_novo_componente()` e exibe mensagem de sucesso. O formulário é limpo automaticamente após o envio (`clear_on_submit=True`).

---

#### `st_remover_componente() -> None`

Página de exclusão permanente de componentes.

**Fluxo:**
1. Exibe aviso de atenção sobre a irreversibilidade da ação.
2. Renderiza seletor com todos os componentes.
3. Exige marcação de checkbox de confirmação.
4. Ao clicar em "Excluir Permanentemente" com confirmação marcada, chama `excluir_componente()`.
5. Exibe erro se a confirmação não estiver marcada.

---

### `utils/configuracao_db.py` — Configuração do banco e autenticação

Gerencia a conexão com o banco de dados e as funções de autenticação de usuários.

**Constantes:**
- `BASE_DIR`: Diretório raiz do projeto, resolvido dinamicamente a partir do caminho do arquivo.
- `DB_PATH`: Caminho absoluto para `db/database.db`.

#### `verificar_senha(senha_digitada, senha_no_banco) -> bool`

Compara a senha digitada com o hash armazenado no banco.

| Parâmetro        | Tipo | Descrição                                    |
| ---------------- | ---- | -------------------------------------------- |
| `senha_digitada` | str  | Senha em texto plano fornecida pelo usuário  |
| `senha_no_banco` | str  | Hash SHA-256 armazenado na tabela `usuarios` |

**Retorno:** `True` se os hashes coincidirem, `False` caso contrário.

**Implementação:** Aplica `hashlib.sha256(senha_digitada.encode()).hexdigest()` e compara o resultado com `senha_no_banco`.

---

#### `buscar_usuario(username) -> tuple | None`

Busca um usuário na tabela `usuarios` pelo nome de usuário.

| Parâmetro  | Tipo | Descrição                     |
| ---------- | ---- | ----------------------------- |
| `username` | str  | Nome de usuário a ser buscado |

**Retorno:** Tupla `(username, senha_hash)` se encontrado, ou `None` se não existir.

**Query executada:**
```sql
SELECT username, senha_hash FROM usuarios WHERE username = ?
```

---

#### `criar_admin_inicial(username, senha) -> None`

Cria um novo usuário no banco de dados. Utilizado pelo script `criar_admin.py`.

| Parâmetro  | Tipo | Descrição                                                        |
| ---------- | ---- | ---------------------------------------------------------------- |
| `username` | str  | Nome de usuário a ser criado                                     |
| `senha`    | str  | Senha em texto plano (será transformada em hash antes de salvar) |

**Comportamento:**
- Gera o hash SHA-256 da senha antes de inserir.
- Captura `sqlite3.IntegrityError` para evitar duplicidade de `username`.
- Imprime mensagem de sucesso ou "Usuário já existe." no console.

---

### `utils/estoque.py` — Lógica de negócio do estoque

Contém todas as operações de leitura e escrita na tabela `estoque`.

**Constantes:**
- `BASE_DIR`: Diretório raiz do projeto.
- `DB_PATH`: Caminho absoluto para `db/database.db`.

#### `executar_query(query, params=()) -> None`

Função auxiliar que encapsula a abertura de conexão, execução, commit e fechamento.

| Parâmetro | Tipo  | Descrição                                                        |
| --------- | ----- | ---------------------------------------------------------------- |
| `query`   | str   | Instrução SQL a ser executada                                    |
| `params`  | tuple | Parâmetros para substituição parametrizada (padrão: tupla vazia) |

Utilizada internamente por `cadastrar_novo_componente`, `adicionar_quantidade`, `alterar_preco`, `remover_quantidade` e `excluir_componente`.

---

#### `listar_estoque() -> pd.DataFrame`

Retorna todos os componentes cadastrados em um DataFrame pandas.

**Retorno:** DataFrame com as colunas:

| Coluna no DataFrame   | Coluna no banco    |
| --------------------- | ------------------ |
| ID                    | `id_item`          |
| Nome                  | `nome`             |
| Quantidade em Estoque | `qtd_estoque`      |
| Preço                 | `preco`            |
| Descrição             | `descricao`        |
| Data de Atualização   | `data_atualizacao` |

**Query executada:**
```sql
SELECT id_item, nome, qtd_estoque, preco, descricao, data_atualizacao FROM estoque
```

---

#### `cadastrar_novo_componente(nome, qtd, preco, descricao) -> None`

Insere um novo componente na tabela `estoque`.

| Parâmetro   | Tipo  | Descrição                       |
| ----------- | ----- | ------------------------------- |
| `nome`      | str   | Nome do componente              |
| `qtd`       | int   | Quantidade inicial em estoque   |
| `preco`     | float | Preço unitário em R$            |
| `descricao` | str   | Descrição técnica do componente |

**Query executada:**
```sql
INSERT INTO estoque (nome, qtd_estoque, preco, descricao) VALUES (?, ?, ?, ?)
```

---

#### `adicionar_quantidade(id_item, qtd_adicional) -> None`

Incrementa a quantidade em estoque de um componente existente e atualiza o timestamp.

| Parâmetro       | Tipo | Descrição                         |
| --------------- | ---- | --------------------------------- |
| `id_item`       | int  | ID do componente a ser atualizado |
| `qtd_adicional` | int  | Quantidade a ser adicionada       |

**Query executada:**
```sql
UPDATE estoque
SET qtd_estoque = qtd_estoque + ?,
    data_atualizacao = CURRENT_TIMESTAMP
WHERE id_item = ?
```

---

#### `alterar_preco(id_item, novo_preco) -> None`

Altera o preço unitário de um componente e atualiza o timestamp.

| Parâmetro    | Tipo  | Descrição                         |
| ------------ | ----- | --------------------------------- |
| `id_item`    | int   | ID do componente a ser atualizado |
| `novo_preco` | float | Novo preço unitário em R$         |

**Query executada:**
```sql
UPDATE estoque
SET preco = ?,
    data_atualizacao = CURRENT_TIMESTAMP
WHERE id_item = ?
```

---

#### `remover_quantidade(id_item, qtd_remover) -> bool`

Realiza uma baixa de estoque com validação prévia de quantidade disponível.

| Parâmetro     | Tipo | Descrição                            |
| ------------- | ---- | ------------------------------------ |
| `id_item`     | int  | ID do componente a ser baixado       |
| `qtd_remover` | int  | Quantidade a ser retirada do estoque |

**Retorno:** `True` se a operação foi realizada com sucesso, `False` se o estoque for insuficiente.

**Fluxo:**
1. Consulta `qtd_estoque` atual do item.
2. Se `qtd_estoque >= qtd_remover`, executa o UPDATE e retorna `True`.
3. Caso contrário, retorna `False` sem alterar o banco.

**Queries executadas:**
```sql
-- Verificação prévia
SELECT qtd_estoque FROM estoque WHERE id_item = ?

-- Atualização (somente se estoque suficiente)
UPDATE estoque
SET qtd_estoque = qtd_estoque - ?,
    data_atualizacao = CURRENT_TIMESTAMP
WHERE id_item = ?
```

---

#### `excluir_componente(id_item) -> None`

Remove permanentemente um componente do banco de dados.

| Parâmetro | Tipo | Descrição                       |
| --------- | ---- | ------------------------------- |
| `id_item` | int  | ID do componente a ser excluído |

**Query executada:**
```sql
DELETE FROM estoque WHERE id_item = ?
```

> **Atenção:** Esta operação é irreversível. O registro e todo o histórico do componente serão apagados.

---

### `criar_admin.py` — Script utilitário

Script de uso único para criação do usuário administrador inicial.

**Execução:**
```bash
python criar_admin.py
```

Chama `criar_admin_inicial("mauricio", "senha123")`, criando o usuário `mauricio` com a senha definida (armazenada como hash SHA-256). Deve ser executado apenas uma vez após a inicialização do banco.

---

## Fluxos da Aplicação

### Autenticação

```
Usuário acessa a aplicação
        │
        ▼
   Formulário de login (sidebar)
        │
        ▼
buscar_usuario(username)  ──────► None → "Usuário ou senha incorretos"
        │
        ▼
verificar_senha(password, hash)  ─► False → "Usuário ou senha incorretos"
        │
        ▼
  st.session_state.logged_in = True
        │
        ▼
     Menu de navegação
```

### Cadastro de componente

```
Usuário preenche o formulário
        │
        ▼
Validação: nome ≠ "" e qtd > 0 e preco > 0
        │
   falhou → st.error()
        │
        ▼
cadastrar_novo_componente(nome, qtd, preco, descricao)
        │
        ▼
  INSERT INTO estoque → st.success()
```

### Baixa de estoque

```
Usuário seleciona componente e informa quantidade
        │
        ▼
remover_quantidade(id_item, qtd_remover)
        │
  SELECT qtd_estoque ── qtd < qtd_remover ──► return False → st.error()
        │
  qtd >= qtd_remover
        │
        ▼
  UPDATE estoque → return True → st.success()
```

### Exclusão de componente

```
Usuário seleciona componente
        │
        ▼
checkbox de confirmação não marcado ──► st.error()
        │
   confirmado
        │
        ▼
excluir_componente(id_item)
        │
        ▼
  DELETE FROM estoque → st.success() → st.rerun()
```

---

## Como Executar

### Pré-requisitos

- Python 3.12.12
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd univesp_pij110

# 2. Crie e ative o ambiente virtual
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\activate.ps1

# 3. Instale as dependências
pip install -r requirements.txt
```

### Inicialização do banco de dados

O arquivo `db/database.db` já está incluído no repositório com as tabelas criadas. Para recriar o banco do zero:

```bash
sqlite3 db/database.db < db/scripts/criacao_tabelas.sql
```

### Criação do usuário administrador

Execute o script utilitário uma única vez para criar o usuário inicial:

```bash
python criar_admin.py
```

> O script cria o usuário `mauricio` com a senha `senha123`. Altere as credenciais no arquivo antes de executar em produção.

### Execução

```bash
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`.

---

## Autenticação e Segurança

- Senhas armazenadas como hash SHA-256 (`hashlib.sha256`).
- Nenhuma senha em texto plano é persistida no banco.
- Controle de acesso via `st.session_state` do Streamlit — todas as páginas de estoque exigem `logged_in = True`.
- Queries SQL utilizam substituição parametrizada (`?`) para evitar SQL Injection.
- O banco SQLite é adequado para implantações de usuário único ou pequenas equipes. Para múltiplos usuários simultâneos, considere migrar para PostgreSQL.

---

## Autores

- Bruno Garcia Piato
- Maria Paula Garcia Lucio
- Maria Claudia Poli
- Pedro Conciani Ribeiro
- Glauber Guimarães Monteiro Bispo
- Maurício Henrique Camargo
- Deivid Rodrigo Correia de Melo

— Projeto Integrador 1, UNIVESP (PIJ110)
