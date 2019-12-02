"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('kitchens/', include('kitchens.urls'))
"""
from django.contrib import admin
# from django.urls import path,include
# from . import views
#
#
# #function view import statement
#
#
# urlpatterns = [
#     path('', views.index, name='kitchens-home'),
#     path('index/', views.index, name='kitchens-home'),
#     path('about/', views.about, name='kitchens-about'),
#
# ]


from django.contrib import admin
from django.urls import path, include
from . import views

# function view import statement

from django.urls import path

# class based urls below
from .views import (
    KitchenListView,
    KitchenDetailView,
    KitchenCreateView,
    KitchenUpdateView,
    KitchenDeleteView
)

# function based views use this statement
from . import views

urlpatterns = [
    # routes for function based views
    # path('', views.home, name='kitchens-home'),
    # path('index/', views.home, name='kitchens-home'),
    # path('about/', views.about, name='kitchens-about'),
    #  end routes for function based views


# create, read, update, delete
# class based urls below
#     uses template home.html and this has to be converted using .as_view() function invoked
    path('', KitchenListView.as_view(), name='kitchens-home'),

    # uses kitchen_detail.html template
    path('kitchen/<int:pk>/', KitchenDetailView.as_view(), name='kitchen-detail'),

    # Expects kitchen_form.html template. it does not expect post_create like you might think django uses post_form instead
    path('kitchen/new/', KitchenCreateView.as_view(), name='kitchen-create'),


   # also uses kitchen_form.html template and shares it with the above post/new
    path('kitchen/<int:pk>/update/', KitchenUpdateView.as_view(), name='kitchen-update'),

    path('kitchen/<int:pk>/delete/', KitchenDeleteView.as_view(), name='kitchen-delete'),

    path('about/', views.about, name='kitchens-about'),

]

