# Deeployr - CI/CD tools

Deeployr aims to provide CI/CD tools to simply work on classic infrastructure - ServerFull :).
No Cloud tools here.

![License AGPLv3](https://img.shields.io/badge/license-AGPLv3-blue "License AGPLv3")
![Python v3.10+](https://img.shields.io/badge/python-v3.10-blue "Python v3.10")
![Tests 238 passed](https://img.shields.io/badge/tests-238%20passed-green "Tests 238 passed")
![Coverage 93%](https://img.shields.io/badge/coverage-93%25-green "Coverage 93%")
[![CodeFactor](https://www.codefactor.io/repository/github/valbou/deeployr/badge)](https://www.codefactor.io/repository/github/valbou/deeployr)

You can follow the [Roadmap](ROADMAP.md)

It's a very early stage of development, so it may include major vulnerabilities.
**Please do not use in production !**

## Technical informations

### Install project

```bash
apt install postgresql lsb-release redis
apt install git python3-venv python3-pip

python3 -m venv deeployr-project
cd deeployr-project
git clone git@github.com:Valbou/deeployr.git
cd deeployr
```

Config your own .env file (based on template.env file in project folder)
Please change the default SECRET_KEY if you are using sessions.

### Install dependencies

```bash
pip install .
```
or to contribute
```
pip install -e .
```

### Install translations

```bash
chmod +x trad_*
./trad_compile_mo.sh users
```

### Run migrations

```bash
alembic upgrade head
```

### To run flask
```bash
# With Werkzeug (dev :5000)
flask --app src.flask run

# With Gunicorn (prod :8000)
gunicorn src.flask:app
```

## Technical informations for developpers

Follow previous steps, an continue with steps below.

### Install dev dependencies

```bash
pip install .[dev]
```

### Add migrations

If you change models

```bash
alembic revision --autogenerate
```

### To run tests
```bash
python -m coverage run -m unittest -vv
```

### To see coverage
```bash
python -m coverage report
```

### To contribute

To contribute:
- clone this git repository first.
- Create a branch nammed like this: "feat-good-feature-#42".
- Use commit namming convention: "feat: my commit message".
- Run tests and check your code coverage (coverage is not just a high %)
- Make a pull request ! <3

## How to help ?

- First you can encourage development with starring project <3
- Give us feedback in issues: what you need, what doesn't work for you...
- If you are a dev, you can submit pull request linked to issues
- If you are a polyglot, you can translate using .po files
- If you are an user, you can write an end user documentation

All with kindness, we are just humans ;)
