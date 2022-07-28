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

