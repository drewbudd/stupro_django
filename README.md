# stupro_django

Running on your system locally
1. Make sure you have Python 3 installed (I will assume your python command is just python, not python3)
2. Install pipenv, start a pipenv shell from base directory, install dependencies
   1. ```pip install pipenv```
   2. ```pipenv shell```
   3. ```pipenv sync```
3. Create a blank file named ```db.sqlite3```
4. Initialize database and create superuser
   1. ```python manage.py makemigrations```
   2. ```python manage.py migrate```
   3. ```python manage.py createsuperuser``` , just follow the steps here
5. Start the server with ```python manage.py runserver```
   