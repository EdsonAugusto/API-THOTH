from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('server_vsc', views.Softswitch_VSCViewset, basename='server_vsc')
router.register('server_gateway', views.Server_GatewayViewset, basename='server_gateway')
router.register('server_pabx', views.Server_PABxViewset, basename='server_pabx')
router.register('server_portability', views.Server_PortabilityViewset, basename='server_portability')
router.register('server_xserver', views.Server_XenServerViewset, basename='server_xserver')


urlpatterns=router.urls