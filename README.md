# Table of contents

[Introduction]()

- [Project organization](#)
- [Tech stack](#)
- [Installation](#)
    - [GIT clone](#)
    - [Python VENV](#)
    - [MySQL Server](#)
- [Tests](#tests)
- [End-user documentation](#end-user-documentation)

## Introduction

This project is carried out as the master thesis at University of Koblenz-Landau.

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

**MySQL database**

The Gesund App requires MySQL database. Hence, you should create:

1. MySQL Database: `gesund`
2. MySQL username: `your_username`
3. MySQL password: `your_password`

**Configure `.env` file**

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

## Database

Following represents ER diagram from the project.

![Database diagram](./resources/images/erd.svg)


## REST API

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

## UML use case diagram

![sitemap](./resources/images/uml_use_case_diagram.svg)

## Wireframes

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

Reference: https://xd.adobe.com/ideas/process/user-research/user-journey-vs-user-flow/
## Sitemap

<p>
A sitemap is a collection of pages on a website. In a simple form, it is a map of the website. Draw.io was used to
create the visual sitemap of the Gesund app.
</p>

![sitemap](./resources/images/sitemap.svg)

<p align="center">
    <i>Figure. Visual sitemap of the Gesund app (own representation).</i>
</p>

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

## License

[MIT](./LICENSE)

# References

[^1]: https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/

## FontAwesome 5.0

- Save: `<i class="fa-solid fa-floppy-disk"></i>`
- Update:
- Delete:  `<i class="fa-solid fa-trash-can"></i>`
- List:
- Go back: `<i class="fa-solid fa-angle-left"></i>`

## Icons

- <a href='https://www.freepik.com/vectors/dairy-free'>Dairy free vector created by macrovector - www.freepik.com</a>
- <a href='https://www.freepik.com/vectors/vegan'>Vegan vector created by studiogstock - www.freepik.com</a>
- <a href="https://www.vecteezy.com/free-vector/salt">Salt Vectors by Vecteezy</a>
- <a href='https://www.freepik.com/vectors/tiny'>Tiny vector created by pch.vector - www.freepik.com</a>
- <a href='https://www.freepik.com/vectors/drink-water'>Drink water vector created by pch.vector - www.freepik.com</a>
- <a href='https://www.freepik.com/vectors/people-walking'>People walking vector created by storyset
    - www.freepik.com</a>
- <a href="https://www.freepik.com/vectors/trekking">Trekking vector created by pch.vector - www.freepik.com</a>
- https://undraw.co/
- Illustration by <a href="https://icons8.com/illustrations/author/292791">Anna Golde</a>
  from <a href="https://icons8.com/illustrations">Ouch!</a>
- <a href="https://www.flaticon.com/free-icons/cigarette" title="cigarette icons">Cigarette icons created by Freepik -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/beer" title="beer icons">Beer icons created by Freepik - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/sugar-cube" title="sugar cube icons">Sugar cube icons created by Freepik
    - Flaticon</a>
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
- <a href="https://www.flaticon.com/free-icons/walking" title="walking icons">Walking icons created by Freepik -
  Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/timer" title="timer icons">Timer icons created by Freepik - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/water" title="water icons">Water icons created by Freepik - Flaticon</a>

