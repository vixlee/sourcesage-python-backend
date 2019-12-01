# User-API Restful by Vix Lee

## Overview
The application is a Rest-Ful API for
This app is served to the client by `app.py` on port 8000 default.

## System requirements
To build and develop, you need to have [Python3](https://www.python.org/downloads/), [Flask](https://pypi.org/project/Flask/), [SQLAlchemy](https://pypi.org/project/SQLAlchemy/),etc..

## Folders/Files structure
```
sourcesage_python_backend
├── app.py
├── common.py
├── config.py
├── __init__.py
├── migrate.py
├── models.py
├── README.md
└── requirement.txt
```

## Frameworks / Libs

This application base on [Flask](https://pypi.org/project/Flask/).
Libray to handle action with database user [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)
Database engine is [SQLite](https://docs.python.org/2/library/sqlite3.html)
Library to handle JSON Web Token is [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/)
Library to handle serialization/deserialization is [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
Library to handle send mail is [Flask-Mail](https://pythonhosted.org/Flask-Mail/)

## Developing

###  Step 1: Creates virtual environment

```
python3 -m venv env
```

###  Step 2: Install all dependencies
From your terminal, make sure you are in the root folder of the project then run the below command:

```
pip3 install -r requirements.txt
```
This will download and install all the extensions in `requirements.txt`

###  Step 3: Running migrations

#### Initial migrations
Migrations are like version control for your database, allowing your team to easily modify and share the application's database schema. If you have ever had to tell a teammate to manually add a column to their local database schema, you've faced the problem that database migrations solve. In this tutorial, we are using a flask extension - flask migrate to acheive this.
Run migrations initialization, using the db init command as follows:

```
python3 migrate.py db init
```

```bash
  Creating directory /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations ...  done
  Creating directory /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/versions ...  done
  Generating /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/README ...  done
  Generating /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/script.py.mako ...  done
  Generating /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/alembic.ini ...  done
  Generating /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/env.py ...  done
  Please edit configuration/connection/logging settings in '/home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/alembic.ini' before proceeding.
```

#### Migrations
Run the script that populates the migration script with the detected changes in the
models. In this case, it is the first time we populate the migration script, and therefore, the
migration script will generate the tables that will persist `User`

```
python migrate.py db migrate
```

```bash
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
  Generating /home/lehungvi/Documents/workspace/sourcesage/sourcesage_python_backend/migrations/versions/c09b23d96c2c_.py ...  done
```

#### Upgrade
Then apply the migration to the database. Run the upgrade command
```
python migrate.py db upgrade
```

```bash
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> eb60b5cd33c0, empty message
```

### Step 3: Run User-API application
Under folder `user-api` run command:

```
python3 app.py
```

```bash
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```

Now, `user-api` is running.
