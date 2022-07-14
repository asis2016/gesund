# Introduction

This project is carried out as the master thesis at University of Koblenz-Landau.

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

| PK                         | Endpoints                                               | Status |
|:---------------------------|:--------------------------------------------------------|:-------|
| **Activity**               |                                                         ||
| GET                        | http://localhost:8000/api/v1/activities/                ||
| POST                       | http://localhost:8000/api/v1/activity/create/           ||
| PUT                        | http://localhost:8000/api/v1/activity/:id/update/       ||
| DELETE                     | http://localhost:8000/api/v1/activity/:id/delete/       ||
|||
| **Calorie**                |                                                         ||
| GET                        | http://localhost:8000/api/v1/calories-intake/           ||
| POST                       | http://localhost:8000/api/v1/calorie-intake/create/     ||
| PUT                        | http://localhost:8000/api/v1/calorie-intake/:id/update/ ||
| DELETE                     | http://localhost:8000/api/v1/calorie-intake/:id/delete/ ||
| _**Calorie Category**_     |                                                         ||
| GET                        | http://localhost:8000/api/v1/food-categories/           ||
| GET                        | http://localhost:8000/api/v1/food-category/:id/         ||
| **_Calorie Food details_** |                                                         ||
| GET                        | http://localhost:8000/api/v1/food-calories/             ||
| GET                        | http://localhost:8000/api/v1/food-calorie/:id/          ||
|||
| **Challenge**              |                                                         ||
| GET                        | http://localhost:8000/api/v1/challenges/                ||
| GET                        | http://localhost:8000/api/v1/challenge/:id/             ||
| POST                       | http://localhost:8000/api/v1/challenge/create/          ||
| PUT                        | http://localhost:8000/api/v1/challenge/:id/update/      ||
| DELETE                     | http://localhost:8000/api/v1/challenge/:id/delete/      ||
|||
| **Pomodoro**               |                                                         ||
| GET                        | http://localhost:8000/api/v1/pomodoros/                 ||
| GET                        | http://localhost:8000/api/v1/pomodoro/:id/              ||
| POST                       | http://localhost:8000/api/v1/pomodoro/create/           ||
| PUT                        | http://localhost:8000/api/v1/pomodoro/:id/update/       ||
| DELETE                     | http://localhost:8000/api/v1/pomodoro/:id/delete/       ||
|||
| **Profile**                |                                                         ||
| GET                        | http://localhost:8000/api/v1/profile/:id/               ||
| PUT                        | http://localhost:8000/api/v1/activity/:id/update/       ||
|||
| **Steps**                  |                                                         ||
| GET                        | http://localhost:8000/api/v1/steps/                     ||
| GET                        | http://localhost:8000/api/v1/steps/:id/                 ||
| POST                       | http://localhost:8000/api/v1/steps/create/              ||
| PUT                        | http://localhost:8000/api/v1/steps/:id/update/          ||
| DELETE                     | http://localhost:8000/api/v1/steps/:id/delete/          ||
||||
| **Water intake**           |                                                         ||
| GET                        | http://localhost:8000/api/v1/water-intake/              ||
| GET                        | http://localhost:8000/api/v1/water-intake/:id/          ||
| POST                       | http://localhost:8000/api/v1/water-intake/create/       ||
| PUT                        | http://localhost:8000/api/v1/water-intake/:id/update/   ||
| DELETE                     | http://localhost:8000/api/v1/water-intake/:id/delete/   ||
||||
| **Weight**                 |                                                         ||
| GET                        | http://localhost:8000/api/v1/weights/                   ||
| GET                        | http://localhost:8000/api/v1/weight/:id/                ||
| POST                       | http://localhost:8000/api/v1/weight/create/             ||
| PUT                        | http://localhost:8000/api/v1/weight/:id/update/         ||
| DELETE                     | http://localhost:8000/api/v1/weight/:id/delete/         ||

## REST API Postman collections

### How to?




# References

## FontAwesome 5.0

- Save: `<i class="fa-solid fa-floppy-disk"></i>`
- Update:
- Delete:  `<i class="fa-solid fa-trash-can"></i>`
- List:
- Go back: `<i class="fa-solid fa-angle-left"></i>`

## Icons

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

