from rest_framework import serializers
from .validators import validate_password_strength

class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, validators=[validate_password_strength])
