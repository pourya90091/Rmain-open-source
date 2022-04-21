from rest_framework import serializers
from games_module.models import H
from games_module.models import J


class HModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = H
        fields = '__all__'


class JModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = J
        fields = '__all__'
