from rest_framework import serializers
from photos_rest.photo_host.models import AccountPlan, UserImage, ThumbnailType
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework.serializers import ImageField


class AdminAccountPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountPlan
        fields = ['id', 'name', 'original_file_access', 'expiring_links_access', 'thumbnail_types']


class AdminThumbnailTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThumbnailType
        fields = '__all__'


class AdminUserImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserImage
        fields = '__all__'


class UserImageAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserImage
        exclude = ['user', 'image_ppoi']


class UserImageSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='user-image-detail', format='html')
    original_image = serializers.SerializerMethodField()
    thumbnails = serializers.SerializerMethodField()

    class Meta:
        model = UserImage
        exclude = ['user', 'image', 'image_ppoi']

    def get_thumbnails(self, obj):
        thumbnail_types = obj.user.account_plan.thumbnail_types.all()
        thumbnails = {th_type.name: self.context['request'].build_absolute_uri(
            obj.image.thumbnail[f'{th_type.img_height}x{th_type.img_width or th_type.img_height}']) for th_type in
            thumbnail_types}
        return thumbnails

    def get_original_image(self, obj):
        if obj.user.account_plan.original_file_access:
            return self.context['request'].build_absolute_uri(obj.image.url)
