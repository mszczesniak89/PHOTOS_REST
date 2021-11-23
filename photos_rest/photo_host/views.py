from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import generics
from photos_rest.photo_host.models import AccountPlan, ThumbnailType, UserImage
from photos_rest.photo_host.serializers import AdminAccountPlanSerializer, AdminThumbnailTypeSerializer, \
    AdminUserImageSerializer, UserImageSerializer, UserImageAddSerializer, UserImageListSerializer


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

    def test_func(self):
        return self.request.user.is_staff


class AdminUserImageView(UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = UserImage.objects.all()
    serializer_class = AdminUserImageSerializer

    def test_func(self):
        return self.request.user.is_staff


class UserImageListView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = UserImageListSerializer

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)


class UserImageView(LoginRequiredMixin, UserPassesTestMixin, generics.RetrieveAPIView):
    serializer_class = UserImageSerializer

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)

    def test_func(self):
        return self.request.user == self.get_object().user


class UserImageAddView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = UserImageAddSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        return super(UserImageAddView, self).perform_create(serializer)


class UserImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, generics.UpdateAPIView):
    serializer_class = UserImageAddSerializer

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)

    def test_func(self):
        return self.request.user == self.get_object().user


class UserImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, generics.DestroyAPIView):
    serializer_class = UserImageAddSerializer

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)

    def test_func(self):
        return self.request.user == self.get_object().user

