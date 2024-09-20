from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the custom user model
CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Use CharField to handle passwords securely
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Use the custom user model's create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the newly created user
        Token.objects.create(user=user)
        return user
