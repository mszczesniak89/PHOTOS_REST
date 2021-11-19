from rest_framework import serializers
from photos_rest.photo_host.models import AccountPlan, UserImage, ThumbnailType


class AccountPlanSerializer(serializers.ModelSerializer):
    thumbnail_types = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='thumbnail-type-detail',
    )

    class Meta:
        model = AccountPlan
        fields = ['all']
