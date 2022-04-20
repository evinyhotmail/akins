from django.apps import AppConfig


class AkinsApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'akins_api'

    # Add this line if you want to keep separate all signals in a file.

    def ready(self):
        import akins_api.signals
