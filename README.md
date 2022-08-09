# Landinator

Sistema de geração de landing pages com formulários

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com python 3.9
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:unisagrado/landinator.git <path/to/workspace>
cd <path/to/workspace>
python -m venv .venv
.vend\Scripts\activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
ALLOWED_HOSTS = ['localhost', '0.0.0.0'] //comentar o antigo ALLOWED_HOSTS e deixar esse apenas no local, reverte esta alteração quando for enviar para o github
python manage.py makemigrations
python manage.py migrate
```

## Como fazer o deploy?

1. Envie o código para o github.


```console
git push origin master
```