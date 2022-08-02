## Database

Following represents ER diagram from the project.

![Database diagram](./resources/images/erd.svg)

### References

### Dummy database

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

