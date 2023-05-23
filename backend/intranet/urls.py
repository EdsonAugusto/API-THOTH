from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('articles', views.KnowledgeBaseItemViewSet, basename='articles')
router.register('faqs', views.FAQViewSet, basename='faqs')
router.register('procedures', views.ProcedureViewSet, basename='procedures')
router.register('technical-dictionaries', views.TechnicalDictionaryViewSet, basename='technical-dictionaries')
router.register('shift-handovers', views.ShiftHandoverViewSet, basename='shift-handovers')
router.register('notices', views.NoticeViewSet, basename='notices')
router.register('general-problems', views.GeneralProblemViewSet, basename='general-problems')
router.register('announcements', views.AnnouncementViewSet, basename='announcements')
router.register('system-maintenances', views.SystemMaintenanceViewSet, basename='system-maintenances')
router.register('team-meetings', views.TeamMeetingViewSet, basename='team-meetings')
router.register('best-practices', views.BestPracticeViewSet, basename='best-practices')
router.register('reminders', views.ReminderViewSet, basename='reminders')
router.register('general-notes', views.GeneralNotesViewSet, basename='general-notes')

urlpatterns = router.urls