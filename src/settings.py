import os

from src.libs.security.utils import file_to_base64


APP_NAME = "Deeployr"
DESCRIPTION = "Deeployr is an open-source CI/CD tools"
VERSION = "0.0.0.pre-alpha"
DOMAIN = "https://api.deeployr.com"

# Validators config
PASSWORD_MIN_LENGTH = 10
UNUSED_ACCOUNT_DELAY = 7  # 7 days

# Auth token validity
TOKEN_VALIDITY = 60 * 60 * 0.5  # 30 minutes
TOKEN_TEMP_VALIDITY = 60 * 3  # 3 minutes

# Validity of a request change (email or password)
REQUEST_VALIDITY = 60 * 5
REQUEST_DAYS_HISTORY = 90

LINK_TO_CHANGE_EMAIL = os.getenv("LINK_TO_CHANGE_EMAIL", "")
LINK_TO_CHANGE_PASSWORD = os.getenv("LINK_TO_CHANGE_PASSWORD", "")

# i18n/l10n
AVAILABLE_LANGUAGES = {
    "fr": "Français",
    "en": "English",
}

LOCALE = os.getenv("LOCALE", "en_GB")
TIMEZONE = os.getenv("TIMEZONE", "Europe/London")

# Emails config
EMAIL_LOGO = f"""data:image/svg+xml;base64,{
    file_to_base64("src/static/deeployr-light.svg")
}"""
