from rest_framework import serializers
from .models import Softswitch_VSC, Server_Gateway, Server_PABx, Server_Portability, Server_XenServer


class Softswitch_VSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softswitch_VSC
        fields = '__all__'

class Server_GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Server_Gateway
        fields = '__all__'

class Server_PABxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server_PABx
        fields = '__all__'

class Server_PortabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Server_Portability
        fields = '__all__'

class Server_XenServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server_XenServer
        fields = '__all__'