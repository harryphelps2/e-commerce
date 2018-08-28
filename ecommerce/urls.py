"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from accounts.views import index, user_login, user_logout
from accounts import urls as accounts_urls
from django.contrib.auth import views as auth_views
from products import urls as urls_products
from cart import urls as urls_cart
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', all_products, name="index"),
    path('accounts/', include(accounts_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$',user_login, name="login" ),
    url(r'^logout/$', user_logout, name="logout"),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name="passwordreset"),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view()),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view()),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view()),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]

