from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('doctors',views.doctors),
    path('main',views.main),
     path('contacts',views.contacts),
]
