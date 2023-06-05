from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MusicConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ensong.music"
    verbose_name = _("Music")

    def ready(self):
        try:
            import ensong.users.signals  # noqa: F401
        except ImportError:
            pass
