"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


# config/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app.views.auth_views import Home, Login, Logout
from app.views.catalogo_views import (
    CatalogoListView,
    CatalogoCreateView,
    CatalogoUpdateView,
    CatalogoDeleteView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path("login/", Login.as_view(), name="login"),
    path('home/', Home.as_view(), name="home"), 
    path("logout/", Logout.as_view(), name="logout"),

    
    
    # URLs para el ABM de Catálogo (Class-Based Views)
    path('catalogos/', CatalogoListView.as_view(), name='lista_catalogos'),
    path('catalogos/crear/', CatalogoCreateView.as_view(), name='crear_catalogo'),
    path('catalogos/editar/<int:pk>/', CatalogoUpdateView.as_view(), name='editar_catalogo'),
    path('catalogos/eliminar/<int:pk>/', CatalogoDeleteView.as_view(), name='eliminar_catalogo'),
]