from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('ipaddress', views.IPAddressViewset, basename='ipaddress')
router.register('equipments', views.EquipmentViewset, basename='equipments')
router.register('racks', views.RackViewset, basename='racks')

urlpatterns=router.urls