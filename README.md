# Introduction

The Gesund App (hereinafter "APP") is a <i>Self-management Gamification Web Application</i> developed as a master thesis
project at the
University of Koblenz-Landau.

The thesis is titled 'Introducing Gamification to overcome employee's health-related risks in work from home (WfH)
settings'. In short, the intervention is trying to find out if the APP is helpful for employees to overcome
health-related risks in their remote work setting.

## Table of contents (WIP)

- [Project organization](#)
- [Tech stack](#)
- [Installation](#)
    - [GIT clone](#)
    - [Python VENV](#)
    - [MySQL Server](#)

- [UML Use case diagram](#uml-use-case-diagram)
- [Database](#database)
    - [Table overview](#table-overview)
    - [Table details](#table-details)
    - [Dummy data setup](#dummy-data-setup)
- [Tests](#tests)
- [Deployment](#deployments)
- [End-user documentation](#end-user-documentation)
- [Feedback](#feedback)
- [Contributing](#contributing)
- "Legal"
    - [Disclaimer](#disclaimer)
    - [License](#license)
    - [Privacy Policy](#privacy-policy)
- [References](#references)
- [Images, vectors, or icons](#images-vectors-or-icons)


## Project organization

## Tech stack

1. [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
2. [Django 4.0.6](https://docs.djangoproject.com/en/4.0/releases/4.0.6/)
3. [MySQL 8.0.29](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-29.html)
4. [Shell Scripts](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html)
5. [Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/download/)
6. [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/)

## Installation

**GIT Clone from Github**

First step is to make a directory.

```shell
$ mkdir gesund_project
$ cd gesund_project
```

Then, clone the [Gesund App repository](https://github.com/asis2016/gesund) from the GitHub.

```shell
gesund_project $ git clone https://github.com/asis2016/gesund.git .
gesund_project $ cd gesund
```

**Python VENV**

Install and activate [Python virtual environments](https://docs.python.org/3/tutorial/venv.html). And activate it.

```shell
gesund_project/gesund $ python3 -m venv venv
gesund_project/gesund $ source venv/bin/activate
```

Once it has been activated, install `requirements.txt`.

```shell
(venv) gesund_project/gesund $ pip install -r requirements.txt
```

### MySQL database

The Gesund App requires MySQL database. Hence, you should create:

1. MySQL Database: `gesund`
2. MySQL username: `your_username`
3. MySQL password: `your_password`

#### phpMyAdmin

todo: step-by-step phpMyAdmin `gesund` setup

### `.env` file

The project depends on .env file.

```shell
(venv) gesund_project/gesund $ touch .env
```

```
# LOCAL
ENVIRONMENT='local'
REST_API_URL='localhost:8000/api/v1'
REST_API_BEARER_TOKEN=''
DB_DATABASE='gesund'
DB_USER='your_mysql_username'
DB_PASS='your_mysql_password'
ALLOWED_HOSTS_ENV='localhost 127.0.0.1 *'
CORS_ORIGIN_WHITELIST_ENV='http://localhost:8000 http://127.0.0.1:8000'

# EMAIL
EMAIL_HOST='your_email_host'
EMAIL_PORT=''
EMAIL_HOST_USER='noreply@your_email_host'
EMAIL_HOST_PASSWORD=''
DEFAULT_FROM_EMAIL='noreply@your_email_host'
RECEIVE_EMAIL_AT='info@your_email_host'
```

**Start migration process**

```shell
(venv) gesund_project/gesund $ python manage.py showmigrations
(venv) gesund_project/gesund $ python manage.py makemigrations
(venv) gesund_project/gesund $ python manage.py migrate
```

**Create Django superuser**

```shell
(venv) gesund_project/gesund $ python manage.py createsuperuser

Username: djangoadmin
Email address: admin@example.com
Password: dj4n604dm1n
```

**Runserver**

```shell
(venv) gesund_project/gesund $ python manage.py runserver 0.0.0.0:8000
```

Your development server must be running at [http://0.0.0.0:8000/](http://0.0.0.0:8000/).

**Validate admin page**

Validate the admin page by going to [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin). And provide the
following credentials:

`username`: `djangoadmin`

`password`: `dj4n604dm1n`

**Update bearer token**

Bearer token is used as a authentication mechanism for REST API. Now, update your `.env`:

```shell
(venv) gesund_project/gesund $ printf '%s' 'djangoadmin:dj4n604dm1n' | base64
```

```
ZGphbmdvYWRtaW46ZGo0bjYwNGRtMW4=
```

```shell
(venv) gesund_project/gesund $ vi .env

---
REST_API_URL='localhost:8000/api/v1'
REST_API_BEARER_TOKEN='ZGphbmdvYWRtaW46ZGo0bjYwNGRtMW4=' #new
---
```

**Is your REST API working?**

Let's check if it is working:

```shell
curl --location --request GET 'http://127.0.0.1:8000/api/v1/echo/' \
--header 'Authorization: Basic ZGphbmdvYWRtaW46ZGo0bjYwNGRtMW4='
```

You should receive response:

```
{"message":"Hello, world!"}
```

### site.webmanifest

Change `start_url` to a relevant URL.

```shell
{
  "name": "Gesund APP",
  "short_name": "GA",
  "start_url": "http://192.168.2.110:8000/",
  ....
}
```

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
 ## User flow

User flow is used for describing the process of interaction between a user and the website. The following image presents
the 'flow' from the Gesund App entry point until the final action, i.e., Logging out.

![sitemap](./resources/images/user_flow.svg)

<p align="center">
Figure. User flow of the Gesund app (own representation).
</p>

### Example of the user flow

A simplified example of setting the goal in the app would be:

1. The user logs in successfully.
2. From the Dashboard page, the user clicks on the Profile menu.
3. From the menu, the user navigates towards the My Goals page.
4. On the page, the user can view her current Goals.
5. By clicking on Update your goals, she is then sent to the Goals update page.
6. Now, she will set her goals by providing relevant information.
7. Finally, she sees the confirmation message.

Above mentioned example of a user flow is called a 'happy path,' which means a simplified version of the user flow has a
successful response.

Reference: ## Wireframes

### Login or Sign up

![login or Sign up](./resources/images/wireframe_sm_login_sign_up.svg)


### Dashboard

![dashboard](./resources/images/wireframe_sm_dashboard.svg)

### Profile

![profile](./resources/images/wireframe_sm_profile.svg)

### Food intake

![food intake](./resources/images/wireframe_sm_food_intake.svg)

### Steps

![steps](./resources/images/wireframe_sm_steps.svg)


### Water intake

![water intake](./resources/images/wireframe_sm_water_intake.svg)

### Weights

![weights](./resources/images/wireframe_sm_weight.svg)

### About us

![about us](./resources/images/wireframe_sm_about_us.svg)

![](./resources/images/)



wireframe_sm_water_intake.drawio
wireframe_sm_weight.drawio



## Mockup

### Login system

![login system](./resources/images/mockup_sm_login_signup.svg)

### Dashboard

![dashboard](./resources/images/mockup_sm_dashboard.svg)

### Profile

![profile](./resources/images/mockup_sm_profile.svg)

### Food intake

![food intake](./resources/images/mockup_sm_food_intake.svg)

### Pomodoro

![pomodoro](./resources/images/mockup_sm_pomodoro.svg)

### Steps

![steps](./resources/images/mockup_sm_steps.svg)

### Water

![water](./resources/images/mockup_sm_water_intake.svg)

### Weight

![weight](./resources/images/mockup_sm_weight.svg)

### About

![about](./resources/images/mockup_sm_about.svg)



## Sitemap

<p>
A sitemap is a collection of pages on a website. In a simple form, it is a map of the website. Draw.io was used to
create the visual sitemap of the Gesund app.
</p>

![sitemap](./resources/images/sitemap.svg)

<p align="center">
    <i>Figure. Visual sitemap of the Gesund app (own representation).</i>
</p>

## UML use case diagram

![sitemap](./resources/images/uml_use_case_diagram.svg)

## Database

Entity-Relationship Diagram (ERD) is a standard approach for data structures and database systems design (todo:erd.pdf).
The
figure:todo represents the ERD of the Gesund app that provides a visual overview of the database and the
relations between tables. The tables are created during the app installation (see the migration process(todo:link)). The
table:todo includes additional information on the database tables.

![Database diagram](./resources/images/erd.svg)

<p align="center">
<i>Figure:todo Entity-Relationship Diagram (ERD) of the Gesund App.</i>
</p>

### Table overview

This table overview section provides brief information on the project database tables.

```shell
$ mysql -u <username> -p
```

```shell
mysql> show databases;
mysql> use gesund;
mysql> show tables;

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
| profiles_profile            |
| steps_steps                 |
| water_intake_waterintake    |
| weights_weight              |
| xps_xp                      |
+-----------------------------+
24 rows in set (0,00 sec)
```

| Table name                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                         | Relevant area(s) of the Gesund App UI                                                                                                                              |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auth_user                                                                                 | The table is a part of the built-in Django authentication system. It stores users' data like username, password, email, is_staff, last_login, et cetera. Furthermore, the authentication system handles groups, permissions, and cookie-based user sessions. See [official documentation](https://docs.djangoproject.com/en/4.1/topics/auth/) for more information.                                 | <ul><li>/accounts/login/</li><li>/accounts/logout/</li><li>/accounts/signup/</li><li>/accounts/password_reset/</li><li>/accounts/password_change/</li></ul>        |
| profiles_profile                                                                          | The table manages users' profile. It has one-to-one relationship with the `user` table.                                                                                                                                                                                                                                                                                                             | <ul><li>/profile/</li><li>/profile/:id/update/</li></ul>                                                                                                           |
| goals_goals                                                                               | The table describes the goals of the user for daily food intake (cal), daily water intake (L), and weight (kg).                                                                                                                                                                                                                                                                                     | <ul><li>/goals/</li><li>/goals/:id/update/</li></ul>                                                                                                               |
| calories_caloriefooddetail                                                                | The table is extracted from the flattened USDA National Nutrient MongoDB Database. The original article can be found at [https://data.world/craigkelly/usda-national-nutrient-db](https://data.world/craigkelly/usda-national-nutrient-db), and the original database can be found at [http://www.ars.usda.gov/Services/docs.htm?docid=8964](http://www.ars.usda.gov/Services/docs.htm?docid=8964). | NA                                                                                                                                                                 |
| calories_caloriecategory                                                                  | The table manages category for `caloriefooddetail` table.                                                                                                                                                                                                                                                                                                                                           | NA                                                                                                                                                                 |
| calories_calorieintake                                                                    | The table manages users' food intake based on the `caloriefooddetail` data.                                                                                                                                                                                                                                                                                                                         | <ul><li>/foods/</li><li>/foods/calorie-intake-datestamp-collection/:datestamp/</li><li>/foods/add/</li><li>/foods/:id/update/</li><li>/foods/:id/delete/</li></ul> |
| pomodoros_pomodoro                                                                        | The table manages users' Pomodoro.                                                                                                                                                                                                                                                                                                                                                                  | <ul><li>/pomodoros/</li><li>/pomodoros/add/</li><li>/pomodoros/detail/:id/</li><li>/pomodoros/pomodoro-datestamp-collection/:datestamp/</li></ul>                  |
| steps_steps                                                                               | The table manages users' steps.                                                                                                                                                                                                                                                                                                                                                                     | <ul><li>/steps/</li><li>/steps/add/</li><li>/steps/:id/update/</li><li>/steps/:id/delete/</li></ul>                                                                |
| water_intake_waterintake                                                                  | The table manages users' water intake.                                                                                                                                                                                                                                                                                                                                                              | <ul><li>/water-intake/</li><li>/water-intake/add/</li><li>/water-intake/:id/update/</li><li>/water-intake/:id/delete/</li></ul>                                    |
| weights_weight                                                                            | The table manages users' weight.                                                                                                                                                                                                                                                                                                                                                                    | <ul><li>/weight/</li><li>/weight/add/</li><li>/weight/:id/update/</li><li>/weight/:id/delete/</li></ul>                                                            |
| xps_xp                                                                                    | The table manages users' experience points (xps).                                                                                                                                                                                                                                                                                                                                                   | /xps/                                                                                                                                                              |
| aboutus_contactus                                                                         | The table consists of the users' messages sent to the admin.                                                                                                                                                                                                                                                                                                                                        | /about/contact-us/                                                                                                                                                 | 
| history_history                                                                           | The table provides a summary of actions taken by the user. The activities include: CREATE a resource, UPDATE the resource, DELETE the resource, and REWARD by the system.                                                                                                                                                                                                                           | /history/                                                                                                                                                          |
| accounts_usersignlog                                                                      | The table logs users' login and logout activity. **
Note:** only the Gesund App admin has access to view for analysis purposes.                                                                                                                                                                                                                                                                      | NA                                                                                                                                                                 |

<p align="center">
<i>Table:todo Tables of the Gesund App database in logical order.</i>
</p>

### Table details

This table details section provides facts about the table and its associated fields. One way to see the detail is
through the following command:

```shell
mysql > describe <table_name>;
```

#### Table: aboutus_contactus

For instance, describe aboutus_contactus table:

```mysql
mysql > describe aboutus_contactus;

+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int          | NO   | PRI | NULL    | auto_increment |
| datestamp | date         | NO   |     | NULL    |                |
| subject   | varchar(100) | NO   |     | NULL    |                |
| message   | longtext     | NO   |     | NULL    |                |
| author_id | int          | NO   | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
```

#### Table: accounts_usersignlog

```mysql
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int         | NO   | PRI | NULL    | auto_increment |
| datestamp  | datetime(6) | NO   |     | NULL    |                |
| log_status | varchar(10) | NO   |     | NULL    |                |
| author_id  | int         | NO   | MUL | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
```

#### Table: auth_group

```mysql
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(150) | NO   | UNI | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
```

#### Table: auth_group_permissions

```mysql
+---------------+--------+------+-----+---------+----------------+
| Field         | Type   | Null | Key | Default | Extra          |
+---------------+--------+------+-----+---------+----------------+
| id            | bigint | NO   | PRI | NULL    | auto_increment |
| group_id      | int    | NO   | MUL | NULL    |                |
| permission_id | int    | NO   | MUL | NULL    |                |
+---------------+--------+------+-----+---------+----------------+
```

#### Table: auth_user

```mysql
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int          | NO   | PRI | NULL    | auto_increment |
| password     | varchar(128) | NO   |     | NULL    |                |
| last_login   | datetime(6)  | YES  |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| username     | varchar(150) | NO   | UNI | NULL    |                |
| first_name   | varchar(150) | NO   |     | NULL    |                |
| last_name    | varchar(150) | NO   |     | NULL    |                |
| email        | varchar(254) | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| date_joined  | datetime(6)  | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```

#### Table: auth_user_groups

```mysql
+----------+--------+------+-----+---------+----------------+
| Field    | Type   | Null | Key | Default | Extra          |
+----------+--------+------+-----+---------+----------------+
| id       | bigint | NO   | PRI | NULL    | auto_increment |
| user_id  | int    | NO   | MUL | NULL    |                |
| group_id | int    | NO   | MUL | NULL    |                |
+----------+--------+------+-----+---------+----------------+
```

#### Table: auth_user_user_permissions

```mysql
+---------------+--------+------+-----+---------+----------------+
| Field         | Type   | Null | Key | Default | Extra          |
+---------------+--------+------+-----+---------+----------------+
| id            | bigint | NO   | PRI | NULL    | auto_increment |
| user_id       | int    | NO   | MUL | NULL    |                |
| permission_id | int    | NO   | MUL | NULL    |                |
+---------------+--------+------+-----+---------+----------------+
```

#### Table: calories_caloriecategory

```mysql
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| category | varchar(100) | NO   |     | NULL    |                |
| status   | tinyint(1)   | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

#### Table: calories_caloriefooddetail

```mysql
+-------------+------------+------+-----+---------+----------------+
| Field       | Type       | Null | Key | Default | Extra          |
+-------------+------------+------+-----+---------+----------------+
| id          | int        | NO   | PRI | NULL    | auto_increment |
| food        | longtext   | NO   |     | NULL    |                |
| description | longtext   | NO   |     | NULL    |                |
| calories    | double     | NO   |     | NULL    |                |
| protein     | double     | NO   |     | NULL    |                |
| fat         | double     | NO   |     | NULL    |                |
| carb        | double     | NO   |     | NULL    |                |
| sugar       | double     | NO   |     | NULL    |                |
| fiber       | double     | NO   |     | NULL    |                |
| status      | tinyint(1) | NO   |     | NULL    |                |
| category_id | int        | NO   | MUL | NULL    |                |
+-------------+------------+------+-----+---------+----------------+
```

#### Table: calories_calorieintake

```mysql
+--------------------+----------+------+-----+---------+----------------+
| Field              | Type     | Null | Key | Default | Extra          |
+--------------------+----------+------+-----+---------+----------------+
| id                 | int      | NO   | PRI | NULL    | auto_increment |
| datestamp          | date     | NO   |     | NULL    |                |
| consume            | double   | NO   |     | NULL    |                |
| author_id          | int      | NO   | MUL | NULL    |                |
| food               | longtext | NO   |     | NULL    |                |
| calories           | double   | NO   |     | NULL    |                |
| carb               | double   | NO   |     | NULL    |                |
| description        | longtext | YES  |     | NULL    |                |
| fat                | double   | NO   |     | NULL    |                |
| fiber              | double   | NO   |     | NULL    |                |
| food_detail_ref_id | int      | NO   | MUL | NULL    |                |
| protein            | double   | NO   |     | NULL    |                |
| sugar              | double   | NO   |     | NULL    |                |
+--------------------+----------+------+-----+---------+----------------+
```

#### Table: challenges_challenge

```mysql
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int         | NO   | PRI | NULL    | auto_increment |
| start_date | datetime(6) | NO   |     | NULL    |                |
| challenge  | varchar(15) | NO   |     | NULL    |                |
| status     | tinyint(1)  | NO   |     | NULL    |                |
| author_id  | int         | NO   | MUL | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
```

#### Table: django_admin_log

```mysql
+-----------------+-------------------+------+-----+---------+----------------+
| Field           | Type              | Null | Key | Default | Extra          |
+-----------------+-------------------+------+-----+---------+----------------+
| id              | int               | NO   | PRI | NULL    | auto_increment |
| action_time     | datetime(6)       | NO   |     | NULL    |                |
| object_id       | longtext          | YES  |     | NULL    |                |
| object_repr     | varchar(200)      | NO   |     | NULL    |                |
| action_flag     | smallint unsigned | NO   |     | NULL    |                |
| change_message  | longtext          | NO   |     | NULL    |                |
| content_type_id | int               | YES  | MUL | NULL    |                |
| user_id         | int               | NO   | MUL | NULL    |                |
+-----------------+-------------------+------+-----+---------+----------------+
```

#### Table: django_content_type

```mysql
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int          | NO   | PRI | NULL    | auto_increment |
| app_label | varchar(100) | NO   | MUL | NULL    |                |
| model     | varchar(100) | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
```

#### Table: django_migrations

```mysql
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | bigint       | NO   | PRI | NULL    | auto_increment |
| app     | varchar(255) | NO   |     | NULL    |                |
| name    | varchar(255) | NO   |     | NULL    |                |
| applied | datetime(6)  | NO   |     | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
```

#### Table: django_session

```mysql
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| session_key  | varchar(40) | NO   | PRI | NULL    |       |
| session_data | longtext    | NO   |     | NULL    |       |
| expire_date  | datetime(6) | NO   | MUL | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
```

#### Table: goals_goals

```mysql
+-----------+--------+------+-----+---------+----------------+
| Field     | Type   | Null | Key | Default | Extra          |
+-----------+--------+------+-----+---------+----------------+
| id        | int    | NO   | PRI | NULL    | auto_increment |
| water     | double | NO   |     | NULL    |                |
| calories  | double | NO   |     | NULL    |                |
| steps     | double | NO   |     | NULL    |                |
| author_id | int    | NO   | MUL | NULL    |                |
| weight    | double | NO   |     | NULL    |                |
| pomodoro  | double | NO   |     | NULL    |                |
+-----------+--------+------+-----+---------+----------------+
```

#### Table: history_history

```mysql
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | int         | NO   | PRI | NULL    | auto_increment |
| datestamp   | datetime(6) | NO   |     | NULL    |                |
| app         | varchar(20) | NO   |     | NULL    |                |
| action      | varchar(10) | NO   |     | NULL    |                |
| description | longtext    | YES  |     | NULL    |                |
| author_id   | int         | NO   | MUL | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
```

#### Table: pomodoros_pomodoro

```mysql
+-------------+----------+------+-----+---------+----------------+
| Field       | Type     | Null | Key | Default | Extra          |
+-------------+----------+------+-----+---------+----------------+
| id          | int      | NO   | PRI | NULL    | auto_increment |
| author_id   | int      | NO   | MUL | NULL    |                |
| remarks     | longtext | YES  |     | NULL    |                |
| long_break  | int      | YES  |     | NULL    |                |
| pomodoro    | int      | YES  |     | NULL    |                |
| short_break | int      | YES  |     | NULL    |                |
| datestamp   | date     | NO   |     | NULL    |                |
| timestamp   | time(6)  | NO   |     | NULL    |                |
+-------------+----------+------+-----+---------+----------------+
```

#### Table: profiles_profile

```mysql
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int          | NO   | PRI | NULL    | auto_increment |
| dob       | date         | YES  |     | NULL    |                |
| gender    | varchar(1)   | YES  |     | NULL    |                |
| height    | double       | YES  |     | NULL    |                |
| author_id | int          | NO   | MUL | NULL    |                |
| name      | varchar(200) | YES  |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
```

#### Table: steps_steps

```mysql
+------------+------+------+-----+---------+----------------+
| Field      | Type | Null | Key | Default | Extra          |
+------------+------+------+-----+---------+----------------+
| id         | int  | NO   | PRI | NULL    | auto_increment |
| datestamp  | date | NO   |     | NULL    |                |
| step_count | int  | NO   |     | NULL    |                |
| author_id  | int  | NO   | MUL | NULL    |                |
+------------+------+------+-----+---------+----------------+
```

#### Table: water_intake_waterintake

```mysql
+----------------+--------+------+-----+---------+----------------+
| Field          | Type   | Null | Key | Default | Extra          |
+----------------+--------+------+-----+---------+----------------+
| id             | int    | NO   | PRI | NULL    | auto_increment |
| datestamp      | date   | NO   |     | NULL    |                |
| drink_progress | double | NO   |     | NULL    |                |
| author_id      | int    | NO   | MUL | NULL    |                |
+----------------+--------+------+-----+---------+----------------+
```

#### Table: weights_weight

```mysql
+-----------+--------+------+-----+---------+----------------+
| Field     | Type   | Null | Key | Default | Extra          |
+-----------+--------+------+-----+---------+----------------+
| id        | int    | NO   | PRI | NULL    | auto_increment |
| datestamp | date   | NO   |     | NULL    |                |
| weight    | double | NO   |     | NULL    |                |
| author_id | int    | NO   | MUL | NULL    |                |
+-----------+--------+------+-----+---------+----------------+
```

#### Table: xps_xp

```mysql
+----------------+----------+------+-----+---------+----------------+
| Field          | Type     | Null | Key | Default | Extra          |
+----------------+----------+------+-----+---------+----------------+
| id             | int      | NO   | PRI | NULL    | auto_increment |
| xp             | int      | YES  |     | NULL    |                |
| author_id      | int      | NO   | MUL | NULL    |                |
| datestamp      | date     | NO   |     | NULL    |                |
| referer_app_id | longtext | YES  |     | NULL    |                |
+----------------+----------+------+-----+---------+----------------+
```

### Dummy data setup

Dummy database with records are provided to work with the App. In `.env` update:

```shell
...
DB_HOST='local'
DB_DATABASE='gesund_dummy_database'
...
```

And, import the provided `gesund_dummy_database.sql` to MySQL server.

todo: image

Django admin details for [http://localhost:8000/admin](http://localhost:8000/admin):

```shell
URL: http://localhost:8000/admin
username: djangoadmin
Password: dj4n604dm1n
```

## REST API

todo: what is rest api?
todo: where it has been used?

Basic Auth is used as Authorization mechanism.

```
username: 'admin'
password: '*****'
```

### Steps

#### Get all steps

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/steps/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' steps.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/steps/'
```

### Get steps by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/steps/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's steps by steps id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/steps/1/'
```

#### Add steps

**HTTP Method:** `POST`

**Endpoint:** `http://localhost:8000/api/v1/steps/`

**Path variables:** `id`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "step_count": 123456,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint records a specific user's steps.

**cURL example request:**

```shell
curl --location --request POST 'http://localhost:8000/api/v1/steps/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "step_count": 123456,
    "author": 1
}'
```

#### Update steps

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/steps/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "step_count": 123,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's steps by steps id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/steps/2/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "step_count": 123,
    "author": 1
}'
```

#### Delete steps

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/steps/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's steps by steps id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/steps/2/'
```

For complete REST API Endpoints, refer to [rest_api_complete.md](./docs/rest_api_complete.md)

### Postman

Postman collection is provided on [resources/gesund_postman_collection.json](./resources/gesund_postman_collection.json)
. You can download the software from [https://www.postman.com/downloads/](https://www.postman.com/downloads/).

Once you have installed Postman, you must import this `gesund_postman_collection.json` into Postman.

#### Postman runner

The collection runner allows developers to run the Gesund App REST API requests in a collection. Moreover, it logs the
request's test result. The detailed article can be found on
the [official website](https://learning.postman.com/docs/running-collections/intro-to-collection-runs/).

#### Running Newman[^1]

Newman is a command-line collection runner for Postman, which helps developers to run requests and tests directly from
CLI.

```shell
$ npm install -g newman
```

```shell
$ newman run resources/gesund_postman_collection.json
```

## Tests

"Code without tests is broken by design." - Jacob Kaplan-Moss

What is automated test?

To run the all the test cases in the Gesund app:

```shell
(venv) gesund_project/gesund $ python manage.py test
```

result:

```shell
Found 29 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
0
.............................
----------------------------------------------------------------------
Ran 29 tests in 15.098s

OK
Destroying test database for alias 'default'...
```

To run specific app test, for an example `steps` app:

```shell
(venv) gesund_project/gesund $ python manage.py test steps
```

result:

```shell
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 1.534s

OK
Destroying test database for alias 'default'...
```


## End-user documentation

This documentation is intended for end-users. It explains the most straightforward way the user can start using the
Gesund App.

**Login page**

<p style="text-align:center;">
<img src="./resources/images/login.png" alt="login page" height="500px" style="border:1px solid #cecece">
</p>

- When the Gesund App starts, it will redirect to the login page.
- If the user is new to the app, he/she can sign up by clicking `Sign up now!`.
- After successful login, the user is redirected to the `Dashboard`.

**Sign up**

- When the user successfully signs up for the Gesund app, they will receive an automatic email from the system.

<p style="text-align:center;">
<img src="./resources/images/sign_up_successful_email.png" alt="sign up successful" height="500px" style="border:1px solid #cecece">
</p>

Now, to get started with the app, the user must follow two steps below:

1. The user must update their goals (i.e., calories, steps, water, and weight).

2. And their profile.

**Quick start guide**

The [quick start guide (.pdf)](./docs/quick_start_guide.pdf) gives a basic guidelines on how to use the
app.

<p style="text-align:center;">
<img src="./resources/images/quick_start_guide.png" alt="quick start guide" height="500px" 
style="border:1px solid #cecece">
</p>

**Instruction on using a `steps` `feature`**

Most "features" on the app are represented in four forms, i.e.,  **Creating**, **Reading**, **Updating**,
or **Deleting** a resource.

- By clicking number **1**, the user can add their steps.
- Number **2** shows randomized "tips/hints".
- **3**, where the user records their steps by clicking `Save changes`, and the user is redirected to
  the [ListView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/) page (**4**).
- **5** - The user gets successful notification and they are [rewarded by the system](#).
- **6** - To update existing steps record.
- **7** - To delete existing steps record.

<p style="text-align:center;">
<img src="./resources/images/steps_user_flow.svg" alt="quick start guide" height="100%">
</p>



## Feedback

If you have any feedback, please reach out to the author at info@amaharjan.online

## Contributing

Contributions are always welcome! please contact the author at info@amaharjan.online

### Disclaimer

<p>
    The information provided by the author(s) on <a href="https://github.com/asis2016/gesund">https://github.com/asis2016/gesund</a> the APP
    is for general informational purposes only. All information on the Web App is provided in good faith. However, we
    make no representation or warranty of any kind, express or implied, regarding the accuracy,
    adequacy, validity, reliability, availability, or completeness of any information on the Web App.
</p>
<p>
    No content on this Web App, regardless of date, regardless of "features", should ever be used as a
    replacement for direct
    medical
    advice from your doctor or other qualified clinicians.
</p>
<p>
    UNDER NO CIRCUMSTANCE SHALL WE HAVE ANY LIABILITY TO YOU FOR ANY LOSS OR DAMAGE OF ANY KIND INCURRED
    AS
    A RESULT OF THE USE OF THE WEB APP OR RELIANCE ON ANY INFORMATION PROVIDED ON THE WEB APP.
</p>
<p>
    YOUR USE OF THE WEB APP AND YOUR RELIANCE ON ANY INFORMATION ON THE WEB APP IS SOLELY AT YOUR OWN
    RISK.
</p>

## License

This project is licensed under the [MIT license](./LICENSE).

## Privacy Policy

General Data Protection Regulation (GDPR) was applied during the APP pilot test period.








# References

- [CLI with Postman Newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)
- [User flow](https://xd.adobe.com/ideas/process/user-research/user-journey-vs-user-flow/)

## Images, vectors, or icons

- [https://undraw.co/](https://undraw.co/)
- <a href="https://www.flaticon.com/free-icons/fruit" title="fruit icons">Fruit icons created by Freepik - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/bottle" title="bottle icons">Bottle icons created by Vitaly Gorbachev -
  Flaticon</a>
- <a href='https://www.freepik.com/vectors/dairy-free'>Dairy free vector created by macrovector - www.freepik.com</a>
- <a href='https://www.freepik.com/vectors/vegan'>Vegan vector created by studiogstock - www.freepik.com</a>
- <a href="https://www.vecteezy.com/free-vector/salt">Salt Vectors by Vecteezy</a>
- <a href='https://www.freepik.com/vectors/tiny'>Tiny vector created by pch.vector - www.freepik.com</a>
- <a href='https://www.freepik.com/vectors/drink-water'>Drink water vector created by pch.vector - www.freepik.com</a>
- <a href='https://www.freepik.com/vectors/people-walking'>People walking vector created by
  storyset, www.freepik.com</a>
- <a href="https://www.freepik.com/vectors/trekking">Trekking vector created by pch.vector - www.freepik.com</a>
- Illustration by <a href="https://icons8.com/illustrations/author/292791">Anna Golde</a>
  from <a href="https://icons8.com/illustrations">Ouch!</a>
- <a href="https://www.flaticon.com/free-icons/cigarette" title="cigarette icons">Cigarette icons created by Freepik -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/beer" title="beer icons">Beer icons created by Freepik - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/sugar-cube" title="sugar cube icons">Sugar cube icons created by Freepik,
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/burger" title="burger icons">Burger icons created by Freepik -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/chocolate" title="chocolate icons">Chocolate icons created by Freepik -
  Flaticon</a>
- Illustration by <a href="https://icons8.com/illustrations/author/Go8GMpKPAq1W">Polina Makeeva</a>
  from <a href="https://icons8.com/illustrations">Ouch!</a>
- <a href="https://www.flaticon.com/de/kostenlose-icons/profil" title="profil Icons">Profil Icons erstellt von Freepik -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/tomato" title="tomato icons">Tomato icons created by Pixel perfect -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/calories" title="calories icons">Calories icons created by Freepik -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/walking" title="walking icons">Walking icons created by Freepik,
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/timer" title="timer icons">Timer icons created by Freepik - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/water" title="water icons">Water icons created by Freepik - Flaticon</a>

