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

python3 -m venv deeployr
cd deeployr
git clone git@github.com:Valbou/deeployr.git
cd deeployr
```

Config your own .env file (based on template.env file in project folder)
Please change the default SECRET_KEY if you are using sessions.
