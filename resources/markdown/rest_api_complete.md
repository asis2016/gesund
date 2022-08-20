## About us

### Get all contact us

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/contact-us/`

**Authorization:** `Basic Auth`

**Description:** The endpoint retrieves all contact us records that users sent.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/contact-us/'
```

## Accounts

### Get all user sign log

**HTTP Method:** `GET`

**Endpoint:** `http://localhost:8000/api/v1/user-sign-log/`

**Authorization:** `Basic Auth`

**Description:** The system retrieves all users' login behavior, i.e., signs in or signs off status.

**cURL example request:**

```shell
curl --location --request GET 'http://localhost:8000/api/v1/user-sign-log/'
```

## Food

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