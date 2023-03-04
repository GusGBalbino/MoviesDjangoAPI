# Boas-vindas ao repositório do Movies API!

Projeto criado para o desafio técnico da empresa Ubots

Vaga: Desenvolvedor Back-End Júnior

# Orientações
<details>
  <summary><strong>⚠ Dependências</strong></summary><br />

  1. Python 3.10
  2. Django 4.0
  
</details>

<details>
  <summary><strong>⚠ Para rodar esse projeto siga os seguintes passos</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone https://github.com/GusGBalbino/MoviesDjangoAPI.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd MoviesDjangoAPI`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Rode a migrate do banco de dados

  - `python manage.py makemigrations`
  - `python manage.py migrate`

  4. Rode o aplicado

  -`python manage.py runserver`

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```
</details>

# Rotas:

## 1 - /movies

Essa rota é responsável pelo cadastro de novos filmes no banco de dados

- A rota deve receber o título, nome do diretor e o ano do filme
- O id é criado automáticamente
- Nessa mesma rota é mostrada a lista dos filmes já cadastrados

## 2 - /rate

É possível, a partir do id de um filme já cadastrado no banco de dados adicionar uma nota a ele.

- A rota recebe o id do filme e a nota.
- Ela também lista as notas e os id's já cadastrados.

## 3 - /movies/<id_movie>/total

Essa rota é responsável por fazer a média de notas a partir do id de um filme.

- A rota recebe como parâmetro o id de um filme já cadastrado e retorna a média seguindo a seguinte fórmula:

  ```
    Soma das notas de todos os registros = SN
    Quantidade de registros = QR

    Fórmula: Total = SN / QR
  ```

- Se não houver registros retorna 0

## 4 - /norate

Essa rota é responsável por retornar os filmes não avaliados, a partir de sua nota.

- A rota retorna as informações dos filmes em lista, que foram avaliados sem nota ou com nota = 0.0



## ✒️ Autor

* **Gustavo Gomes** - *API* - [GusGBalbino](https://github.com/GusGBalbino)
