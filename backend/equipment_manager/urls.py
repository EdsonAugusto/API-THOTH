from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
urlpatterns = [
    path('query-vsc/<int:softswitch_vsc_id>/<int:command_id>/',
    views.Query_VSCDB, name='Query_VSCDB'),
]

router.register('commands', views.CommandsViewset, basename='commands_equipment')

urlpatterns=router.urls + urlpatterns