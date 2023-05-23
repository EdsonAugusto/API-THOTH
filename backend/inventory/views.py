from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Equipment, IPAddress, Rack 
from.serializers import EquipmentSerializer, IPAddressSerializer, RackSerializer


class EquipmentViewset(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'responsible_sector', 'rack_installed__identification', 'ip_address__ip', 'description_equipment', 'created', 'created_by', 'status')
    search_fields = ('identification', 'status')
    ordering_fields = ('identification', 'created_by')

class IPAddressViewset(viewsets.ModelViewSet):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('ip', 'subnet', 'equipment', 'is_available', 'created_at', 'updated_at')
    search_fields = ('ip', 'subnet', 'created_at')
    ordering_fields = ('ip', 'subnet')

class RackViewset(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('identification', 'pop_installed__name', 'created', 'created_by', 'status')
    search_fields = ('identification', 'pop_installed__name', 'status')
    ordering_fields = ('created_by', 'identification')