## Excutando projeto localmente:
##### Clonando o projeto:
```bash
git clone https://github.com/jefersondeff/api_challenge
cd api_challenge
```

##### Criando e ativando ambiente virtual:
```bash
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

##### Instalando dependências:
```pip
pip install -r requeriments.txt
```

##### Criando banco de dados:
``` python 
python manage.py migrate
```

##### Adicionado dados fake para teste:
```python
python manage.py loaddata app/fixture/fake_db.json 
```

##### Executando:
```python
python manage.py runserver
```