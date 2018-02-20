from django.apps import AppConfig


class CoreConfig(AppConfig):
    # because of django.core.exceptions.ImproperlyConfigured: Application labels aren't unique, duplicates: auth
    name = 'authentication'

