from django.contrib import admin
from photos_rest.photo_host.models import AccountPlan, UserImage, ThumbnailType

# Register your models here.

admin.site.register(AccountPlan)
admin.site.register(UserImage)
admin.site.register(ThumbnailType)


