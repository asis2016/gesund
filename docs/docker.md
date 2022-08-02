## Or, use **Docker**

```shell
$ mkdir gesund_docker
$ cd gesund_docker
gesund_docker $ git clone https://github.com/asis2016/gesund.git .
```

Copy provided `.env`, `docker-compose.yml`, `Dockerfile`, and `requirements.txt` in the `gesund_docker` root folder.

**docker-compose.yml**

```yaml
version: '3.7'

services:
  web:
    build: .
    command: python /code/gesund/manage.py runserver 0.0.0.0:9001
    volumes:
      - .:/code

    ports:
      - 9001:9001

    depends_on:
      - db

  db:
    image: mysql:5.7
    environment:
      MYSQL_DATABASE: 'gesund'
      MYSQL_ALLOW_EMPTY_PASSWORD: 'true'
    volumes:
      - ./data/mysql/db:/var/lib/mysql
```

**Dockerfile**

```
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

COPY . /code/
```

**requirements.txt**
```
asgiref==3.5.2
backports.zoneinfo==0.2.1
Django==4.0.6
django-active-link==0.1.8
django-cors-headers==3.11.0
django-filter==21.1
djangorestframework==3.13.1

protobuf==4.21.2
python-dotenv==0.20.0
pytz==2022.1
sqlparse==0.4.2
whitenoise==6.2.0
XlsxWriter==3.0.3

mysqlclient>=2.0
```

**.env**

```
# LOCAL
ENVIRONMENT='local'
REST_API_URL='http://192.168.2.110:8000/api/v1'
REST_API_BEARER_TOKEN=''
DB_DATABASE='gesund'
DB_USER='root'
DB_PASS=''
ALLOWED_HOSTS_ENV='localhost 127.0.0.1 *'
CORS_ORIGIN_WHITELIST_ENV='http://localhost:8000 http://127.0.0.1:8000'

# EMAIL
EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
DEFAULT_FROM_EMAIL=''
RECEIVE_EMAIL_AT=''
```

**pipenv install**

```shell
gesund_docker $ pipenv shell
(gesund_docker-xyz) $ pipenv install -r requirements.txt
```

Update `settings.py` with the following information:

```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db',                             #new
        'PORT': '3306',
        'NAME': DB_DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PASS
    }
}
```





The docker build command builds Docker images from a Dockerfile:

```shell
(gesund_docker-xyz) $ docker build . -t gesund_img

Sending build context to Docker daemon  17.88MB
Step 1/7 : FROM python:3.8
3.8: Pulling from library/python
d836772a1c1f: Downloading  23.12MB/55MB
66a9e63c657a: Download complete 
d1989b6e74cf: Download complete 
c28818711e1e: Downloading   5.34MB/54.58MB
5084fa7ebd74: Downloading  8.014MB/196.8MB
7f162c881e4f: Waiting 
3834558b67a0: Waiting 
edcbbf846ff7: Waiting 
865a38cd8857: Pulling fs layer
```

The docker-compose up starts and restart all the services mentioned in `docker-compose.yml`:

```shell
(gesund_docker-xyz) $ docker-compose up -d
```



Database migration:

```shell
(gesund_docker-xyz) $ docker-compose exec web python gesund/manage.py migrate
```

create superuser:

```shell
(gesund_docker-xyz) $ docker-compose exec web python gesund/manage.py createsuperuser

username: admin
password: *****
```

Now, check if [localhost:9001](http://0.0.0.0:9001/) is working.

### Docker container

```shell
$ docker ps -a
```

Stop a container

```shell
$ docker stop <container_id>
```

**Warning:** Deleting all container

```shell
$ docker rm -f $(docker ps -a -q)
```

### Docker image

```shell
$ docker images
```

### checking MySQL

```shell
(gesund_docker-xyz) $ docker exec -it <container_id> bash
bash-4.2# mysql
mysql> show databases;  

+--------------------+
| Database           |
+--------------------+
| information_schema |
| gesund             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

```shell
mysql > use gesund;
mysql > show tables;

+-----------------------------+
| Tables_in_gesund            |
+-----------------------------+
| aboutus_contactus           |
| accounts_usersignlog        |
| auth_group                  |
| auth_group_permissions      |
| auth_permission             |
| auth_user                   |
| auth_user_groups            |
| auth_user_user_permissions  |
| calories_caloriecategory    |
| calories_caloriefooddetail  |
| calories_calorieintake      |
| challenges_challenge        |
| django_admin_log            |
| django_content_type         |
| django_migrations           |
| django_session              |
| goals_goals                 |
| history_history             |
| pomodoros_pomodoro          |
| postpilottest_postpilottest |
| profiles_profile            |
| steps_steps                 |
| water_intake_waterintake    |
| weights_weight              |
| xps_xp                      |
+-----------------------------+
25 rows in set (0.00 sec)
```
 