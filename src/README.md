├── client_module
│   ├── __init__.py
│   ├── client.py # a core of the client module (also with logics)
│   ├── configs.py # local client configs
│   ├── dependencies.py # context instruments
│   ├── exceptions.py 
├── server_module
│   ├── __init__.py
│   ├── configs.py # local server's configs
│   ├── dependencies.py # context instruments 
│   ├── exceptions.py
│   ├── models.py # models description
│   ├── repository.py # CRUD manager, data proxy (from database/connector to standart)
│   ├── router.py # core/view with all endpoints
│   └── service.py # bisuness logic
├── configs.py # global configs
├── database.py # database connectors
├── exceptions.py # global exceptions
├── __init__.py
├── main.py # main file with app started (root of the project)
├── schemas.py # DTO (global, a contract for clients and services)
└── utils.py # global non-business logic 


- client_module - Client base module for external service communication
- server_module - Package with standart API for this microservice


Important!
database.py - SINGLETON connector

