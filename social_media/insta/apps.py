
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insta'

    def ready(self):
        import insta.signals  # اطمینان حاصل کنید که نام اپلیکیشن شما درست است