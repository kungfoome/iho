## Quickstart

Then run the following commands to bootstrap your environment with `poetry`: ::

    git clone https://github.com/kungfoome/iho
    cd iho
    poetry install
    poetry shell

To run the web application in debug use::

    uvicorn app.main:app --reload
    Open your browser at
        http://127.0.0.1:8000/docs to get to Swagger
        http://127.0.0.1:8000/redoc to get ReDoc

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging, helpers.
    ├── db               - db related stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    └── main.py          - FastAPI application creation and configuration.
