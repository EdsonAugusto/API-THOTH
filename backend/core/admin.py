from django.contrib import admin

from .models import Company, Sector, Extensions, DataCenter, AccessRelease, ImportantAccesses, ProActiveContacts, ProviderContacts


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnpj', 'phone', 'site', 'created_by', 'is_active']
    search_fields = ['name', 'phone', 'is_active']
    list_filter = ['created_by', 'name']


class SectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'flag_company', 'acting_sector', 'phone_company', 'created', 'status']
    search_fields = ['name', 'flag_company__name', 'acting_sector']
    list_filter = ['flag_company', 'name', 'acting_sector', 'status']

    def phone_company(self, obj):
        return obj.flag_company.phone  # Altere 'company' para 'flag_company'
    phone_company.short_description = 'Telefone da Empresa'


class ExtensionsAdmin(admin.ModelAdmin):
    list_display = ['employee', 'branch_line', 'acting_sector', 'created', 'mac_phone', 'status']
    search_fields = ['employee','acting_sector']
    list_filter = ['employee', 'branch_line', 'acting_sector']


class DataCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'responsible_company','acting_sector', 'phone_number', 'cell_number', 'email',  'created']
    search_fields = ['name', 'acting_sector', 'responsible_company__name']
    list_filter =  ['name', 'acting_sector', 'responsible_company__name']


class AccessReleaseAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'employees_CPF', 'employees_RG', 'acting_sector', 'status']
    search_fields = ['employee_name', 'acting_sector']
    list_filter =  ['employee_name', 'acting_sector']

class ImportantAccessesAdmin(admin.ModelAdmin):
	list_display = ['user', 'password_acesses', 'access_url', 'note']
	search_fields = ['user', 'access_url']
	list_filter = ['user', 'access_url']

class ProActiveContactsAdmin(admin.ModelAdmin):
	list_display = ['responsible_company', 'name_client', 'phone', 'email','note']
	search_fields = ['name_client', 'phone']
	list_filter = ['name_client', 'phone']

class ProviderContactsAdmin(admin.ModelAdmin):
	list_display = ['responsible_company', 'name_provider', 'phone', 'email', 'note']
	search_fields = ['name_provider', 'phone']
	list_filter = ['name_provider', 'phone']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Extensions, ExtensionsAdmin)
admin.site.register(DataCenter, DataCenterAdmin)
admin.site.register(AccessRelease, AccessReleaseAdmin)
admin.site.register(ImportantAccesses, ImportantAccessesAdmin)
admin.site.register(ProActiveContacts, ProActiveContactsAdmin)
admin.site.register(ProviderContacts, ProviderContactsAdmin)