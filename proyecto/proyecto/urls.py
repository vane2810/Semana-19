"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views as ap1v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap1v.index,name="home"),
    path('registro/', ap1v.reg_user,name='registro'),
    path('login/', ap1v.iniciar_sesion,name="login"),
    path('logout/', ap1v.cerrar_sesion, name='logout'),
    path('proveedores/', ap1v.list_prov),
    path('add_proveedores/', ap1v.add_proveedor, name="add_proveedores"),
    path('productos/', ap1v.list_prod),
     path('add_producto/', ap1v.add_producto, name="add_producto"),
]
