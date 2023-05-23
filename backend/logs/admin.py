from django.contrib import admin
from .models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'object_id', 'content_object', 'action', 'timestamp']
    search_fields = ['user', 'content_type', 'object_id']
    list_filter = ['user', 'content_type', 'object_id']


admin.site.register(LogEntry, LogEntryAdmin)