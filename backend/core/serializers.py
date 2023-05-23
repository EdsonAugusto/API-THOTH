from rest_framework import serializers
from .models import Company, Sector, Extensions, DataCenter, AccessRelease, ImportantAccesses, ProActiveContacts, ProviderContacts


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class ExtensionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extensions
        fields = '__all__'

class DataCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCenter
        fields = '__all__'

class AccessReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRelease
        fields = '__all__'

class ImportantAccessesSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImportantAccesses
		fields = '__all__'

class ProActiveContactsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProActiveContacts
		fields = '__all__'
		
class ProviderContactsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProviderContacts
		fields = '__all__'