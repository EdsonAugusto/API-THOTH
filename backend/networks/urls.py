from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('Switchs', views.SwitchViewset, basename='Switchs')
router.register('SwitchPorts', views.SwitchPortViewset, basename='SwitchPorts')


urlpatterns=router.urls