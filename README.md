## Excutando projeto localmente:
#### Manualmente:

##### Clonando o projeto:
```bash
git clone https://github.com/jefersondeff/api_challenge
cd api_challenge
```

##### Criando e ativando ambiente virtual:
```bash
python3.8 -m venv venv
source venv/bin/activate
```

##### Instalando dependências:
```pip
pip install -r requeriments.txt
```

#### Criando banco de dados:
``` python 
python manage.py migrate
```

#### Executando:
```python
python manage.py runserver
```