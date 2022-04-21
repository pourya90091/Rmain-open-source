from rest_framework import serializers


class SettingsModelSerializer(serializers.Serializer):
    new_jokes = serializers.JSONField()
