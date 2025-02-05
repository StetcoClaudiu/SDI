"""ShopParts URL Configuration

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
from ShopParts import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parts/', views.part_list),
    path('users/', views.user_list),
    path('orders/', views.order_list),
    path('users/<int:id>/',views.user_detail),
    path('parts/<int:id>/',views.part_detail),
    path('orders/<int:id>/',views.order_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
