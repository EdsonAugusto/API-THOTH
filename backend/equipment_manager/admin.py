from django.contrib import admin
from .models import Command

class CommandAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'server_type', 'command_type']
    search_fields = ['title', 'server_type', 'command_type']
    list_filter = ['title', 'server_type', 'command_type']

    
admin.site.register(Command, CommandAdmin)