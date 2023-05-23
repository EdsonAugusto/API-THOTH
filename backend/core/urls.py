from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api/companys', views.CompanyViewset, basename='companys')
router.register('api/sectors', views.SectorViewset, basename='sectors')
router.register('api/extensions', views.ExtensionsViewset, basename='extensions')
router.register('api/datacenters', views.DataCenterViewset, basename='datacenters')
router.register('api/access', views.AccessReleaseViewset, basename='access')
router.register('api/important-accesses', views.ImportantAccessesViewset, basename='ImportantAccesses')
router.register('api/pro-active-contacts', views.ProActiveContactsViewset, basename='ProActiveContacts')
router.register('api/provider-contacts', views.ProviderContactsViewset, basename='ProviderContacts')

urlpatterns=router.urls