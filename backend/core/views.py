from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Company, Sector, Extensions, DataCenter, AccessRelease, ImportantAccesses, ProActiveContacts, ProviderContacts
from.serializers import CompanySerializer, SectorSerializer, ExtensionsSerializer, DataCenterSerializer, AccessReleaseSerializer, ImportantAccessesSerializer, ProActiveContactsSerializer, ProviderContactsSerializer


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('name', 'cnpj', 'phone', 'site', 'created_at', 'is_active')
    search_fields = ('name', 'phone', 'is_active')
    ordering_fields = ('name', 'created_at')

    def perform_destroy(self, instance):
        user = self.request.user

class SectorViewset(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('name', 'email', 'flag_company', 'acting_sector', 'created', 'status')
    search_fields = ('name', 'flag_company__name', 'acting_sector')
    ordering_fields = ('flag_company', 'flag_company__name')

class ExtensionsViewset(viewsets.ModelViewSet):
    queryset = Extensions.objects.all()
    serializer_class = ExtensionsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('employee', 'branch_line', 'acting_sector', 'created', 'mac_phone', 'status')
    search_fields = ('employee','acting_sector')
    ordering_fields = ('employee', 'branch_line', 'acting_sector')

class DataCenterViewset(viewsets.ModelViewSet):
    queryset = DataCenter.objects.all()
    serializer_class = DataCenterSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('name', 'responsible_company','acting_sector', 'phone_number', 'cell_number', 'email',  'created')
    search_fields = ('name','acting_sector',  'responsible_company__name')
    ordering_fields = ('name', 'acting_sector', 'responsible_company__name')

class AccessReleaseViewset(viewsets.ModelViewSet):
    queryset = AccessRelease.objects.all()
    serializer_class = AccessReleaseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('employee_name', 'employees_CPF', 'employees_RG', 'acting_sector', 'status')
    search_fields = ('employee_name', 'acting_sector')
    ordering_fields = ('employee_name', 'acting_sector')

class ImportantAccessesViewset(viewsets.ModelViewSet):
	queryset = ImportantAccesses.objects.all()
	serializer_class = ImportantAccessesSerializer
	filter_backends = [
		DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
	]
	filterset_fields = ('user', 'password_acesses', 'access_url', 'note')
	search_fields = ('user')
	ordering_fields = ('user')

class ProActiveContactsViewset(viewsets.ModelViewSet):
	queryset = ProActiveContacts.objects.all()
	serializer_class = ProActiveContactsSerializer
	filter_backends = [
		DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
	]
	filterset_fields = ('responsible_company', 'name_client', 'phone', 'email','note')
	search_fields = ('responsible_company', 'name_client')
	ordering_fields = ('name_client', 'responsible_company')

class ProviderContactsViewset(viewsets.ModelViewSet):
	queryset = ProviderContacts.objects.all()
	serializer_class = ProviderContactsSerializer
	filter_backends = [
		DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
	]
	filterset_fields = ('responsible_company', 'name_provider', 'phone', 'email', 'note')
	search_fields = ('responsible_company', 'name_provider')
	ordering_fields = ('name_provider', 'responsible_company')