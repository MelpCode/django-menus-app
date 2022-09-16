"""django_menus_app URL Configuration

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
from django.urls import path
from menus.views import menus, create_menu, delete_menu, edit_menu,search_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menus/',menus),
    path('menus/new/',create_menu, name="create_menu"),
    path('menus/delete/<int:menu_id>',delete_menu, name="delete_menu"),
    path('menus/edit/<int:menu_id>', edit_menu, name="edit_menu"),
    path('menus/search',search_menu)
]
