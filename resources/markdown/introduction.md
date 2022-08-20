
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

