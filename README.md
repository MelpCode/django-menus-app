## django menus app

This app was created usign Django Web Framework and PostgreSQL.

### Steps to start the project

1. Create a project folder:

```
  mkdir django-menus-app
```

2. Create a virtual enviroment 

```
  python -m virtualenv venv
```

3. Clone the repository

```
  git clone https://github.com/MelpCode/django-menu-app.git
```

3. Activate virtual enviroment

```
  .\venv\Scripts\activate
```

4. Install libraries

```
  pip install -r requirements.txt
```

5. Active your PostgreSQL client

6. Create your ```.env``` file within *django_menus_app* folder and set:

```PSQL_NAME``` ```PSQL_HOST``` ```PSQL_USER``` ```PSQL_PASSWORD``` ```PSQL_PORT```

7. Create a database with the name registered ````PSQL_NAME```

```sql
  CREATE DATABASE <NAME>
```

8. Make migrations:

  move to the folder django_menus_app

  ```
    python manage.py migrate
  ```

  ```
    python manage.py makemigrations
  ```

8. Move to the django_menus_app folder and type in your CMD

```
  python manage.py runserver
```
