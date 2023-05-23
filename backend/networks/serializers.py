from rest_framework import serializers
from .models import Switch, SwitchPort


class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'

class SwitchPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwitchPort
        fields = '__all__'