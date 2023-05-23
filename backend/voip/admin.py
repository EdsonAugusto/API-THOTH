from django.contrib import admin

from .models import Softswitch_VSC, Server_Gateway, Server_Portability, Server_XenServer, Server_PABx
from .forms import Softswitch_VSCAdminForm, Server_GatewayAdminForm, Server_PABxAdminForm, Server_PortabilityAdminForm, Server_XenServerAdminForm


class Softswitch_VSC_Admin(admin.ModelAdmin):
    form = Softswitch_VSCAdminForm
    list_display = ['id_vsc', 'identification', 'server_type', 'ip_address', 'portability_server', 'idrac', 'server_port_count']
    search_fields = ['identification', 'server_type']
    list_filter = ['server_type', 'portability_server']

class Server_Gateway_Admin(admin.ModelAdmin):
    form = Server_GatewayAdminForm
    list_display = ['identification', 'ip_address',  'server_type']
    search_fields = ['identification']

class Server_PABx_Admin(admin.ModelAdmin):
    form = Server_PABxAdminForm
    list_display = ['identification', 'ip_address', 'server_type']
    search_fields = ['identification']

class Server_Portability_Admin(admin.ModelAdmin):
    form = Server_PortabilityAdminForm
    list_display = ['identification', 'ip_address']
    search_fields = ['identification']

class Server_XenServer_Admin(admin.ModelAdmin):
    form = Server_XenServerAdminForm
    list_display = ['identification', 'ip_address']
    search_fields = ['identification']


admin.site.register(Softswitch_VSC, Softswitch_VSC_Admin)
admin.site.register(Server_Gateway, Server_Gateway_Admin)
admin.site.register(Server_PABx, Server_PABx_Admin)
admin.site.register(Server_Portability, Server_Portability_Admin)
admin.site.register(Server_XenServer, Server_XenServer_Admin)