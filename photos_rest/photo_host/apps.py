from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PhotoHostConfig(AppConfig):
    name = "photos_rest.photo_host"
    verbose_name = _("Photo Host")
