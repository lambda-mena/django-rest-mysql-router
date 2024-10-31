from rest_framework import serializers

def validate_password_strength(raw_password):
    if len(raw_password) < 8:
        raise serializers.ValidationError('Password must be at least 8 characters long.')
    if not any(char.isdigit() for char in raw_password):
        raise serializers.ValidationError('Password must contain at least one digit.')
    if not any(char.isupper() for char in raw_password):
        raise serializers.ValidationError('Password must contain at least one uppercase letter.')
    if not any(char.islower() for char in raw_password):
        raise serializers.ValidationError('Password must contain at least one lowercase letter.')
    return raw_password
