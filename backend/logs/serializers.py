from rest_framework import serializers
from django.contrib.admin.models import LogEntry

class LogEntrySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    content_type = serializers.StringRelatedField()

    class Meta:
        model = LogEntry
        fields = ['user', 'content_type', 'object_id']