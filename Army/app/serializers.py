from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Remove password from validated data
        password = validated_data.pop("password")

        # Create user without saving to the database yet
        user = User(**validated_data)

        # Hash the password using set_password
        user.set_password(password)

        # Save the user object
        user.save()
        return user

    def update(self, instance, validated_data):
        # Remove password from validated data if it's provided
        password = validated_data.pop("password", None)

        # Update user with the rest of the data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # If password is provided, hash it using set_password
        if password:
            instance.set_password(password)

        # Save the updated user object
        instance.save()
        return instance
