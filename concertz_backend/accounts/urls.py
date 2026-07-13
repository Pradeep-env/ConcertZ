from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.index, name = "index"),
    path('accounts/user', views.user, name = "user"),
]
