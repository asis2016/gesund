# Introduction

This project is carried out as the master thesis at University of Koblenz-Landau.

## Project organization

```
.
├── aboutus
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── signals.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views
...
├── accounts
├── api
├── calories
├── challenges
├── dashboard
├── exports
├── gesund_projekt
├── goals
├── history
├── leaderboards
├── manage.py
├── passenger_wsgi.py.bak
├── pomodoros
├── postpilottest
├── profiles
├── requirements.txt
├── static
├── staticfiles
├── steps
├── templates
├── tree
├── utils
├── venv
├── water_intake
├── weights
└── xps

```
## Installation

```shell
$ mkdir gesund_project
$ cd gesund_project
```

## Initial setup

```shell
$ mkdir gesund && cd gesund
$ pipenv install django==4.0.1 --python 3
$ pipenv shell

(gesund) $ python3 manage.py runserver
```

## Django REST framework

```shell
(gesund) $ pipenv install djangorestframework==3.13.1
```

### update `./gesund_projekt/settings.py`

```python
INSTALLED_APPS = [
    ...
    ###
    'rest_framework',
]
```

## Migration

```shell
(gesund) $ python3 manage.py showmigrations
(gesund) $ python3 manage.py makemigrations <app_name>
(gesund) $ python3 manage.py migrate
```

## Admin page

http://localhost:8000/admin

## Create superuser

```shell
(gesund) $ python3 manage.py createsuperuser
```

## Creating an app

### recipes app

```shell
(gesund) $ python3 manage.py startapp recipes
```

Update `INSTALLED_APPS` from `./gesund_projekt/settings.py`

```python
INSTALLED_APPS = [
    ...
    ###
    'rest_framework',

    ###
    'recipes.apps.RecipesConfig',
]
```

### recipes app models

```python
# recipes/models.py
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    calorie = models.IntegerField()
    cook_level = models.CharField(max_length=15)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title} - {self.calorie} Cal - {self.cook_level}'
```

Make migrations.

Update `admin.py`

```python
from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)
```

Check if http://127.0.0.1:8000/admin/recipes/ is working.

## URLs setup

1. Update `gesund_projekt/urls.py`

```python
urlpatterns = [
    ...,
    path('api/v1/', include('recipes.urls')),
]
```

2. Create `recipes/urls.py`

```python
from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    path('<uuid:id>/', RecipeDetail.as_view()),
    path('', RecipeList.as_view())
]
```

3. Add `recipes/serializers.py`

```python
from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Recipe
```

4. Update `recipes/views.py`

```python
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
```

Restart the server and browse > http://127.0.0.1:8000/api/v1/ and http://127.0.0.1:8000/api/v1/uuid

## settings.py

### `.env` file

```
API_URL='http://192.168.2.110:8000/api/v1/'

# ENVIRONMENT='prod'
DB_DATABASE=''
DB_USER=''
DB_PASS=''
ALLOWED_HOSTS_ENV=''

# EMAIL
EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
DEFAULT_FROM_EMAIL=''
```

# Database

Following represents database models from the project.

## activity

| PK   | id (1,1)         |
|:-----|:-----------------|
|      | datestamp (Date) |
|      | todo             |
| FK   | author           |

## calorie

### CalorieCategory

| PK   | id (1,1)            |
|:-----|:--------------------|
|      | category (Char)     |
|      | status (Boolean)    |
| FK   | author              |

### CalorieFoodDetail

| PK   | id (1,1)            |
|:-----|:--------------------|
|      | food (Char)         |
|      | description (Text)  |
|      | calories (Float)    |
|      | protein (Float)     |
|      | fat (Float)         |
|      | carb (Float)        |
|      | sugar (Float)       |
|      | fiber (Float)       |
|      | status (Boolean)    |
| FK   | CalorieCategory     |

### CalorieIntake

| PK   | id (1,1)                 |
|:-----|:-------------------------|
|      | datestamp (Date)         |
| FK   | food (CalorieFoodDetail) |
| FK   | author                   |

