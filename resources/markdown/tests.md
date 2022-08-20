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

