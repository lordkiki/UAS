"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from personal.views import home_screen_view
from personal.views import crud1
from personal.views import add
from personal.views import edit
from personal.views import update
from personal.views import delete
from django.urls import path
from personal.views import tbcarsApi
from personal.views import rsa
from personal.views import encrypt
from personal.views import decrypt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', home_screen_view),
    path('', crud1),
    path('add', add),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
    path('cars', tbcarsApi),
    path('cars/<int:id>', tbcarsApi),
    path('chat', rsa),
    path('encrypt', encrypt),
    path('decrypt', decrypt),
]
