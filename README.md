# Simple Twitter App

- this is to practice Django to build twitter-like functionality

## Server Setup

- setup a MySQL server locally before running this app
    - use brew sql install and xcode command line tools for MySQL to work on macOS
    - install the SQL server on Windows
- create a DB that matches the name in the `settings.py` in SQL server
    - ensure the right credentials for DB in `settings.py`

## Install dependencies 


```
pip install -r requirements.txt
```

## Activate virtual environment

```zsh
source bin/activate
```

## Run the development server 

```zsh
python manage.py runserver
```