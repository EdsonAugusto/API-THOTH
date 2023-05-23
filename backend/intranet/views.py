from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import (Category, Article, FAQ, Procedure, TechnicalDictionary, ShiftHandover, Notice,
                     GeneralProblem, Announcement, SystemMaintenance, TeamMeeting, BestPractice,
                     Reminder, GeneralNotes)
from .serializers import (CategorySerializer, KnowledgeBaseItemSerializer, TechnicalDictionarySerializer,
                          ShiftHandoverSerializer, NoticeSerializer, GeneralProblemSerializer,
                          AnnouncementSerializer, SystemMaintenanceSerializer, TeamMeetingSerializer,
                          BestPracticeSerializer, ReminderSerializer, GeneralNotesSerializer)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['created', 'updated_by']

class KnowledgeBaseItemViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = KnowledgeBaseItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'category__name']
    ordering_fields = ['category', 'created_by', 'created', 'updated_by']

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = KnowledgeBaseItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'category__name']
    ordering_fields = ['category', 'created_by', 'created', 'updated_by']

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = KnowledgeBaseItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'category__name']
    ordering_fields = ['category', 'created_by', 'created', 'updated_by']

class TechnicalDictionaryViewSet(viewsets.ModelViewSet):
    queryset = TechnicalDictionary.objects.all()
    serializer_class = TechnicalDictionarySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['term']
    ordering_fields = ['created_by', 'created', 'updated_by']

class ShiftHandoverViewSet(viewsets.ModelViewSet):
    queryset = ShiftHandover.objects.all()
    serializer_class = ShiftHandoverSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['start_time', 'end_time', 'created_by__username', 'handed_over_to__username']
    ordering_fields = ['created_by', 'handed_over_to', 'created', 'updated_by']

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'author__username']
    ordering_fields = ['author', 'created', 'updated_by']

class GeneralProblemViewSet(viewsets.ModelViewSet):
    queryset = GeneralProblem.objects.all()
    serializer_class = GeneralProblemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'created_by__username']
    ordering_fields = ['created_by', 'resolved', 'created', 'updated_by']

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'author__username']
    ordering_fields = ['author', 'start_date', 'end_date', 'created', 'updated_by']

class SystemMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = SystemMaintenance.objects.all()
    serializer_class = SystemMaintenanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'created_by__username']
    ordering_fields = ['created_by', 'start_time', 'end_time', 'completed', 'created', 'updated_by']

class TeamMeetingViewSet(viewsets.ModelViewSet):
    queryset = TeamMeeting.objects.all()
    serializer_class = TeamMeetingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'created_by__username', 'location']
    ordering_fields = ['created_by', 'date', 'time', 'location', 'created', 'updated_by']

class BestPracticeViewSet(viewsets.ModelViewSet):
    queryset = BestPractice.objects.all()
    serializer_class = BestPracticeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'category__name']
    ordering_fields = ['category', 'created_by', 'created', 'updated_by']

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'assigned_to__username']
    ordering_fields = ['assigned_to', 'due_date', 'completed', 'created', 'updated_by']

class GeneralNotesViewSet(viewsets.ModelViewSet):
    queryset = GeneralNotes.objects.all()
    serializer_class = GeneralNotesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'created_by__username']
    ordering_fields = ['created_by', 'resolved', 'created', 'updated_by']