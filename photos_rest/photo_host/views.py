from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import generics
from photos_rest.photo_host.models import AccountPlan, ThumbnailType, UserImage
from photos_rest.photo_host.serializers import AdminAccountPlanSerializer, AdminThumbnailTypeSerializer, \
    AdminUserImageSerializer, UserImageSerializer


# Create your views here.


class AdminAccountPlanListView(UserPassesTestMixin, generics.ListCreateAPIView):
    queryset = AccountPlan.objects.all()
    serializer_class = AdminAccountPlanSerializer

    def test_func(self):
        return self.request.user.is_staff


class AdminAccountPlanView(UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountPlan.objects.all()
    serializer_class = AdminAccountPlanSerializer

    def test_func(self):
        return self.request.user.is_staff


class AdminThumbnailTypeListView(UserPassesTestMixin, generics.ListCreateAPIView):
    queryset = ThumbnailType.objects.all()
    serializer_class = AdminThumbnailTypeSerializer

    def test_func(self):
        return self.request.user.is_staff


class AdminThumbnailTypeView(UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ThumbnailType.objects.all()
    serializer_class = AdminThumbnailTypeSerializer

    def test_func(self):
        return self.request.user.is_staff


class AdminUserImageListView(UserPassesTestMixin, generics.ListCreateAPIView):
    queryset = UserImage.objects.all()
    serializer_class = AdminUserImageSerializer


class AdminUserImageView(UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = UserImage.objects.all()
    serializer_class = AdminUserImageSerializer


class UserImageListView(LoginRequiredMixin, generics.ListCreateAPIView):
    serializer_class = UserImageSerializer

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        return super(UserImageListView, self).perform_create(serializer)


class UserImageView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserImageSerializer

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super(UserImageView, self).get_serializer_context()
        thumbnail_types = ThumbnailType.objects.filter(accountplan__user=self.request.user)
        context['thumbnail_types'] = 'guwno'
        # context['thumbnail_types'] = [item.name for item in thumbnail_types]
        return context
        # return {
        #     'request': self.request,
        #     'thumbnail_types': 'test1', 'test2',
        # }

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
