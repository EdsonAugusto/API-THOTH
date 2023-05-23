from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Softswitch_VSC, Server_Gateway, Server_PABx, Server_Portability, Server_XenServer
from .serializers import Softswitch_VSCSerializer, Server_GatewaySerializer, Server_PABxSerializer, Server_PortabilitySerializer, Server_XenServerSerializer


class Softswitch_VSCViewset(viewsets.ModelViewSet):
    queryset = Softswitch_VSC.objects.all()
    serializer_class = Softswitch_VSCSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('id_vsc', 'identification', 'server_type', 'ip_address', 'portability_server', 'idrac', 'server_port_count')
    search_fields = ('id_vsc', 'identification', 'server_type', 'ip_address')
    ordering_fields = ('created_by', 'identification', 'server_type')

class Server_GatewayViewset(viewsets.ModelViewSet):
    queryset = Server_Gateway.objects.all()
    serializer_class = Server_GatewaySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'ip_address',  'server_type')
    search_fields = ('identification', 'server_type')
    ordering_fields = ('identification', 'server_type')

class Server_PABxViewset(viewsets.ModelViewSet):
    queryset = Server_PABx.objects.all()
    serializer_class = Server_PABxSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'ip_address',  'server_type')
    search_fields = ('identification', 'server_type')
    ordering_fields = ('identification', 'server_type')

class Server_PortabilityViewset(viewsets.ModelViewSet):
    queryset = Server_Portability.objects.all()
    serializer_class = Server_PortabilitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'ip_address')
    search_fields = ('identification', 'ip_address')
    ordering_fields = ('identification', 'ip_address')

class Server_XenServerViewset(viewsets.ModelViewSet):
    queryset = Server_XenServer.objects.all()
    serializer_class = Server_XenServerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'ip_address')
    search_fields = ('identification', 'ip_address')
    ordering_fields = ('identification', 'ip_address')