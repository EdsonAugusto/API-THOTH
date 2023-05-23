from rest_framework import serializers
from .models import Equipment, IPAddress, Rack


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = '__all__'

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = '__all__'