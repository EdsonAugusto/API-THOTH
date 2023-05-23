from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated


from .models import LogEntry
from .serializers import LogEntrySerializer


class LogEntryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('user', 'content_type', 'object_id', 'action', 'timestamp')
    search_fields = ('user', 'content_type', 'object_id')
    ordering_fields = ('user', 'content_type', 'object_id')