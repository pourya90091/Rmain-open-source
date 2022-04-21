from rest_framework import serializers


class SettingsModelSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password1 = serializers.CharField(max_length=20)
    password2 = serializers.CharField(max_length=20)
    error = serializers.CharField(max_length=20)
    url = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100)
    cookie_content = serializers.CharField(max_length=72)
    MEDIA_URL = serializers.CharField(max_length=20)

