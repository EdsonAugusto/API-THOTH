from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from voip.models import Softswitch_VSC
from .utils import Macro_SQL
from .models import Command
from .serializers import CommandSerializer

def row_to_dict(row):
    print({column[0]: value for column, value in zip(row.cursor_description,row)})
    return {column[0]: value for column, value in zip(row.cursor_description,row)}

def Query_VSCDB(request, softswitch_vsc_id, command_id):
    softswitch_vsc = Softswitch_VSC.objects.get(id=softswitch_vsc_id)
    manager_sql_server = softswitch_vsc.get_manager_sql_server()
    command = Command.objects.get(id=command_id)
    # Example of using the manager_sql_server instance for querying
    result = manager_sql_server.query_sql(command.command)
    # Example of using Macro_SQL with the manager_sql_server instance
    result_dict = [row_to_dict(row) for row in result]
    return JsonResponse({"result": result_dict}, safe=False) # Use result_dict instead of result

class CommandsViewset(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('title', 'status', 'server_type', 'command_type', 'command', 'note')
    search_fields = ('title', 'status', 'server_type')
    ordering_fields = ('title', 'status', 'server_type')