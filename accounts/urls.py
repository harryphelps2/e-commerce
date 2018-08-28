from django.conf.urls import url, include
from accounts.views import index, user_logout, user_login, user_registration, user_profile
from django.urls import path, re_path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index, name="index"),
    re_path(r'^accounts/register/', user_registration, name="register"),
    re_path(r'^accounts/profile/', user_profile, name="profile"),
]