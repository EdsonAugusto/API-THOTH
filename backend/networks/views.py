from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Switch, SwitchPort
from.serializers import SwitchSerializer, SwitchPortSerializer


class SwitchViewset(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'manufacturer', 'model', 'is_manageable', 'installation_date', 'warranty_period', 'number_of_ports', 'port_speed', 'created', 'created_by', 'status')
    search_fields = ('identification', 'manufacturer', 'model', 'is_manageable')
    ordering_fields = ('created_by', 'identification', 'model', 'is_manageable')

class SwitchPortViewset(viewsets.ModelViewSet):
    queryset = SwitchPort.objects.all()
    serializer_class = SwitchPortSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('switch', 'port_number', 'vlan', 'protocol', 'speed')
    search_fields = ('switch__identification', 'port_number', 'vlan', 'protocol', 'speed')
    ordering_fields = ('switch', 'protocol')