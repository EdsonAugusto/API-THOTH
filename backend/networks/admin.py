from django.contrib import admin
from .models import Switch, SwitchPort

class SwitchAdmin(admin.ModelAdmin):
    list_display = ['identification', 'manufacturer', 'model', 'is_manageable', 'installation_date', 'warranty_period', 'number_of_ports', 'port_speed', 'created', 'created_by', 'status']
    search_fields = ['identification', 'manufacturer', 'model', 'is_manageable']
    list_filter = ['created_by', 'manufacturer', 'model', 'is_manageable']

class SwitchPortAdmin(admin.ModelAdmin):
    list_display = ['switch', 'port_number', 'vlan', 'protocol', 'speed']
    search_fields = ['switch__identification', 'port_number', 'vlan', 'protocol', 'speed']
    list_filter = ['switch', 'protocol']

admin.site.register(Switch, SwitchAdmin)
admin.site.register(SwitchPort, SwitchPortAdmin)