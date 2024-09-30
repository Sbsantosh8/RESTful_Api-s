from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.


class Useradmin(admin.ModelAdmin):

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "password",
            "first_name",
            "last_name",
        ]
