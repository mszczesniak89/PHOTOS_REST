from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from photos_rest.photo_host.views import AdminAccountPlanListView, AdminThumbnailTypeListView, AdminThumbnailTypeView, \
    AdminAccountPlanView, \
    AdminUserImageListView, AdminUserImageView, UserImageListView, UserImageView, UserImageAddView, UserImageUpdateView, \
    UserImageDeleteView, UserImageExpiringLinkVew

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("photos_rest.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path('admin/account-plans/', AdminAccountPlanListView.as_view()),
    path('admin/account-plan/<int:pk>/', AdminAccountPlanView.as_view(), name='admin-account-plan-detail'),
    path('admin/thumbnail-types/', AdminThumbnailTypeListView.as_view()),
    path('admin/thumbnail-type/<int:pk>/', AdminThumbnailTypeView.as_view(), name='admin-thumbnail-type-detail'),
    path('admin/user-images/', AdminUserImageListView.as_view()),
    path('admin/user-image/<int:pk>/', AdminUserImageView.as_view(), name='admin-user-image-detail'),
    path('user-images/', UserImageListView.as_view(), name='user-images'),
    path('user-image/<int:pk>/', UserImageView.as_view(), name='user-image-detail'),
    path('user-image/add/', UserImageAddView.as_view(), name='user-image-add'),
    path('user-image/<int:pk>/update/', UserImageUpdateView.as_view(), name='user-image-update'),
    path('user-image/<int:pk>/delete/', UserImageDeleteView.as_view(), name='user-image-delete'),
    path('user-image/<int:pk>/temp-link/<int:exp_time>/', UserImageExpiringLinkVew.as_view(),
         name='user-image-temp-link'),

]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
