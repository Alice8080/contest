"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from viewflow.contrib.admin import Admin
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Site, Application

from data.views import CustomUserViewset

site = Site(
    title="Приложение",
    primary_color="#3949ab",
    secondary_color="#5c6bc0",
    viewsets=[
        # AtlasApp(),
        # StaffApp(),
        Application(
            app_name="users",
            title="Пользователи",
            icon="user",
            viewsets=[
                CustomUserViewset()
                # CategoryViewset(),
                # SubCategoryViewset(),
                # ProjectViewset(),
                # TaskViewset(),
            ],
        ),
        # SalesApp(),
        # Admin(),
    ],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theme_soft_design.urls')),
    path("", site.urls),
    path("accounts/", AuthViewset().urls),
]
