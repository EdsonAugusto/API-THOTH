from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('equipment_logs', views.LogEntryViewset, basename='equipment_logs')

urlpatterns = router.urls