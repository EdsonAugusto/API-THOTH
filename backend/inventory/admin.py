from django.contrib import admin

from .models import Equipment, Rack, IPAddress


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['identification', 'responsible_sector', 'rack_installed', 'pop_installed', 'ip_address', 'description_equipment', 'created', 'created_by', 'status']
    search_fields = ['identification', 'pop_installed__name', 'status']
    list_filter = ['created_by', 'identification']

class IPAddressAdmin(admin.ModelAdmin):
    list_display = ['ip', 'network', 'subnet', 'equipment', 'is_available', 'created_at', 'updated_at']
    search_fields = ['ip', 'network', 'subnet', 'created_at']
    list_filter = ['ip', 'network', 'subnet']

class RackAdmin(admin.ModelAdmin):
    list_display = ['identification', 'pop_installed', 'created', 'created_by', 'status']
    search_fields = ['identification', 'pop_installed__name', 'status']
    list_filter = ['created_by', 'identification']


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(IPAddress, IPAddressAdmin)
admin.site.register(Rack, RackAdmin)