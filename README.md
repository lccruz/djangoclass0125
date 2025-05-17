## Como instalar e rodar este repositório

### Pré-requisitos

- Python 3.8+
- pip
- Virtualenv (opcional, mas recomendado)

### Passos para instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/djangoclass0125.git
    cd djangoclass0125
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Comandos úteis

- **Criar as migrações:**
  ```bash
  python manage.py makemigrations
  ```

- **Aplicar as migrações:**
  ```bash
  python manage.py migrate
  ```

- **Criar um superusuário Django:**
  ```bash
  python manage.py createsuperuser
  ```

- **Rodar o servidor de desenvolvimento:**
  ```bash
  python manage.py runserver
  ```

Acesse o painel administrativo em `http://127.0.0.1:8000/admin/` após criar o superusuário.