# inlineformsettemp

Tentando rodar o inlineformset_factory.

## Como colaborar

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo 'SECRET_KEY=my_secret_key' > .env
echo 'DEBUG=True' >> .env
echo 'ALLOWED_HOSTS=127.0.0.1, .localhost' >> .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```