## challenge

| PK   | id (1,1)               |
|:-----|:-----------------------|
|      | start_date (DateTime)  |
|      | challenge (Char)       |
|      | status (Text)          |
| FK   | author                 |

## pomodoro

| PK   | id (1,1)                 |
|:-----|:-------------------------|
|      | datestamp (Date)         |
|      | pomodoro_minutes (Float) |
|      | break_minutes (Float)    |
|      | remarks (Text)           |
| FK   | author                   |

## profile

| PK   | id (1,1)                        |
|:-----|:--------------------------------|
|      | dob (Date)                      |
|      | city (Char)                     |
|      | gender (Char)                   |
|      | height (Float)                  |
|      | daily_calorie_goal (Float)      |
|      | daily_step_goal (Float)         |
|      | daily_water_intake_goal (Float) |
| FK   | author                          |

## steps

| PK   | id (1,1)             |
|:-----|:---------------------|
|      | datestamp (Date)     |
|      | step_count (Integer) |
| FK   | author               |

## waterintake

| PK   | id (1,1)               |
|:-----|:-----------------------|
|      | datestamp (Date)       |
|      | drink_progress (Float) |
| FK   | author                 |

## weight

| PK   | id (1,1)         |
|:-----|:-----------------|
|      | datestamp (Date) |
|      | weight (Float)   |
| FK   | author           |

## Database diagram

![Database diagram](screenshots/database-diagram.png)

# REST API

Basic Auth is used as Authorization mechanism.

```
username: 'admin'
password: '*****'
```

## about_us

### Get all contact us

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/contact-us/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all contact us records that users sent.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/contact-us/'
```

## accounts

### Get all user sign log

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/user-sign-log/`

**Authorization:** `Basic Auth`

**Description:** The system retrieves all users' login behavior, i.e., signs in or signs off status.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/user-sign-log/'
```

## food

### Get all food categories

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/food-categories/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all food categories.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/food-categories/'
```

### Get food category by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/food-category/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves food category by id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/food-category/2/'
```

### Get all food calories

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/food-calories`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all food calories information.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/food-calories'
```

### Get food calories information by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/food-calories/:id`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** Retrieves food calories information by id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/food-calories/1000'
```

### Get food intake calories

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/calories-intake/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' food intake.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/calories-intake/'
```

### Get food intake calories by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/calories-intake/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's food intake by food intake id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/calories-intake/1/'
```

### Add food intake

**HTTP Method:** `POST`

**Endpoint:** `http://localhost:8000/api/v1/calories-intake/`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "food": "Chicken",
  "consume": 250,
  "description": "chicken meat cooked.",
  "calories": 1234,
  "protein": 123,
  "fat": 10,
  "carb": 10,
  "sugar": 0.1,
  "fiber": 0.1,
  "food_detail_ref": null,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint records a specific user's food intake.

**cURL example request:**

```shell
curl --location --request POST 'http://localhost:8000/api/v1/calories-intake/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "food": "Chicken",
    "consume": 250,
    "description": "chicken meat cooked.",
    "calories": 1234,
    "protein": 123,
    "fat": 10,
    "carb": 10,
    "sugar": 0.1,
    "fiber": 0.1,
    "food_detail_ref": null,
    "author": 1
}'
```

### Update food intake

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/calories-intake/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "food": "Chicken",
  "consume": 100,
  "description": "chicken meat cooked.",
  "calories": 1,
  "protein": 1,
  "fat": 1,
  "carb": 1,
  "sugar": 0.1,
  "fiber": 0.1,
  "food_detail_ref": null,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's food intake by food intake id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/calories-intake/1/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "food": "Chicken",
    "consume": 100,
    "description": "chicken meat cooked.",
    "calories": 1,
    "protein": 1,
    "fat": 1,
    "carb": 1,
    "sugar": 0.1,
    "fiber": 0.1,
    "food_detail_ref": null,
    "author": 1
}'
```

### Delete food intake

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/calories-intake/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's food intake by food intake id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/calories-intake/1/'
```

