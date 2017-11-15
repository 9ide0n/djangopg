ALLOWED_HOSTS = ["192.168.33.15",]

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "test_database",
        # Not used with sqlite3.
        "USER": "test_user",
        # Not used with sqlite3.
        "PASSWORD": "qwerty",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "192.168.33.15",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "5432",
    }
}

INSTALLED_APPS += [
    'polls.apps.PollsConfig',
]
