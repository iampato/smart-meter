# Smart-Meter
A python project that aims to a make smart meter server that communicates on MQTT and uses a MongoDB

## How to run
In the config directory inside the root folder of the project edit the `config.ini` file to reflect correct credentials
then run `make get` to install the dependencies and `make run` with the terminal dir points to the root dir of the project

## Technology stack
Techonology stack for smart meter includes:
    * Python 3.8.5
    * MQTT - Communication channel
    * MongoDB - Database layer
    * Sentry - For error reporting

## Tests
There is work to-do in this sector

## Project structure
```
.
├── config
│   ├── config.ini
│   ├── connect.py
│   ├── connect_test.py
│   ├── __init__.py
│   └── __pycache__
│       ├── connect.cpython-38.pyc
│       ├── connect_test.cpython-38.pyc
│       └── __init__.cpython-38.pyc
├── entities
│   └── device_entities.py
├── LICENSE
├── main.py
├── MakeFile
├── models
│   ├── device.py
│   └── __init__.py
├── README.md
├── requirements.txt
├── utils
│   ├── error_handler.py
│   ├── __init__.py
│   └── __pycache__
│       ├── error_handler.cpython-38.pyc
│       └── __init__.cpython-38.pyc
└── v1
    └── device
        ├── handler
        │   └── mqtt_handler.py
        ├── repository
        │   └── device_repo.py
        └── service
            └── device_service.py

```

## Licences

## Contributions
