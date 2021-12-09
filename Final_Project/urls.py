"""Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, settings

urlpatterns = [
    path('index/',views.index,name='index'),
    path('shipments/',views.shipments,name="shipments"),
    path('shipments/<str:id>',views.shipment,name="shipments"),
    path('archive/', views.archive, name="archive"),
    path('manage/', views.manage, name="manage"),
    path('manage/<int:id>', views.editClient, name="editClient"),
    path('manage/<int:id>/', views.deleteClient, name="deleteClient"),
    path('login/', views.login, name="login"),
    path('register/',views.register,name="register"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('404/',views.notfound,name="404"),
] + static(settings.STATIC_URL)

