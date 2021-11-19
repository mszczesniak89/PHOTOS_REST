from django.db.models import Model, CharField, ForeignKey, BooleanField, ManyToManyField, IntegerField, CASCADE, \
    ImageField
from photos_rest.users.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


# Create your models here.


class AccountPlan(Model):
    name = CharField(_("Name of the Account Plan"), blank=False, max_length=255)
    original_file_access = BooleanField('Original file access', default=False)
    expiring_links_access = BooleanField('Expiring links access', default=False)
    thumbnail_types = ManyToManyField('ThumbnailType')


class ThumbnailType(Model):
    name = CharField(_("Name of the thumbnail type"), blank=False, max_length=255)
    img_height = IntegerField(_("Image height"), null=False, blank=False)
    img_width = IntegerField(_("Image width"), null=True, blank=True)


class UserImage(Model):
    name = CharField(_("Name of the user image"), blank=False, max_length=255)
    user = ForeignKey(User, blank=False, null=False, on_delete=CASCADE)
    image = ImageField(upload_to="user_images/")

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.name


