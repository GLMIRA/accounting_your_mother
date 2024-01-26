
# Comamando uteis:
## DJANGO

**para rodar o projeto usando como base de dados do sqlite3, antes de dar os comandos abaixo setar a vaiavel de ambiente `DJANGO_DATABASE='tests'` usando o comando `export`. Caso isso não seja feito o projeto vai tentar encontrar o servidor do mariadb**
```bash
export DJANGO_DATABASE='tests' && python manage.py runserver
```
- Rodar o servidor: `python manage.py runserver`
- Migrações: `python manage.py makemigrations` e `python manage.py migrate`
- criar o super usuário: `python manage.py createsuperuser`
- rodar o shell: `python manage.py shell`

## URLS:
- Django Admin: `http://127.0.0.1:8000/admin/`
- Django DOCS: `https://docs.djangoproject.com/en/5.0/intro/tutorial01/`


## ordem das coisas
1. Clonar o repositório
2. Criar um virtualenv
3. Ativar o virtualenv
4. Instalar as dependências
5. Rodar o migrate
6. Rodar o servidor

## Extensões do VSCode
- Python
- Todo Tree
- Todo Highlight


## Arquivo .env
1. Criar o arquivo `.env` dentro da pasta `aym`:
```
    aym/
        aym/
        control_payments/
        .env     <----------------- aqui
        docker-compose.yml
        Dockerfile
        manage.py
        requirements.txt
```
2. O arquivo `.env` deve ter as seguintes definições de variaveis:
```bash
# Django Configuration
DJANGO_SECRET_KEY=secret_key_gerada_pelo_django #(veja gerar a chave mais abaixo)
DJANGO_DEBUG=True # deve ser True ou False, onde True é para desenvolvimento e False para produção
DJANGO_ALLOWED_HOSTS=* # é uma lista de IP's separados por espaço " " na qual o aceita receber requisições. Caso esteja com * aceita de qualquer IP. O aconselhavel é colocar somente o IP da rede na qual o projeto está rodando, por exemplo: 192.168.0.0/24
# MySQL settings
MYSQL_ROOT_PASSWORD=root # senha do root do banco de dados
MYSQL_DATABASE=aym # nome do banco de dados
MYSQL_USER=aym_user # nome do usuário do banco de dados na qual o django vai usar para se conectar
MYSQL_PASSWORD=password # senha do usuário do banco de dados do django
```

3. Gerar a `DJANGO_SECRET_KEY`:
- Abra o terminal e digite o seguinte comando:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```


## Docker
1. Instalar o docker e o docker-compose
2. Criar o diretorio de dados do mysql:
```bash
# dentro da pasta raiz do projeto criar o diretorio db
mkdir db
# caso esteja usando linux, dar permissão de escrita para o usuario do docker
sudo chown -R 777 ./db
```
```
o resultado de como deve ficar a estrutura de pastas:
aym/
    aym/
    control_payments/
    .env
    docker-compose.yml
    Dockerfile
    manage.py
    requirements.txt
db/     <----------------- aqui
```
2. Rodar o comando `docker-compose up -d --build` dentro da pasta `aym` para subir os containers do projeto