## goals

### Get all goals

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/goals/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' goals.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/goals/'
```

### Get goals by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/goals/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's goals by goals id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/goals/1/'
```

### Update goals by id

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/goals/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "calories": 1234,
  "steps": 1234,
  "water": 1.2,
  "weight": 67,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's goals by goals id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/goals/1/' \
--data-raw '{
    "calories": 1234,
    "steps": 1234,
    "water": 1.2,
    "weight": 67,
    "author": 1
}'
```

## history

### Get all history

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/history/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' history.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/history/'
```

### Get history by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/history/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's history by history id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/history/1/'
```

## pomodoro

### Get all pomodoro

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/pomodoro/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' pomodoro.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/pomodoro/'
```

### Get pomodoro by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/pomodoro/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's pomodoro by pomodoro id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/pomodoro/1/'
```

### Add pomodoro

**HTTP Method:** `POST`

**Endpoint:** `http://localhost:8000/api/v1/pomodoro/`

**Path variables:** `id`

**Body** raw:

```json
 {
  "datestamp": "2022-06-16",
  "pomodoro": 100,
  "short_break": 0,
  "long_break": 0,
  "remarks": "new pomodoro",
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint records a specific user's pomodoro.

**cURL example request:**

```shell
curl --location --request POST 'http://localhost:8000/api/v1/pomodoro/' \
--data-raw '    {
        "datestamp": "2022-06-16",
        "pomodoro": 100,
        "short_break": 0,
        "long_break": 0,
        "remarks": "new pomodoro",
        "author": 1
    }'
```

### Update pomodoro

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/pomodoro/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "datestamp": "2022-06-16",
  "pomodoro": 1000,
  "short_break": 10,
  "long_break": 10,
  "remarks": "new pomodoro, not that new.",
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's pomodoro by pomodoro id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/pomodoro/1/' \
--data-raw '    {
        "datestamp": "2022-06-16",
        "pomodoro": 1000,
        "short_break": 10,
        "long_break": 10,
        "remarks": "new pomodoro, not that new.",
        "author": 1
    }'
```

### Delete pomodoro

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/pomodoro/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's pomodoro by pomodoro id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/pomodoro/1/'
```

## profile

### Get all profiles

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/profile/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' profile.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/profile/'
```

### Get profile by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/profile/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's profile by profile id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/profile/2/'
```

### Update profile

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/profile/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "name": "John Doe",
  "dob": "2000-01-01",
  "gender": "M",
  "height": 175,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's profile by profile id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/profile/1/' \
--data-raw '{
    "name": "John Doe",
    "dob": "2000-01-01",
    "gender": "M",
    "height": 175,
    "author": 1
}'
```

## steps

### Get all steps

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

### Add steps

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

### Update steps

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

### Delete steps

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/steps/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's steps by steps id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/steps/2/'
```

## water_intake

### Get all water intake

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/water-intake/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' water intake.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/water-intake/'
```

### Get water intake by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/water-intake/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's water intake by water intake id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/water-intake/1/'
```

### Add water intake

**HTTP Method:** `POST`

**Endpoint:** `http://localhost:8000/api/v1/water-intake/`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "drink_progress": 1.5,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint records a specific user's water intake.

**cURL example request:**

```shell
curl --location --request POST 'http://localhost:8000/api/v1/water-intake/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "drink_progress": 1.5,
    "author": 1
}'
```

### Update water intake

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/water-intake/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "drink_progress": 1.5,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's water intake by water intake id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/water-intake/1/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "drink_progress": 1.5,
    "author": 1
}'
```

### Delete water intake

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/water-intake/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's water intake by water intake id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/water-intake/1/'
```

## weights

### Get weights

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/weights/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' weight.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/weights/'
```

### Get weight by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/weight/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves a specific user's weight by weight id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/weight/1/'
```

### Add weight

**HTTP Method:** `POST`

**Endpoint:** `http://localhost:8000/api/v1/weights/`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "weight": 70,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint records a specific user's weight.

