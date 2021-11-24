from django.db.models import Model, CharField, ForeignKey, BooleanField, ManyToManyField, IntegerField, CASCADE, \
    ImageField
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from versatileimagefield.fields import VersatileImageField, PPOIField

import config.settings.base
# Create your models here.


class AccountPlan(Model):
    name = CharField(_("Name of the Account Plan"), blank=False, max_length=255)
    original_file_access = BooleanField('Original file access', default=False)
    expiring_links_access = BooleanField('Expiring links access', default=False)
    thumbnail_types = ManyToManyField('ThumbnailType')

    def __str__(self):
        return self.name


class ThumbnailType(Model):
    name = CharField(_("Name of the thumbnail type"), blank=False, max_length=255)
    img_height = IntegerField(_("Image height"), null=False, blank=False)
    img_width = IntegerField(_("Image width"), null=True, blank=True)

    def __str__(self):
        return self.name


class UserImage(Model):
    name = CharField(_("Name of the user image"), blank=False, max_length=255)
    user = ForeignKey(config.settings.base.AUTH_USER_MODEL, blank=False, null=False, on_delete=CASCADE)
    image = VersatileImageField(
        'Image',
        upload_to='ser_images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.name

    @property
    def thumbnails(self):
        return self.user.account_plan.thumbnail_types.all()



