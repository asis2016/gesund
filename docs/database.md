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
| accounts_usersignlog                                                                      | The table logs users' login and logout activity. **Note:** only the Gesund App admin has access to view for analysis purposes.                                                                                                                                                                                                                                                                      | NA                                                                                                                                                                 |

<p align="center">
<i>Table:todo Tables of the Gesund App database in logical order.</i>
</p>

### Table details

This table details section provides facts about the table and its associated fields. One way to see the detail is through the following command:

```shell
mysql > describe <table_name>;
```

For instance, describing xps_xp table:

```mysql
mysql > describe xps_xp;
+-----------+------+------+-----+---------+----------------+ 
| Field     | Type | Null | Key | Default | Extra          | 
+-----------+------+------+-----+---------+----------------+ 
| id        | int  | NO   | PRI | NULL    | auto_increment | 
| xp        | int  | YES  |     | NULL    |                | 
| author_id | int  | NO   | MUL | NULL    |                | 
| datestamp | date | NO   |     | NULL    |                | 
+-----------+------+------+-----+---------+----------------+ 
4 rows in set (0,00 sec)
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

