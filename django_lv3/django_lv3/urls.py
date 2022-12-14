"""django_lv3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from forms_app.views import contatti,homepage
from blog.views import crea_post_view
from prova_pratica.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="home"),
    path('contattaci/',contatti,name="contatti"),
    path('crea-post/',crea_post_view,name="crea_post"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('contatti/',contact_view,name="contact_view")
]