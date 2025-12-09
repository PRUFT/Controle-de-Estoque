📦 Controle de Estoque – Sistema em Python + Streamlit

Um sistema simples e funcional para controle de produtos, desenvolvido em Python, utilizando SQLite como banco de dados e Streamlit como interface gráfica.
Ideal para pequenos comércios, uso pessoal ou estudo.

🚀 Funcionalidades

Cadastro de produtos

Consulta de produtos

Atualização de registros

Exclusão de registros

Banco de dados local em SQLite (produtos.db)

Interface rápida e leve via Streamlit

🛠 Tecnologias utilizadas

Python 3

Streamlit – interface web

SQLite3 – banco de dados local

Pandas – manipulação de tabelas

OS / pathlib – manipulação de arquivos

📁 Estrutura do projeto
Controle-de-Estoque/
│
├── app.py
├── funcoes.py
├── registro.py
│
├── produtos.db
├── login.db
│
├── pages/
│   ├── MENU.py
│   └── (outras páginas do Streamlit)
│
└── README.md

▶️ Como executar o projeto
1. Execute o terminal na pasta base

Clique com o botão direito em um espaço vazio na pasta do Controle de Estoque e clique em executar no cmd 

2. Instale as dependências

No terminal:

pip install streamlit pandas

3. Execute o App
python - m streamlit run app.py

4. Login
Usuário:admin
Senha:123456

O navegador abrirá automaticamente a interface.

🧩 Descrição dos principais arquivos
app.py

Arquivo principal do Streamlit.
Carrega as páginas, menu e navegação.

funcoes.py

Contém as funções principais do sistema:

conexão com o banco

inserção de produtos

edição

exclusão

busca por código ou nome

registro.py

Tela responsável pelo cadastro de novos usuários (opcional).

produtos.db

Banco SQLite onde ficam armazenados:

código

produto

preço

unidade de medida

quantidade

🗃 Banco de Dados
Estrutura da tabela produtos
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prod TEXT NOT NULL,
    cod TEXT NOT NULL,
    prec REAL NOT NULL,
    und TEXT NOT NULL
);



🤝 Contribuição

Sinta-se livre para:

abrir issues

sugerir melhorias

enviar PRs

📜 Licença

Este projeto é distribuído sob a licença MIT.
Você pode usar, copiar, modificar e distribuir livremente.