**cURL example request:**

```shell
curl --location --request POST 'http://localhost:8000/api/v1/weights/' \
--data-raw '{
    "datestamp": "2012-12-12",
    "weight": 70,
    "author": 1
}'
```

### Update weight

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/weight/:id/`

**Path variables:** `id`

**Body** raw:

```json
{
  "datestamp": "2012-12-12",
  "weight": 60.0,
  "author": 1
}
```

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's weight by weight id.

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/weight/1/' \
--data-raw '
{
    "datestamp": "2012-12-12",
    "weight": 60.0,
    "author": 1
}'
```

### Delete weight

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/weight/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's weight by weight id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/weight/1/'
```

## xps

### Get all XPs

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/xps/`

**Path variables:** not required

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all users' XP.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/xps/'
```

### Get XP by id

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/xp/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves XP by XP id.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/xp/1/'
```

### Update XP

**HTTP Method:** `PUT`

**Endpoint:** `http://localhost:8000/api/v1/xps/:id`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint updates a specific user's XP by XP id.

**Body** raw:

```json
{
  "xp": 123456,
  "author": 2
}
```

**cURL example request:**

```shell
curl --location --request PUT 'http://localhost:8000/api/v1/xps/1' \
--data-raw '{
    "xp": 123456,
    "author": 2
}'
```

### Delete XP

**HTTP Method:** `DELETE`

**Endpoint:** `http://localhost:8000/api/v1/xp/:id/`

**Path variables:** `id`

**Authorization:** `Basic Auth`

**Description:** The endpoint deletes a specific user's XP by XP id.

**cURL example request:**

```shell
curl --location --request DELETE 'http://localhost:8000/api/v1/xp/1/'
```

## Postman

Postman collection is provided on [resources/gesund_postman_collection.json](./resources/gesund_postman_collection.json)
. You can download the software from [https://www.postman.com/downloads/](https://www.postman.com/downloads/).

Once you have installed Postman, you must import this `gesund_postman_collection.json` into Postman.

### Postman runner

The collection runner allows developers to run the Gesund App REST API requests in a collection. Moreover, it logs the
request's test result. The detailed article can be found on
the [official website](https://learning.postman.com/docs/running-collections/intro-to-collection-runs/).

### Running Newman[^1]

Newman is a command-line collection runner for Postman, which helps developers to run requests and tests directly from
CLI.

```shell
$ npm install -g newman
```

```shell
$ newman run resources/gesund_postman_collection.json
```

# User flow

User flow is used for describing the process of interaction between a user and the website. The following image presents
the 'flow' from the Gesund App entry point until the final action, i.e., Logging out.

![sitemap](./resources/user_flow.svg)

<p align="center">
Figure. User flow of the Gesund app (own representation).
</p>

## Example of the user flow

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

# Sitemap

<p>
A sitemap is a collection of pages on a website. In a simple form, it is a map of the website. Draw.io was used to
create the visual sitemap of the Gesund app.
</p>

![sitemap](./resources/sitemap.svg)

<p align="center">
    <i>Figure. Visual sitemap of the Gesund app (own representation).</i>
</p>

# End-user documentation

This documentation is intended for end-users. It explains the most straightforward way a user can start using the Gesund
App.

To set up a new account, please follow this video instruction.

todo:
www.youtube.com

Check this [quick start guide (.pdf)](./resources/quick_start_guide.pdf) that gives basic guidelines on how to user the
app.


## Feedback

If you have any feedback, please reach out to the author at info@amaharjan.online

## Contributing

Contributions are always welcome! please contact the author at info@amaharjan.online

## License

[MIT](https://choosealicense.com/licenses/mit/)

# References

[^1]: https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/

## FontAwesome 5.0

- Save: `<i class="fa-solid fa-floppy-disk"></i>`
- Update:
- Delete:  `<i class="fa-solid fa-trash-can"></i>`
- List:
- Go back: `<i class="fa-solid fa-angle-left"></i>`

## Icons

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

