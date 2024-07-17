from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'flightApp_DRF', # database_name
#         'USER': 'postgres', # login_user_name
#         'PASSWORD': '4518***', # login_user_pass (setted on install)
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# print(config('SQL_PASSWORD'))
DATABASES = { 
    "default": { 
        "ENGINE": "django.db.backends.postgresql", 
        "NAME": config("SQL_DATABASE_NAME"), 
        "USER": config("SQL_USER_NAME"), 
        "PASSWORD": config('SQL_PASSWORD'), 
        "HOST": config("SQL_HOST"), 
        "PORT": config("SQL_PORT"), 
        # "ATOMIC_REQUESTS": True, 
    } 
}
#ana dizinde debug.log içinde istdiğin ayara göre tutar Ayarlar.INFO WARNING ERROR CRITICAL ...VS
LOGGING = {
    "version": 1,
    # is set to True then all loggers from the default configuration will be disabled.
    "disable_existing_loggers": True,
    # Formatters describe the exact format of that text of a log record. 
    "formatters": {
        "standard": {
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s"
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # The handler is the engine that determines what happens to each message in a logger.
    # It describes a particular logging behavior, such as writing a message to the screen, 
    # to a file, or to a network socket.
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "ERROR",
            "stream": "ext://sys.stdout",
            },
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'INFO',          
        },
    },
    # A logger is the entry point into the logging system.
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
            # log level describes the severity of the messages that the logger will handle. 
            "level": config("DJANGO_LOG_LEVEL", "INFO"),
            'propagate': True,
            # If False, this means that log messages written to django.request 
            # will not be handled by the django logger.
        },
    },
}