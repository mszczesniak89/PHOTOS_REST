from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ForeignKey
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from photos_rest.photo_host.models import AccountPlan


class User(AbstractUser):
    """Default user for PHOTOS_REST."""
    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    account_plan = ForeignKey('AccountPlan', blank=False, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
