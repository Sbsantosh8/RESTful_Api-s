from django.contrib import admin
from django.urls import path, include
from .views import (
    RegisterUserAPIView,
    ListUserAPIView,
    UpdateUserAPIView,
    DeleteUserAPIView,
)

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("list/", ListUserAPIView.as_view(), name="list"),
    path("list/<str:username>/", ListUserAPIView.as_view(), name="list"),
    path("update/<str:username>/", UpdateUserAPIView.as_view(), name="update"),
    path("delete/<str:username>/", DeleteUserAPIView.as_view(), name="delete"),
]
