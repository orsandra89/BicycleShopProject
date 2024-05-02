## Setup project

First of all python venv environment should be setup after clone repo:

```python -m venv /path/to/cloned/project/root```

This new venv environment should be activated. To do so, execute command from project root:

Linux: `./.venv/activate`
Windows: `./.venv/activate.bat`

then all dependencies should be installed. To do so just execute:

```pip install -r requirements.txt```

Basic project setup done

### Run third party applications

To start application database should be started first. To do so docker-compose configuration prepared under ./dev-scripts folder.

Execute from dev-scripts folder:
```docker-compose -f docker-compose.yaml up -d db pgadmin```

### Setup test environment

Now we need to setup database and create superadmin:

Basic migration already generated. To load it to db execute:

```python manage.py migrate```

To create superuser execute:

```python manage.py createsuperuser```

To start application run:

```python manage.py runserver```

### Run application in docker

There is possibility to run backend and DB in docker to do so execute from ./dev-scripts command:

```docker-compose -f docker-compose.yaml up -d db pgadmin bicycle```

### Change model

if model changed migration files should be generated and executed on DB.

execute command to generate migration files:

```python manage.py makemigrations```

execute migration changes:

```python manage.py migrate```

## Test Api

OpenApi used to generate api schema. To download it start application and paste in browser url

```GET <host>:<port>/api/schema/```

Downloaded schema could be used to load to, for example, postman, which generate example requests.
